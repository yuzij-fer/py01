from camera import Camera
from location import Get_distance
from finding import Detector
from connect import Ser
import config
import time
import threading
import logging
import queue

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#内参自检：和分辨率对不上就警告，但不阻止运行
for _p in config.CAMERA.problems():
    logging.warning('内参自检：%s', _p)

p_queue = queue.Queue(maxsize=1)
stop_event = threading.Event()
camera = Camera(p_queue, stop_event)
ser = Ser(config.SERIAL_PORT, config.SERIAL_BAUD)
finder=Detector(p_queue)
location = Get_distance()

t1=threading.Thread(target=ser.recv_running, args=( stop_event,),daemon=True)
t2=threading.Thread(target=camera.running,daemon=True)
t1.start()
t2.start()
time.sleep(1)

#缓存数据
last_x=0.0
last_y=0.0
last_z=0.0
lock=False

#初始数据
img_w=config.WIDTH
img_h=config.HEIGHT
frame=0
Max_frame=24

try:
    while not  stop_event.is_set():
        now , box  =  finder.deal()

#----------------------------------正常识别-------------------------------
        if box  is  not None:
            L=location.locate(box,img_w,img_h)

            if L is not None:
                dx=L['dx']
                dy=L['dy']
                dz=L['z']
                last_x=dx
                last_y=dy
                last_z=dz
                lock=True
                frame=0
                try:
                    ok=ser.send(dx,dy,dz,notice=1)
                    if ok:
                        logging.info('send success')
                    else:
                        ser.send(dx, dy, dz, notice=1)
                except Exception as e:
                    logging.warning('send fail%s',e)
            else:
                logging.warning('位置测算失败')


#--------------------------------------未识别到目标------------------------------------
        elif  now and  lock:
            frame+=1
#--------------------------------------短暂丢失目标，复用缓存 ---------------------------
            if frame < Max_frame:
                try:
                    ok=ser.send(last_x,last_y,last_z,notice=2)
                    if ok:
                        logging.info('send success')
                    else:
                        ser.send(last_x, last_y, last_z, notice=2)
                except Exception as e:
                    logging.warning('send fail%s',e)

#------------------------------------目标消失，悬停----------------------------------
            else:
                try:
                    ok=ser.send(0,0,0,notice=0)
                    if ok :
                        logging.info('悬停成功')
                    else:
                        ser.send(0,0,0,notice=0)
                except Exception as e:
                    logging.warning('send fail%s',e)

#------------------------------刚开机未开始识别-------------------------------
        else:
            ser.send(0, 0, 0, 0)

        time.sleep(0.01)

except KeyboardInterrupt:
    logging.info('stop')

except Exception as e:
    logging.warning('main fail%s',e)
    stop_event.set()

finally:
    stop_event.set()
    ser.stop()
    logging.info('stop finish')
