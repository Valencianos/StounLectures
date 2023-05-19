# Написать функцию для проверки числа:
#   - четность - нечетность
#   - простое число (имеет всего два делителя - само себя и единицу)
#   - сумма всех цифр числа является делителем этого числа
#   - принимает число и выдает его только простые делители

def odd_even(num: int) -> str:
    if num % 2 == 0:
        return f'{num} is even'
    else:
        return f'{num} is odd'

def simple_number(num: int) -> str:
    count = 0
    for item in range(1, num):
        if num % item == 0:
            count += 1
    if count < 2:
        return f'{num} is a simple number'
    return f'{num} is NOT a simple number'

def sum_division(num: int) -> str:
    summa = 0
    num_ = num
    while num_:
        summa += num_ % 10
        num_ //= 10
    if num % summa == 0:
        return f'Sum of {num} is a division for this number'
    return f'Sum of {num} is NOT a division for this number'

def simple_divisor(num: int) -> str:
    num_ = num
    divisors = (2, 3, 5, 7)
    result = []
    while num_ % divisors[0] == 0:
        num_ //= divisors[0]
        result.append(divisors[0])
    while num_ % divisors[1] == 0:
        num_ //= divisors[1]
        result.append(divisors[1])
    while num_ % divisors[2] == 0:
        num_ //= divisors[2]
        result.append(divisors[2])
    while num_ % divisors[3] == 0:
        num_ //= divisors[3]
        result.append(divisors[3])
    if num_ > 1:
        result.append(num_)
    return f'Divisors for number {num} is: {result}'

number = int(input('Enter number: '))
print(odd_even(number))
print(simple_number(number))
print(sum_division(number))
print(simple_divisor(number))