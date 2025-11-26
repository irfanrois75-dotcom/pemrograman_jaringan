import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -----------------------------
# 1. Timeout 3 detik saat connect
# -----------------------------
client.settimeout(3)

try:
    client.connect((HOST, PORT))
    print("Terhubung ke server!")
except socket.timeout:
    print("Koneksi timeout! (saat connect)")
    exit()
except Exception as e:
    print("Error lain:", e)
    exit()

# -----------------------------
# 2. Timeout 2 detik saat membaca data
# -----------------------------
client.settimeout(2)

try:
    data = client.recv(1024)  # menunggu data max 2 detik
    print("Data dari server:", data.decode())
except socket.timeout:
    print("Koneksi timeout! (saat membaca data)")
except Exception as e:
    print("Error lain:", e)

client.close()
