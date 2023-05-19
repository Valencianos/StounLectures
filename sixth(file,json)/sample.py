PATH = 'sample.txt'

with open(PATH, 'r', encoding='UTF-8') as file:
    data = file.read()


def capitalize(text: str) -> str:
    t = text
    pos = 0
    while pos < len(text) and t[pos] == ' ':
        pos += 1
    if pos < len(text):
        t = t[0 : pos] + t[pos].upper() + t[pos + 1 : len(t)]
    pos = 0

    while pos < len(text):
        if t[pos] == '.':
            pos += 1
            while pos < len(text) and t[pos] == ' ':
                pos += 1
            if pos < len(text):
                t = t[0: pos] + t[pos].upper() + t[pos + 1 : len(t)]
        pos += 1
    return t


with open(PATH, 'w', encoding='UTF-8') as file:
    file.write(capitalize(data))
