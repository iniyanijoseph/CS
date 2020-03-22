import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))
totmsg = ""
while True:
    msg = s.recv(7)
    totmsg += msg.decode("utf-8")
    print(totmsg)