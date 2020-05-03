import socket
import sys
print(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 65526))
s.listen(100)

while True:
    conn, adr = s.accept()
    print("asdf")
    msg = b""
    packet = conn.recv(4096)
    while sys.getsizeof(packet) > 4000:
        msg += packet
        packet = conn.recv(4096)
    msg += packet
    conn.sendall(msg)