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

#缓存数据
last_x= 0.0
last_y= 0.0
last_z= 0.0
lost_frame_cnt= 0
max_lost_frame= 24
#线程开始执行

t1.start()
time.sleep(1)


try:
    while not stop_event.is_set():
        now , box = finder.deal()
        if box is not None:
#=======================检测到目标=======================
            L=location.locate(box=box,img_w=WIDTH,img_h=HEIGHT)
            lost_frame_cnt= 0
            try:
                if L is not None:
                    z = L['z']
                    dx = L['dx']
                    dy = L['dy']
                    last_x = dx
                    last_y = dy
                    last_z = z
                    ok=cont.send(dx,dy,z,notice=1)
                    if ok:
                        logging.info("send success")
                else:
                    logging.warning('位置测算失败')
            except Exception as e :
                logging.warning("发送异常%s",e)

#------------------------------------ 队列没空，但未识别目标---------------------------------------

#========================目标暂时被遮挡=======================
        elif  now:
            lost_frame_cnt +=1
            if lost_frame_cnt <= max_lost_frame:
                try:
                    ok = cont.send(last_x, last_y, last_z, notice=2)
                    if ok:
                        logging.info(f"短时丢失目标，复用缓存数据,丢失{lost_frame_cnt}帧")
                except Exception as e :
                    logging.warning('缓存异常%s',e)
#========================目标长时间丢失，进入悬停====================
            else:
                try:
                    ok = cont.send(0 , 0 , 0 , notice=0)
                    if ok:
                        logging.info('悬停')
                    if not ok :
                        logging.warning('悬停失败')
                except Exception as e :
                    logging.warning('悬停异常%s',e)

#-------------------------------------队列空了-------------------------------------
#立即悬停
        else:
            cont.send(0 , 0 , 0 , notice=0)

        time.sleep(0.01)

except KeyboardInterrupt:  #收到退出的指令
    logging.info("stop")

except Exception as e :
    logging.warning('主循环异常%s',e)

finally:
    stop_event.set()   #结束所有进程
    cont.stop()
    logging.info("stop")
