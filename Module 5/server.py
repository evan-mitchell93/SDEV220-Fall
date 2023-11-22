import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #socket binds to the ip and port #
    s.bind((HOST,PORT))
    #socket listens for connection requests
    s.listen()
    #blocks execution until a connection is established
    #conn is socket object, addr is tuple of client IP,PORT
    conn,addr = s.accept()
    with conn:
        print(f"Client information: {addr}")
        while True:
            #Read 1024 bytes worth of data from the client
            data = conn.recv(1024)
            print(f"{data}")
            if not data:
                break
            #respond to client with same message
            conn.send(data)

