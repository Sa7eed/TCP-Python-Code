import socket, sys
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
port = 12345
print('trying to connect to the user...\n')
soc.connect((socket.gethostname(), port))
print(f"connected to {shost}...\n")
name = input('enter your name: ')
print('\n')
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('Enter [bye] to exit.')
while True:
   message = soc.recv(1024)
   message = message.decode()
   print(server_name, ">", message)
   message = input(str("Me > "))
   if message == "[bye]":
      message = "Left the Chat room"
      soc.send(message.encode())
      print("\ndisconnecting...\ndisconnected")
      soc.close()
      break
   soc.send(message.encode())
