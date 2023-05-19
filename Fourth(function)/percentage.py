# Функция принимает предложение, вычисляет какой буквы в этом предложении больше и
# возвращает эту букву и процент ее вхождения предложение

text = 'And I was walking down the street and the sun is shining to MY FACE!'
text = text.lower()
text_ = ''
for letter in text:
    if letter.isalpha():
        text_ += letter

uniq = set(text_)
my_dict = {}
for uniq in text_:
    my_dict[uniq] = text_.count(uniq)

summ = 0
for value in my_dict.values():
    summ += value

max_ = 0
for value in my_dict.values():
    if value > max_:
        max_ = value

kiz = ''
for key, value in my_dict.items():
    if max_ in value:
        kiz = my_dict(key)
print(kiz)
