text = input('Enter text: ')
new_text = []
displ = 3
alphabet = 'ABCDEFGHIJKLMNOPRSTQUVWXYZ'
for letter in text.upper():
    for item in alphabet:
        if letter == item:
            new_text.append(item[displ])

print(new_text)


