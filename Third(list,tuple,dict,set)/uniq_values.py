# Дан список чисел. Создать новый список, который будет содержать только уникальные элементы исходного списка

import random
size = int(input('Enter list length: '))
my_list = [random.randint(0,10) for _ in range(size)]
print(my_list)

my_list = set(my_list)
print(my_list)