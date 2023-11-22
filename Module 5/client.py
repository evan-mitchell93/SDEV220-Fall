import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((SERVER_HOST,SERVER_PORT))
    msg = input("Enter a message: ")
    while msg != "QUIT":
        c.send(str.encode(msg))
        msg = input("Enter another message: ")
        data = c.recv(1024)
        print(f"Server said: {data}")