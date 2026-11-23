#识别处理画面，得到目标方位
import logging
import queue
from ultralytics import YOLO
import cv2
import numpy as np
from config import HSV_LOWER, HSV_UPPER, MAX_JUMP


class Detector:
    def __init__(self, p_queue, model_path='best.pt'):  #自定义模型与监测阈值
        self.model = YOLO(model_path)
        self.p_queue = p_queue
        self.last_img = None      # 最近一帧，给主线程画框用
        self.lower = HSV_LOWER
        self.upper = HSV_UPPER
        self.max_jump = MAX_JUMP
        self.locked = None        # 上一帧锁定的框 (x1,y1,x2,y2)

    def pick(self, cands):
        if not cands:                            # 一个候选都没有
            return None

        if self.locked is None:                  # 没有历史，按分数选一个
            best = max(cands, key=lambda c: c[4])
            self.locked = best[:4]               # 只留坐标，丢掉分数
            return self.locked

        lx = (self.locked[0] + self.locked[2]) / 2
        ly = (self.locked[1] + self.locked[3]) / 2

        # 候选中心到上一帧锁定中心的距离平方（比较大小不需要开根号）
        def dist(c):
            return ((c[0] + c[2]) / 2 - lx) ** 2 + ((c[1] + c[3]) / 2 - ly) ** 2

        near = min(cands, key=dist)

        if dist(near) ** 0.5 < self.max_jump:    # 在容许位移内，认作同一个目标
            self.locked = near[:4]
            return near[:4]

        self.locked = None                       # 锁定目标真的消失
        return None                              # 这一帧不换靶

    def deal(self):               #调用yolo优先处理
        try:
            img = self.p_queue.get(timeout=0.25)
        except queue.Empty:       # 队列空是正常情况，不是异常
            return False, None
        self.last_img = img

#------------------------------1. YOLO：只产出候选，不负责选------------------------------
        cands = []
        try:
            result = self.model(img, conf=0.6, verbose=False)
            for b in result[0].boxes:            # 遍历全部框，不再取 boxes[0]
                x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
                cands.append((x1, y1, x2, y2, float(b.conf)))
        except Exception as e:
            logging.error(f"YOLO推理异常{e}")

        if cands:                                # 有候选就在这里停
            return True, self.pick(cands)

#--------------------------yolo失败转用opencv--------------------------------
        cands = []
        try:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lower, self.upper)
            kernel = np.ones((5,5),np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            contour,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contour:
                area = cv2.contourArea(cnt)
                if area > 50:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cands.append((x, y, x + w, y + h, area))
        except Exception as e:
            logging.error(f'opencv推理异常{e}')

        return True, self.pick(cands)
