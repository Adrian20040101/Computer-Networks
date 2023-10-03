#se transmite o litera de la client la server, serverul trimite inapoi litera dublata
import socket
# server code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5555))
buff,addr = s.recvfrom(10)
letter = buff.decode()
response = letter * 2
s.sendto(response.encode(), addr)
# print(response)  -> not actually needed since the server doesn't have to print anything

# client code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "h"  # Send a single letter
s.sendto(str.encode(msg), ("127.0.0.1", 5555))

response, address = s.recvfrom(10)
print(response.decode())