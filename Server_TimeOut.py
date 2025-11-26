import socket

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server berjalan...")

conn, addr = server.accept()
print("Client terhubung:", addr)

# Tidak mengirim data → untuk memicu timeout pada client
while True:
    pass
