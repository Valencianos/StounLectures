# 1. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное. (float)
# num = input('Enter number: ')
# sum_ = 0
# for item in num:
#     if item.isdigit():
#         sum_ += int(item)
# print(sum_)

# 2. На вход поступает вещественное число, найти первую цифру дробной части.
# num = input(' Enter number: ')
# num1 = num.index('.')
# print(num[num1+1])

# 3. На вход поступает десятичное число, вывести его в виде двоичного
num = int(input(' Enter number: '))
my_res = ''
while num:
    my_res = str(num % 2) + my_res
    num //= 2
print(my_res)