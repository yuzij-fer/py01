#用户端接受与发出信息，双线程处理
import queue
import threading

class User:
    def __init__(self,q_reiv,q_send,stop_event):
        self.q_reiv=q_reiv
        self.q_send=q_send
        self.stop_event=stop_event

    def sendmessage(self):
        while not self.stop_event.is_set():
            msg=input('请输入：')
            if msg=='q':
                self.stop_event.set()
                break
            else:
                self.q_send.put(msg)

    def receivemessage(self):
        while not self.stop_event.is_set() or not self.q_reiv.empty():
            try:
                msg=self.q_reiv.get(timeout=0.25)
                print(msg)
            except queue.Empty:
                pass
    def start(self):
        threading.Thread(target=self.sendmessage,daemon=True).start()
        threading.Thread(target=self.receivemessage,daemon=True).start()

