from lib import *

number_of_elements = int(input('Введите количество членов арифметической прогрессии: '))
start = int(input('Введите первый член арифметической прогрессии: '))
difference = int(input('Введите шаг арифметической прогрессии: '))

arr = [arithmetic_progression(i + 1, start, difference) for i in range(number_of_elements)]

print(arr)