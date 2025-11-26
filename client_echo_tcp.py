import socket

HOST = "127.0.0.1"   # server lokal
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

pesan = "Tes Koneksi"
client_socket.sendall(pesan.encode())

data = client_socket.recv(1024)
print("Balasan dari server:", data.decode())

client_socket.close()
