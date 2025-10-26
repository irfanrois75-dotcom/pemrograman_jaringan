import socket
import threading
from datetime import datetime

SERVER_ADDRESS = ("localhost", 12345)  # ubah ke IP server kalau beda laptop
JUMLAH_REQUEST = 10  # jumlah request yang dikirim bersamaan


def kirim_pesan(nomor):
    """Fungsi untuk mengirim satu pesan ke server"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pesan = f"Request ke-{nomor}"
    client_socket.sendto(pesan.encode(), SERVER_ADDRESS)

    try:
        client_socket.settimeout(3)
        data, _ = client_socket.recvfrom(1024)
        waktu = datetime.now().strftime("%H:%M:%S")
        print(f"[{waktu}] Balasan untuk {pesan}: {data.decode()}")
    except socket.timeout:
        print(f"❌ Request ke-{nomor} tidak mendapat balasan (timeout)")
    finally:
        client_socket.close()

def main():
    threads = []

    print(f"Mengirim {JUMLAH_REQUEST} request bersamaan ke server...\n")

    # Jalankan 10 thread client
    for i in range(1, JUMLAH_REQUEST + 1):
        t = threading.Thread(target=kirim_pesan, args=(i,))
        threads.append(t)
        t.start()

    # Tunggu semua thread selesai
    for t in threads:
        t.join()

    print("\n✅ Semua request telah dikirim.")


if __name__ == "__main__":
    main()