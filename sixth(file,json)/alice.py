import string
PATH = 'Alice in Wonderland.txt'

with open(PATH, 'r', encoding='UTF-8') as file:
    data = file.read()
data = data.rstrip()
for item in data:
    if item not in string.punctuation:
        data += item

vocal = []
data = data.split(' ')
for word in data:
    if len(word) > 4:
        vocal.append(word)
print(vocal)
set_alice = set(vocal)
print(set_alice)



