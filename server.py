import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12346))

print("Server aktif dan mencatat pesan client...")

while True:
    data, addr = server_socket.recvfrom(1024)
    pesan = data.decode()
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Cetak di terminal
    print(f"[{waktu}] Pesan dari {addr}: {pesan}")
    
    # Simpan ke file log
    with open("server_log.txt", "a") as file:
        file.write(f"[{waktu}] {addr} : {pesan}\n")
    
    # Kirim balasan ke client
    balasan = f"Server telah menerima pesan '{pesan}' pada {waktu}"
    server_socket.sendto(balasan.encode(), addr)
