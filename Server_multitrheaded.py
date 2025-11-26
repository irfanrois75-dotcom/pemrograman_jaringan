import socket
import threading

HOST = "0.0.0.0"
PORT = 5050

# daftar client yang sedang terhubung
clients = []

def broadcast(message, sender_conn):
    """Kirim pesan ke semua client kecuali pengirim"""
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[TERHUBUNG] {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            
            print(f"Pesan dari {addr}: {msg.decode()}")
            broadcast(msg, conn)

        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"[DISCONNECT] {addr}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER JALAN] Listening di port {PORT}")

    while True:
        conn, addr = server.accept()
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()

