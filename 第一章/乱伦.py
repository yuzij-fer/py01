# import threading
# import queue
# import time
# import logging
# import opencv
#
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
#
# class VisionSystem:
#     def __init__(self):
#         self.frame_queue = queue.Queue(maxsize=5)
#         self.is_running = True
#
#     def camera_capture(self):
#         logging.info("摄像头采集线程启动...")
#         frame_id = 0
#         while self.is_running:
#             time.sleep(0.05)
#             frame_id += 1
#
#             if self.frame_queue.full():
#                 logging.warning(f"传送带满了，丢弃图像_{frame_id}！")
#                 continue
#             self.frame_queue.put(f"图像_{frame_id}")
#             logging.info(f"抓取 图像_{frame_id}，放入队列")
#
#     def yolo_process(self):
#         logging.info("AI处理线程启动...")
#         while self.is_running or not self.frame_queue.empty():
#             try:
#                 data = self.frame_queue.get(timeout=1)
#
#                 time.sleep(0.1)
#                 logging.info(f"处理完成: {data}")
#
#             except queue.Empty:
#                 pass
#
#     # ================= 启动开关 =================
#     def run(self):
#         t_cam = threading.Thread(target=self.camera_capture)
#         t_ai = threading.Thread(target=self.yolo_process)
#
#         t_cam.start()
#         t_ai.start()
#
#         time.sleep(5)
#         self.is_running = False
#         logging.info("主程序发出停止信号...")
#
#         t_cam.join()
#         t_ai.join()
#         logging.info("所有任务结束，系统安全退出。")
#
#
# if __name__ == '__main__':
#     app = VisionSystem()
#     app.run()
import threading
import time
import queue
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class VisionSystem:
    def __init__(self):
        self.queue = queue.Queue(maxsize=5)
        self.running = True
    def acquire(self):
        logging.info('正在抓取画面')
        i=0
        while self.running:
            logging.info(f'以获取第{i+1}张画面')
            i+=1
            time.sleep(0.05)
            if self.queue.full():
                 logging.warning(f'图像已满丢弃第{i}张图')
                 continue
            self.queue.put(f'第{i}张图')
            logging.info(f'第{i}张图放入队列')
    def deal_ai(self):
        logging.info('开始处理图像')
        while self.running or not self.queue.empty():
            try:
                data=self.queue.get(timeout=5)
                logging.info(f'正在处理{data}')
                time.sleep(0.1)
                logging.info(f'处理完{data}')

            except queue.Empty:
                 pass
    def run(self):
        t1 = threading.Thread(target=self.deal_ai)
        t2=threading.Thread(target=self.acquire)
        t1.start()
        t2.start()

        time.sleep(5)
        self.running = False
        logging.info('任务停止')
        t1.join()
        t2.join()
        logging.info('任务结束')
if __name__ == '__main__':
    app = VisionSystem()
    app.run()