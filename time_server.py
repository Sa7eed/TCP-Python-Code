import socket
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
current_time = str(current_time)
msg = current_time
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5001))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    print(f"connection from {client_address} has been established!")
    client_socket.send(msg.encode())
    print(f"disconnecting with {client_address}...\ndisconnected!\n")
    client_socket.close()
		
