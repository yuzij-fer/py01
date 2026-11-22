#识别处理画面，得到目标方位
import logging
import queue
from ultralytics import YOLO
import cv2
import numpy as np
from config import HSV_LOWER,HSV_UPPER


class Detector:
    def __init__(self,p_queue,model_path='best.pt'):  #自定义模型与监测阈值
        self.model = YOLO(model_path)
        self.p_queue = p_queue
        self.last_img = None      # 最近一帧，给主线程画框用
        self.lower= HSV_LOWER
        self.upper= HSV_UPPER

    def deal(self):               #调用yolo优先处理
        try:
            img=self.p_queue.get(timeout=0.25)
        except queue.Empty:       # 队列空是正常情况，不是异常
            return False , None
        self.last_img = img
        try:
            result=self.model(img,conf=0.3,verbose=False)
            boxes=result[0].boxes
            if len(boxes)>0:
                box=boxes[0]
                x1,y1,x2,y2=box.xyxy[0].cpu().numpy()
                return True  ,  (int(x1),int(y1),int(x2),int(y2))
        except Exception as e:
            logging.error(f"YOLO推理异常{e}")


#--------------------------yolo失败转用opencv--------------------------------

        try:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lower, self.upper)
            kernel = np.ones((5,5),np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            contour,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(contour)>0:
                cnt=max(contour,key=cv2.contourArea)
                if cv2.contourArea(cnt)>50:
                    x,y,w,h = cv2.boundingRect(cnt)
                    return  True ,  (int(x),int(y),int(x+w),int(y+h))
        except Exception as e:
            logging.error(f'opencv推理异常{e}')
        return  True , None