import socket

HOST = "0.0.0.0"   # listen ke semua alamat
PORT = 5050

# buat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server berjalan di port {PORT}...")

conn, addr = server_socket.accept()
print(f"Terhubung dengan client: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    print("Pesan diterima dari client:", data.decode())
    conn.sendall(data)   # kirim balik (echo)

conn.close()
server_socket.close()
