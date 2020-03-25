import socket
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9873))
s.listen(2)

while True:
    conn, adr = s.accept()
    msg = pickle.loads(conn.recv(1024))
    conn.send(msg)