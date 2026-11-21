#串口通信
import serial
import logging
import threading
import time
import struct


class Ser:
    def __init__(self,port='COM1',baud=115200):  #内定参数并打开串口
        self.ser = None
        self.port = port
        self.baud = baud
        self._lock = threading.Lock()
        self.open()

#打开串口
    def open(self) -> bool:
        try:
            self.ser = serial.Serial(self.port,self.baud,timeout=0.25)
            logging.info("Connected")
            return True
        except Exception as e:
            logging.error("Failed to connect to serial port")
            logging.error(e)
            self.ser = None
            return False

#尝试重新连接
    def reconnect(self) -> bool:
        if self.is_connected():
            return True
        logging.info("Reconnecting")
        return self.open()

#判断串口状态
    def is_connected(self) -> bool:
        return self.ser is not None and self.ser.is_open

#发送坐标
    def send(self,x,y,dist,notice) -> bool:
        x = max(0, min(9999, int(round(float(x)))))
        y = max(0, min(9999, int(round(float(y)))))
        dist = max(0, min(9999, int(round(float(dist)))))
        with self._lock:
            if not  self.is_connected() and not self.reconnect() :
                logging.warning("串口连接失败")
                return False
            pack=struct.pack("<ffff",x,y,dist,notice)
            #0xAA接收至0x55
            try:
                self.ser.write(b'\xAA'+pack+b'\x55')
                return True
            except Exception as e:
                logging.error("Failed to send data")
                logging.error(e)
                try:
                    self.ser.close()
                except Exception :
                    pass
                self.ser = None
                return False

 #————————————————————————————悬停重复发送指令————————————————————————————————

    def send_repeat(self,x,y,dist,notice,times=2,interval=0.02):
        for i in range(times):
            ok=self.send(x,y,dist,notice)
            if not ok:
                return False
            time.sleep(interval)
        return True

#断开连接
    def stop(self):
        with self._lock:
            if self.ser:
                self.ser.close()
                self.ser = None


