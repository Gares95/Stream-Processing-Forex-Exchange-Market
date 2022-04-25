import socket

if __name__ == '__main__':
    print("Starting Server...")

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 9000

    serversocket.bind((host,port)) 
    serversocket.listen(1)
    clientsocket,addr = serversocket.accept()
    with clientsocket:
        print(f"Connected to {addr}")
        while True:
            data = clientsocket.recv(1024)
            # Stop reading stream if data is not being received
            if not data:
                break
            message = data.decode('utf8')
            print("Message recieved: {}".format(message))

            
