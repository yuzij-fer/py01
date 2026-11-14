#接口端双线处理接受与发出
import queue
import serial
import socket
import threading
class Network:
    def __init__(self,q_send, q_reiv,stop_event):
        self.q_send = q_send
        self.q_reiv = q_reiv
        self.stop_event = stop_event
        self.boss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.boss.bind(('127.0.0.1',8080))
        self.boss.listen(5)
        self.a, self.b = self.boss.accept()

    def start(self):
        threading.Thread(target=self.send,daemon=True).start()
        threading.Thread(target=self.recv,daemon=True).start()
    def send(self):
        while not self.stop_event.is_set()  and  not self.q_send.empty():
            try:
                 msg=self.q_send.get(timeout=1)
                 msg_send=f'<START>{msg}</START>'
                 self.a.send(msg_send.encode())

            except self.q_send.empty():
                pass

    def recv(self):
        while not self.stop_event.is_set() :
            try:
                data=self.a.recv(1024).decode()
                data_receive=data.replace('<START>','').replace('</START>','')
                self.q_reiv.put(data_receive)
            except Exception :
                break

class Server:
    def __init__(self,q_send,q_recv, stop_event):
        self.q_send = q_send
        self.q_recv = q_recv
        self.ser=serial.Serial('COM',9600)
        self.stop_event = stop_event

    def start(self):
        threading.Thread(target=self.send, daemon=True).start()
        threading.Thread(target=self.recv, daemon=True).start()

    def send(self):
        while not self.stop_event.is_set() and not self.q_send.empty():
            try:
                msg=self.q_send.get(timeout=1)
                msg_send=b'\xAA'+msg.encode()+b'\x55'
                self.ser.write(msg_send.encode())
            except queue.Empty :
                pass

    def recv(self):
        while not self.stop_event.is_set():
            try:
                data = self.ser.read_all()
                data_receive=data.replace(b'\xAA','').replace(b'\x55','')
                self.q_recv.put(data_receive.decode())
            except Exception :
                break






