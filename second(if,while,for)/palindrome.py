# а) на вход подается слово - проверить, является ли оно палиндромом
# Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.

# word = input('Enter a word: ')
# word = word.lower()
# if word == word[::-1]:
#     print('Its palindrome')
# else:
#     print('Its not palindrome')


# б) на вход подается фраза - проверить, является ли она палиндромом
# Не учитывается регистр, знаки препинания и пробелы.

import string
text = 'А роза, упала на лапу Азора!'
for syntax in string.punctuation:
    text = text.replace(syntax, '')
text = text.replace(' ', '').lower()
print(text == text[::-1])
