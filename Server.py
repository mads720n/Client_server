import socket
import threading
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    name_recieved = 0


    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            while name_recieved == 0:
                name = msg
                print(f"[CLIENT NAMED] {addr} is now known as {name}")
                name_recieved = 1

            if msg == DISCONNECT_MESSAGE:
                print(f"[CLIENT DISCONNECT] Client {addr} disconnected")
                connected = False

            print(f"[{addr}] {msg}")
        if connected == False:
            break

def send_msg(conn, message):
    welcome_msg = "Hello, you are now connected to SERVER"
    conn.send(welcome_msg.encode(FORMAT))
    #print(f"msg sent {message}, {message.encode(FORMAT)} to {conn}")
    while True:
        conn.send(message.encode(FORMAT))


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[STARTING]")

start()
