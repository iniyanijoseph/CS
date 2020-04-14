import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 65535))
s.listen(2)

while True:
    conn, adr = s.accept()
    msg = b""
    for element in range(1000):
        packet = conn.recv(4096)
        if not packet:
            break
        msg += packet
    print(msg)
    conn.sendall(msg)
