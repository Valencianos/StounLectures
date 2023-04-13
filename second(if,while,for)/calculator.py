# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций (сложение, вычитание, умножение или деление):
# вводим первое число, потом операцию и второе число - выводится результат
# Программа должна завершаться только по желанию пользователя: можно ввести enter и программа закончится, или еще операцию и еще число.
# Ну и помним, что на ноль делить нельзя.

from decimal import Decimal
a = Decimal(input('Enter 1st number: '))
b = input('Enter operation: ')
c = Decimal(input('Enter 2nd number: '))
if c:
    match b:
        case '+':
            print(f'{a + c}')
        case '-':
            print(f'{a - c}')
        case '*':
            print(f'{a * c}')
        case '/':
            print(f'{a / c}')
else:
    print('You cant divide by zero')