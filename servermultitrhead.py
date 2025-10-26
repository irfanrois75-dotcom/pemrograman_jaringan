import socket
import threading
import datetime

# Konfigurasi server
HOST = "localhost"
PORT = 12345

# Fungsi untuk menangani tiap client
def handle_client(conn, addr):
    print(f"[TERHUBUNG] Client {addr} terhubung ke server.")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            pesan = data.decode()
            waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Tampilkan di server
            print(f"[{waktu}] Pesan dari {addr}: {pesan}")

            # Balas ke client
            balasan = f"Server menerima: {pesan} pada {waktu}"
            conn.sendall(balasan.encode())

    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan dengan {addr}: {e}")
    finally:
        conn.close()
        print(f"[PUTUS] Koneksi dari {addr} ditutup.")

# Menjalankan server utama
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[MENUNGGU] Server berjalan di {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        # Buat thread untuk tiap client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[AKTIF] Jumlah thread aktif: {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
