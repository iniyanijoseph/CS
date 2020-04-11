import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9873))
s.listen(2)

while True:
    conn, adr = s.accept()
    data = b""
    for element in range(1000):
        data += s.recv(4096)
        if not data:
            break
    conn.sendall(data)
