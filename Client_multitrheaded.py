import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def listen_server():
    while True:
        try:
            msg = client.recv(1024).decode()
            print("\n[Broadcast] " + msg)
        except:
            break

def send_message():
    while True:
        pesan = input()
        client.send(pesan.encode())

thread_listen = threading.Thread(target=listen_server)
thread_listen.daemon = True
thread_listen.start()

send_message()
