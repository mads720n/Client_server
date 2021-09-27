import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.107.169.211"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(f"[CONNECTED] Client connected to {ADDR}")

#send funktion
def send(msg):
    #message variablen svarer til den utf-8 (byte) formaterede version af msg fra send funktionen
    message = msg.encode(FORMAT)
    #angiver længden af beskeden i bytes
    msg_length = len(message)
    #længden af beskeden, kodet i bytes
    send_length = str(msg_length).encode(FORMAT)
    """
    Gør at første besked til serveren bliver 64bytes.
    Serveren forventer at første besked er 64 bytes - Den første besked fortæller Serveren
    hvor lang den faktiske besked er.
    """
    send_length += b'' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

#Recieve funktion, tillader at modtage beskeder
def recieve():
    print(f"[LISTENING] Listening for messages from server")
    while True:
        encoded_message = client.recv(HEADER)
        print(encoded_message.decode(FORMAT))

#Naming
client_name = input("Please input your alias: ")
send(str(client_name))

print(f"You are connected to {ADDR} as \"{client_name}\"")
print(f"To disconnect, please type {DISCONNECT_MESSAGE}")
print("")

#Starter recieve funktionen i seperat tråd
thread = threading.Thread(target=recieve)
thread.start()

#Messaging loop
while True:
    besked = input()
    besked = str(besked)

    #kun ved DISCONNECT_MESSAGE
    if besked == DISCONNECT_MESSAGE:
        send(besked)
        print(f"[DISCONNECTED]")
        break
    #ellers normal funktion via send funktionen
    else:
        send(besked)
