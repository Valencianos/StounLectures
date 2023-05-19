# Написать функцию, которая принимает на вход строку из рандомных цифр и букв, а возвращает:
# - строку только из букв
# - строку только из цифр
# - сравнить длину строк из цифр и из букв и вернуть ту, которая длиннее
def division_into_letters_and_numbers(text: str):
    letters = numbers = ''
    for item in text:
        if item.isalpha():
            letters += item
        elif item.isdigit():
            numbers += item
    print(f'Numbers - {numbers}')
    print(f'Letters - {letters}')
    if len(numbers) > len(letters):
        print(f'The longest streak - {numbers}')
    else:
        print(f'The longest streak - {letters}')


division_into_letters_and_numbers('hjsr73254f 2445 ')



