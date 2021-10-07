import socket
import threading
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
msg_global = 'NULL'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


class client():
    def handle_client(conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        name_recieved = 0
        name = "NULL"

        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)

            if msg_length:

                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)


                global msg_global
                if name != "NULL":
                    msg_global = 'User/' + name + ': ' + msg

                #msg_new = msg_global
                #print(f"[VARS]", msg_global, msg, msg_new, msg_old)
                while name_recieved == 0:
                    name = msg
                    print(f"[CLIENT NAMED] {addr} is now known as {name}")
                    name_recieved = 1

                    #start ny thread til at skubbe beskeder til denne client.
                    pushThread = threading.Thread(target=send, args=(conn, name))
                    pushThread.start()
                    print("[STARTING pushThread]")

                if msg == DISCONNECT_MESSAGE:
                    print(f"[CLIENT DISCONNECT] Client {addr} disconnected")
                    connected = False

                print(f"[{addr}] {msg}")

            if connected == False:
                break

    def send(conn, name):
        connected = True
        msg_new = "NULL"
        msg_old = msg_new
        global msg_global

        while connected:

            msg_new = msg_global

            if msg_new != msg_old:
                msg = msg_new
                conn.send(msg.encode(FORMAT))
                #send(conn, msg_new)

                print(f"[MSG SENT] sent {msg_new}")

                msg_old = msg_new
            #time.sleep(10)

    def test():
        return True



class listen():
    def listenStart():
        print("[STARTING]")
        server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

    def test():
        return True






#serverStart()
#listenStart()
