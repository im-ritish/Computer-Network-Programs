import socket
UDP_IP="127.0.0.1"
UDP_PORT=5005
MESSAGE=b"Hello, India!"
print("UDP TARGET IP: %s" %UDP_IP)
print("UDP TARGET PORT : %s" %UDP_PORT)
print("message is", MESSAGE)
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))