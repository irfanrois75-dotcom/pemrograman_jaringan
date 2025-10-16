import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 12346)

while True:
    pesan = input("Kirim pesan ('exit' untuk keluar): ")
    if pesan.lower() == "exit":
        break
    
    client_socket.sendto(pesan.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    print(f"Balasan server: {data.decode()}")
