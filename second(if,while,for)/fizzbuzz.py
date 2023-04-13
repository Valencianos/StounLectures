# Напишите программу, которая выводит на экран числа от 1 до n. При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

num = int(input('Enter n = '))
for i in range(1, num + 1):
    if not i % 3 and not i % 5:
        print('FizzBuzz')
    elif not i % 3:
        print('Fizz')
    elif not i % 5:
        print('Buzz')
    else:
        print(i)