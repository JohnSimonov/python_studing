import random

# Задаём размер грядки
n = random.randint(6, 22)
# Задаём конфигурацию грядки
a = [random.randint(20, 100) for i in range(n) ]

# Задаём массив, в котором каждый элемент sum_array[i] - собранный урожай при остановке у куста i 
# (без первого и последнего куста)
sum_array = [a[i - 1] + a[i] + a[i + 1] for i in range(1, n - 1)]

# Добавим последний куст
sum_array.append(a[n - 2] + a[n - 1] + a[0])

# Добавим первый куст
sum_array.insert(0, a[n - 1] + a[0] + a[1] )

# Поиск максимума среди собранных урожаев

maximum = -1

for el in sum_array:
	if el > maximum:
		maximum = el

print(sum_array)
print(maximum)