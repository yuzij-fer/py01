# 主线：相机线程 → 队列 → 识别 → 串口发送
import logging
import queue
import threading
import time
from camera import Camera
from connect import Ser
from finding import Detector
#import cv2
from  location import Get_distance


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s')
Poet='COM3'
baud=115200
width=640
height=480
fps=30
cap_id=0
img_w=width
img_h=height

stop_event=threading.Event()
p_queue = queue.Queue(maxsize=1)
cam=Camera(p_queue,stop_event,width=width,height=height,fps=fps,capid=cap_id)
cont= Ser(Poet,baud)
finder = Detector(p_queue)
location = Get_distance()
t1=threading.Thread(target=cam.running,daemon=True)

t1.start()

#被标记的代码为测试所用

time.sleep(1)



try:
    while not stop_event.is_set():
        box = finder.deal()
       # img=finder.last_img
        if box is not None:
            L=location.locate(box=box,img_w=img_w,img_h=img_h)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            try:
                if L['z'] is not None:
                    z = L['z']
                    dx = L['dx']
                    dy = L['dy']
                    ok=cont.send(dx,dy,z,notice=1)
                         #print(f'{c_x},{c_y},{ok}')
                    if ok:
                        logging.info("send")
                else:
                    logging.warning("距离出现问题")
                    dx = L['dx']
                    dy = L['dy']
                    z=0
                    ok = cont.send(dx, dy, z, notice=0)
            except Exception as e :
                logging.warning("发送异常")
        else:
            try:
                msg=cont.send_repeat(9999,9999,9999,notice=9999)  #无目标时发送悬停指令(9999,9999,9999 为保留值,超出像素范围)
                if msg:
                    logging.info("悬停成功",)
                else:
                    msg_new=cont.send_repeat(9999,9999,9999,notice=9999)
                    if not  msg_new:
                        logging.warning('悬停失败')
            except Exception as e :
                logging.warning('悬停失败%s',e)


        time.sleep(0.01)
        #cv2.imshow('img',img)
        #cv2.waitKey(1)
except KeyboardInterrupt:  #收到退出的指令
    logging.info("stop")
finally:
    stop_event.set()   #结束所有进程


