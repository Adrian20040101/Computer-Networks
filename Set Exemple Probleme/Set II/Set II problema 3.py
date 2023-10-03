#se transmit cuvinte serverului si serverul trimite inapoicuvantul cu cele mai multe caractere
import socket
# server code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5555))

buff, addr = s.recvfrom(1024)  # Adjust buffer size to handle longer messages
words = buff.decode().split(" ")

max_characters = -1
max_word = ""
for word in words:
    count = word.__len__()
    if count > max_characters:
        max_characters = count
        max_word = word

response_message = f'{max_word}'

s.sendto(str.encode(response_message), addr)

# print(response_message)  -> not actually needed since the server doesn't have to print anything

# client code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "This is an example that is absolutely amazing"  # should print out absolutely
s.sendto(str.encode(msg), ("127.0.0.1", 5555))

response, address = s.recvfrom(1024)  # Adjust buffer size
print(response.decode())
