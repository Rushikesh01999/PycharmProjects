import socket
from threading import Thread
server_socket=socket.socket()
server_socket.bind(("",1000))
print("server in bounded to port")
server_socket.listen()
print("server is listening")
conn,addr=server_socket.accept()
print("found client")
def receive():
    while True:
        data=conn.recv(1000)
        print("client:",data.decode())


def send():
    while True:
        msg=input()
        conn.sendall(msg.encode())
t=Thread(target=receive())
t.start()
send()