import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((socket.gethostname(), 1234))

while True:
    msg = sock.listen(1024)
    if msg: 
        print(msg.decode("utf-8"))

