from ultralytics import YOLO
import cv2
import numpy as np
import threading
import queue
import time
import logging
model=YOLO(r'/opencv/runs\detect\train\weights\best.pt')

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)s] - %(message)s')

camera_mtx = np.array([[945.15025581, 0., 431.22090007],
                       [0., 786.09360996, 261.05788457],
                       [0., 0., 1.]], dtype=np.float32)

camera_dist = np.array([[-1.36251624e+00, 6.68606376e+00, 8.73288483e-02, -2.84729744e-03, -9.19749936e+00]],
                       dtype=np.float32)


class VisionSystem:
    def __init__(self):
        self.frame_queue = queue.Queue(maxsize=5)
        self.is_running = True
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def camera_capture(self):
        logging.info("📷 摄像头采集线程启动...")
        while self.is_running:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame_undistorted = cv2.undistort(frame, camera_mtx, camera_dist)
            if self.frame_queue.full():
                self.frame_queue.get()

            self.frame_queue.put(frame_undistorted)
            time.sleep(0.01)

    def process_frame(self):
        logging.info("🧠 视觉处理线程启动...")
        while self.is_running or not self.frame_queue.empty():
            try:
                frame = self.frame_queue.get(timeout=1)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                lower_red = np.array([0, 120, 70])
                upper_red = np.array([10, 255, 255])
                mask = cv2.inRange(hsv, lower_red, upper_red)
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > 500:
                        x, y, w, h = cv2.boundingRect(cnt)
                        center_x = int(x + w / 2)
                        center_y = int(y + h / 2)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        text = f"({center_x}, {center_y})"
                        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        logging.info(f"发现目标: X={center_x}, Y={center_y}")
                cv2.imshow("Undistorted & Tracking", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.is_running = False
                    break
            except queue.Empty:
                pass

    def run(self):
        t_cam = threading.Thread(target=self.camera_capture, name="采集线程")
        t_ai = threading.Thread(target=self.process_frame, name="处理线程")

        t_cam.start()
        t_ai.start()

        t_cam.join()
        t_ai.join()

        self.cap.release()
        cv2.destroyAllWindows()
        logging.info("✅ 所有任务结束，系统安全退出。")


if __name__ == '__main__':
    app = VisionSystem()
    app.run()