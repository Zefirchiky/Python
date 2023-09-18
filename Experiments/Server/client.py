from settings import *
import socket
import threading

HEADER = 64
PORT = 5050
DISCONNECT_MSG = '!!!_DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(_msg):
    msg = _msg.encode('utf-8')
    msg_len = len(msg)
    send_len = str(msg_len).encode('utf-8')
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(msg)

def msg_input():
    while True:
        msg = input(f"Say something to server: \n")
        if msg == DISCONNECT_MSG:
            break
        send(msg)

def msg_handler():
    while True:
        msg = client.recv(1024).decode('utf-8')
        print(msg)
    
thread = threading.Thread(target=msg_input)
thread2 = threading.Thread(target=msg_handler)
thread.start()
thread2.start()


