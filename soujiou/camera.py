#摄像头采集,保存画面
import cv2
import logging
import numpy as np
import queue
import time



class Camera :
    #内定参数可自定义
    def __init__ (self,p_queue,stop_event,width=640,height=480,fps=30,capid=0):
        self.width=width
        self.height=height
        self.fps=fps
        self.cap_id=capid
        self.p_queue = p_queue
        self.stop_event=stop_event
        self._init_camera()
        self.camera_mtx = np.array([[945.15025581, 0., 431.22090007],
                               [0., 786.09360996, 261.05788457],
                               [0., 0., 1.]], dtype=np.float32)

        self.camera_dist = np.array([[-1.36251624e+00, 6.68606376e+00, 8.73288483e-02, -2.84729744e-03, -9.19749936e+00]],
                               dtype=np.float32)

#导入参数
    def _init_camera(self):
        self.cap = cv2.VideoCapture(self.cap_id)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)

#开始获取数据
    def capture(self):
       try:
           ret, frame = self.cap.read()
       except Exception as e:
           logging.warning(f'捕捉异常{e}')
           return False
       if not ret:
            logging.warning('摄像头未捕捉到画面')
            return False
       frame_undistorted = cv2.undistort(frame, self.camera_mtx, self.camera_dist)
       if  self.p_queue.full():#队列满，直接丢弃老数据
            try:
               self.p_queue.get_nowait()
            except queue.Empty :
                pass
       self.p_queue.put(frame_undistorted)
       return True

    def stop(self):
        self.stop_event.set()

#——————————————————————————————开始运行————————————————————————————
    def running(self):
        try:
            while  not self.stop_event.is_set():
                if not  self.cap.isOpened():
                    logging.warning('摄像头未打开')
                    self.cap.release()
                    time.sleep(1)
                    self._init_camera() #尝试重连
                    continue            # 重连后跳过本轮，下一轮再采集
                self.capture()
        finally:
            self.cap.release()          # 线程退出时释放摄像头，否则被占用
            logging.info('相机线程已退出')