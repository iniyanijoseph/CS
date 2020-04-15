import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 65533))
s.listen(10)

while True:
    conn, adr = s.accept()
    msg = b""
    while True:
        packet = conn.recv(4093)
        print(packet)
        if sys.getsizeof(packet) < 4096:
            print("wassap")
            break
        msg += packet
    conn.sendall(msg)
























