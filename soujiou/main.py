# 主线：相机线程 → 队列 → 识别 → 串口发送
import logging
import queue
import threading
import time
from camera import Camera
from config import (CAMERA, WIDTH, HEIGHT, FPS, CAP_ID,
                    SERIAL_PORT, SERIAL_BAUD)
from connect import Ser
from finding import Detector
#import cv2
from location import Get_distance


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s')

#内参自检：和分辨率对不上就警告，但不阻止运行
for _p in CAMERA.problems():
    logging.warning('内参自检：%s', _p)

stop_event=threading.Event()
p_queue = queue.Queue(maxsize=1)
cam=Camera(p_queue,stop_event,width=WIDTH,height=HEIGHT,fps=FPS,capid=CAP_ID)
cont= Ser(SERIAL_PORT,SERIAL_BAUD)
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
            L=location.locate(box=box,img_w=WIDTH,img_h=HEIGHT)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            try:
                if L is not None:
                    z = L['z']
                    dx = L['dx']
                    dy = L['dy']
                    ok=cont.send(dx,dy,z,notice=1)
                         #print(f'{c_x},{c_y},{ok}')
                    if ok:
                        logging.info("send")
                else:
                    logging.warning('位置测算失败')
            except Exception as e :
                logging.warning("发送异常")
        else:
            try:
                msg=cont.send_repeat(0,0,0,notice=0)  #无目标时发送悬停指令(0,0,0 为保留值,超出像素范围)
                if msg:
                    logging.info("悬停成功",)
                else:
                    msg_new=cont.send_repeat(0,0,0,notice=0)
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
    cont.stop()

