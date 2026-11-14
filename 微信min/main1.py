import threading
import queue
import user
import servers
import time

q_reiv=queue.Queue()
q_send=queue.Queue()
stop_event=threading.Event()

user1 = user.User(q_reiv=q_reiv,q_send=q_send,stop_event=stop_event)
user1.start()
network=servers.Network(q_send=q_send,q_reiv=q_reiv,stop_event=stop_event)
network.start()
while not stop_event.is_set():
    time.sleep(1)



