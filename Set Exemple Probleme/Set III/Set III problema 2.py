#se transmit 2 numere serverului si serverul trimite inapoi produsul acestora
import socket
# server code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5555))

buff, addr = s.recvfrom(1024)  # Adjust buffer size to handle longer messages
numbers = buff.decode().split(" ")

num1 = int(numbers[0])
num2 = int(numbers[1])
product = num1 * num2

response_message = f'{product}'

s.sendto(str.encode(response_message), addr)

# print(response_message)  -> not actually needed since the server doesn't have to print anything

# client code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = f'10 5'  # should print out absolutely
s.sendto(str.encode(msg), ("127.0.0.1", 5555))

response, address = s.recvfrom(1024)  # Adjust buffer size
print(response.decode())
