import socket 

IP=socket.gethostbyname(socket.gethostname())
PORT= 4455
ADDR=(IP, PORT)
SIZE=1024
FORMAT= "utf-8"

def main():
    print("[Starting] Server is starting.")
    serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(ADDR)
    serverSocket.listen()
    print("[Listening] Server is listening.")
    while(True):
        """Accept"""
        conn, addr= serverSocket.accept()
        print(f"[New Connection]", addr, "connected")
        """File name and handling"""
        filename=conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Received the filename.")
        file=open(filename, "w")
        """Acknowledge file name received"""
        conn.send("Filename receieved.".encode(FORMAT))
        """File data"""
        data=conn.recv(SIZE).decode(FORMAT)
        print(f"[Received] Receiving the file data")
        file.write(data)
        """Acknowledge file data received"""
        conn.send("File data received".encode(FORMAT))
        """Close file and connection"""
        file.close()
        conn.close()
        print(f"[Disconnected]", addr, "disconnected")

if __name__== "__main__":
    main()


