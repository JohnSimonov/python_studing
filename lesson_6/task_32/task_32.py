from lib import *

minimum = int(input('Введите минимум: '))
maximum = int(input('Введите максимум: '))

print()

elements_number = int(input('Введите количество элементов массива: '))

arr = input_int_arr(elements_number)
print(elements_in_range_indexes(arr, minimum, maximum))