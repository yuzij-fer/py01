import serial
ser=serial.Serial('COM1',9600,timeout=1)
msg="你好".encode("utf-8")
ser.write(b'\xAA''+msg'+b'\x55')
data=ser.read_all()
print(data.decode("utf-8"))
ser.close()
