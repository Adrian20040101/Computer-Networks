#se transmit cuvinte serverului si serverul trimite inapoicuvantul cu cele mai multe consoane
import socket
# server code

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5555))

buff, addr = s.recvfrom(1024)  # Adjust buffer size to handle longer messages
words = buff.decode().split(" ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

max_vowels = -1
max_word = ""

for word in words:
    vowel_count = 0
    for character in word:
        if character not in vowels and character.isalpha():
            vowel_count += 1
    if vowel_count > max_vowels:
        max_vowels = vowel_count
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
