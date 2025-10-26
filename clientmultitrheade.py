import socket
import threading
import datetime

# Konfigurasi client
HOST = "localhost"
PORT = 12345
JUMLAH_REQUEST = 10

def kirim_pesan(nomor):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            waktu = datetime.datetime.now().strftime("%H:%M:%S")

            pesan = f"Halo dari client-{nomor} pada {waktu}"
            client.sendall(pesan.encode())

            data = client.recv(1024)
            print(f"[{waktu}] Balasan untuk client-{nomor}: {data.decode()}")
    except Exception as e:
        print(f"[X] Client-{nomor} error: {e}")

def main():
    threads = []

    print(f"Mengirim {JUMLAH_REQUEST} request bersamaan ke server...\n")

    for i in range(1, JUMLAH_REQUEST + 1):
        t = threading.Thread(target=kirim_pesan, args=(i,))
        threads.append(t)
        t.start()

    # Tunggu semua thread selesai
    for t in threads:
        t.join()

    print("\nSemua request telah dikirim dan diterima server.")

if __name__ == "__main__":
    main()
