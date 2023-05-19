# Мы уже делали переводчик числа из десятичной в двоичную в двоичную, самое время сделать для восьмиричной
# и шестнадцатиричной. а лучше сделать универсальный (двоичная, восьмиричная, шеснадцатиричная)
# и подумать как интереснее оформить "меню" выбора в какую систему переводим:)

num = int(input('Enter number: '))
system = int(input('Enter system for transfer (2, 8 or 16): '))

my_string = ''
my_list = '0123456789ABCDEF'

while num:
    my_string = my_list[num % system] + my_string
    num //= system
print(my_string)