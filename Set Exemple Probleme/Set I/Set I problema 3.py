#se transmite un text de la client la server si serverul trimite inapoi numarul de vocale din text
import socket
# server code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5555))

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

buff, addr = s.recvfrom(1024)  # Adjust buffer size to handle longer messages
text = buff.decode()
count = 0
for letter in text:
    if letter in vowels:
        count += 1

response_message = f"{count}"
s.sendto(str.encode(response_message), addr)
# print(response_message)  -> not actually needed since the server doesn't have to print anything

# client code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "This is an Example text"  # Send a text
s.sendto(str.encode(msg), ("127.0.0.1", 5555))

response, address = s.recvfrom(1024)  # Adjust buffer size
print(response.decode())