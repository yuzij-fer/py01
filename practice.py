import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(5)
a,b=s.accept()
data=a.recv(1024).decode("utf-8")
print(data)
a.send("你好".encode("utf-8"))
a.close()

