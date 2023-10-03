#se transmit cuvinte serverului si serverul trimite inapoi numarul de cuvinte primit
import socket
# server code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5555))

buff, addr = s.recvfrom(1024)  # Adjust buffer size to handle longer messages
words = buff.decode().split(" ")

response_message = f"{words.__len__()}"
s.sendto(str.encode(response_message), addr)
# print(response_message)  -> not actually needed since the server doesn't have to print anything

# client code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "TWO WORDS"
s.sendto(str.encode(msg), ("127.0.0.1", 5555))

response, address = s.recvfrom(1024)  # Adjust buffer size
print(response.decode())
