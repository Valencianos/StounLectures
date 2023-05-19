import math


def caesars_code(phrase: str, step: int) -> str:
    phrase = input('Please enter phrase: ')
    step = int(input('Please enter step: '))
    new_phrase = ''
    for letter in phrase:
        pos = ord(letter) + step
        new_phrase += chr(pos)
    return new_phrase

# def collatz_hypoteza(num: int) -> int:
#     num_ = int(input('Please enter number(0 or negative number to quit): '))
#     return num_
#
#     while num_ != 1:
#         if num_ % 2 == 0:
#             return num_ // 2
#             num_ = num_ // 2
#         else:
#             return num_ * 3 + 1
#             num_ = num_ * 3 + 1

def nod(n: int, m: int) -> int:
    n = int(input('Enter n number: '))
    m = int(input('Enter m number: '))
    d = min(n, m)
    while n % d != 0 or m % d != 0:
        d -= 1
    return d

def taxi(distance: int) -> float:
    BASE_RATE = 4
    ADD_RATE = 0.25
    CHARGE_DIST = 140
    result = round(BASE_RATE + math.ceil(distance / CHARGE_DIST) * ADD_RATE, 2)
    return result

def mediana() -> float:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    if a < b < c or a > b > c:
        return b
    elif b < a < c or b > a > c:
        return a
    elif a < c < b or a > c > b:
        return c

def capitalize(text: str) -> str:
    t = text
    pos = 0
    while pos < len(text) and t[pos] == ' ':
        pos += 1
    if pos < len(text):
        t = t[0 : pos] + t[pos].upper() + t[pos + 1 : len(t)]

    pos = 0
    while pos < len(text):
        if t[pos] == '.' or t[pos] == '?' or t[pos] == '!':
            pos += 1
            while pos < len(text) and t[pos] == ' ':
                pos += 1
            if pos < len(text):
                t = t[0: pos] + t[pos].upper() + t[pos + 1 : len(t)]
        pos += 1

    pos = 1
    while pos < len(text) - 1:
        if t[pos - 1] == " " and t[pos] == "i" and (t[pos + 1] == " " or t[pos + 1] == "." or t[pos + 1] == "!" or t[pos + 1] == "?" or t[pos + 1] == "'"):
            t = t[0 : pos] + "I" + t[pos + 1: len(t)]
        pos += 1
    return t

print(capitalize('where am i? why im here? when do i leave this? fuck!'))

