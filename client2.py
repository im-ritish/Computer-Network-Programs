import socket 

IP=socket.gethostbyname(socket.gethostname())
PORT= 4455
ADDR=(IP, PORT)
SIZE=1024
FORMAT= "utf-8"

def main():
    """Create a TCP Socket"""
    clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """Connect to server"""
    clientSocket.connect(ADDR)
    """Opening and reading file data"""
    file=open("yt.txt", "r")
    data=file.read()
    """Sending the filename to the server"""
    clientSocket.send("yt.txt".encode(FORMAT))
    msg=clientSocket.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]:", msg)
    """Sending file data to the server"""
    clientSocket.send(data.encode(FORMAT))
    msg=clientSocket.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]:", msg)
    """Closing the file"""
    file.close()
    """Closing the socket"""
    clientSocket.close()

if __name__=="__main__":
    main()

