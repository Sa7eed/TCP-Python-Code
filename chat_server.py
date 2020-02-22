import socket, sys
name = "Sayeed"
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 12345
soc.bind((host_name, port))
soc.listen(1) #Try to locate using socket
client_socket, client_addr = soc.accept()
print("connection established!")
#get a connection from client side
client_name = client_socket.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
client_socket.send(name.encode())
while True:
   message = input('Me > ')
   if message == '[bye]':
      message = 'disconnecting...'
      client_socket.send(message.encode())
      print("\ndisconnected!")
      soc.close()
      break
   client_socket.send(message.encode())
   message = client_socket.recv(1024)
   message = message.decode()
   print(client_name, '>', message)
