import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 5001))

print("requesting the time server for local time...")
msg = client_socket.recv(1024)
print("local time >> ", msg.decode(),"\n")

