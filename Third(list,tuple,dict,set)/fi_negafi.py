# Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

count = int(input('Enter length of sequence: '))

n_1 = 0
n_2 = 1
my_fi = [n_1, n_2]
for i in range(2, count + 1):
    n_1, n_2 = n_2, n_1 + n_2
    my_fi.append(n_2)

m_1 = 1
m_2 = -1
my_ne = [m_1, m_2]
for i in range(2, count):
    m_1, m_2 = m_2, m_1 - m_2
    my_ne.append(m_2)

print(my_ne[::-1] + my_fi)


