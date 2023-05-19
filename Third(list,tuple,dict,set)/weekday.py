# Вводим сегодняшнюю дату и сегодняшний день недели,
# затем вводим новую дату и программа должна выдать нам какой день недели будет в эту дату

from datetime import date
import calendar
WEEK_DAY = ['Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday', 'Monday', 'Tuesday']
MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year: int) -> int:
    return (year - 1968)//4
day, month, year = input('Enter date: ').split('.')
days = int(day) + sum(MONTHS[:int(month) - 1]) + (int(year) - 1970)*365 + leap_year(int(year))

print(WEEK_DAY[days % 7])
