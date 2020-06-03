import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b'What time is it now?', ("localhost", 123))
date, addr = client_socket.recvfrom(512)
print(date.decode())
client_socket.close()
