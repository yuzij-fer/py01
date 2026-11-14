import socket
clint=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clint.connect(('127.0.0.1', 8080))
clint.send("嗨咯".encode("utf-8"))
data=clint.recv(1024).decode("utf-8")
print(data)
clint.close()