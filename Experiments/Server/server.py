from settings import *
import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '192.168.0.196'
ADDR = (SERVER, PORT)
DISCONNECT_MSG = '!!!_DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_messages(msg, _conn):
    for client in clients:
        conn = client[0]
        if conn != _conn:
            conn.send(msg.encode("utf-8"))

def handle_client(conn, addr):
    print(f"{GREEN_TEXT}[NEW CONNECTION] {addr} connected.{FORMAT_CLEAR}")
    print(f"{YELLOW_TEXT}[ACTIVE CONECTIONS] {threading.active_count() - 1}.{FORMAT_CLEAR}")
    print(f"{YELLOW_TEXT}[ACTIVE CONNECTIONS] {[addr for _, addr in clients]}{FORMAT_CLEAR}")

    connected = True
    while connected:
        try:
            msg_len = conn.recv(HEADER).decode('utf-8')
            if msg_len:
                msg_len = int(msg_len)
                msg = conn.recv(msg_len).decode('utf-8')
                if msg == DISCONNECT_MSG:
                    connected = False

                print(f"[{addr}] {msg}")
                handle_messages(msg, conn)
        except ConnectionResetError:
            connected = False

    print(f"{RED_TEXT}[DISCONNECT] {addr} disconnected{FORMAT_CLEAR}")
    conn.close()

def start():
    print(f"{YELLOW_TEXT}[STARTING] Server is starting...{FORMAT_CLEAR}")
    server.listen()
    print(f"{YELLOW_TEXT}[LISTENING] Server is listening on {SERVER}...{FORMAT_CLEAR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(clients)

if __name__ == "__main__":
    start()



