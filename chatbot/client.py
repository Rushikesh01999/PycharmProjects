import socket
from threading import Thread
client_socket=socket.socket()
client_socket.connect(("localhost",1000))
print("connected to the server")
def receive():
    print("hii")
    while True:
        data=client_socket.recv(10000)
        print("server:",data.decode())
def send():
    while True:
        user_input=input()
        client_socket.sendall(user_input.encode())

t=Thread(target=receive())
t.start()
send()