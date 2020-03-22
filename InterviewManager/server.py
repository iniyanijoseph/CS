import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} has been established")
    clt.send(bytes("So... this is sockets", "utf-8"))