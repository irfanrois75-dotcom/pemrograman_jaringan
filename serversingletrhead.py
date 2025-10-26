import socket
from datetime import datetime

# Konfigurasi server
HOST = "localhost"     # ubah ke IP server kalau antar laptop
PORT = 12345

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Server UDP single-thread berjalan di {HOST}:{PORT}")
print("Menunggu pesan dari client...\n")

try:
    while True:
        # Menerima pesan dari client (1 per 1)
        data, address = server_socket.recvfrom(1024)
        pesan = data.decode()
        waktu = datetime.now().strftime("%H:%M:%S")

        print(f"[{waktu}] Pesan diterima dari {address}: {pesan}")

        # Membuat balasan
        balasan = f"Server menerima: '{pesan}' pada {waktu}"
        server_socket.sendto(balasan.encode(), address)

except KeyboardInterrupt:
    print("\nServer dihentikan secara manual.")
finally:
    server_socket.close()
