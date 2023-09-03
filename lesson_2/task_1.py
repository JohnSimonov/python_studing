coins_number = int(input('Введите число монет на столе: '))

print()
print('Введите ориентацию всех монет в виде цифр. Цифра 1 - орёл, 0 - решка')
print()
counter = 0 
up = 0 
down = 0

while counter < coins_number:
	orientation = int(input(f'ориентация монеты {counter + 1}: ' ))
	
	if orientation == 1:
		up += 1
	else:
		down += 1

	counter += 1

min_changes = up if up < down else down
print()
print(f'Минимальное количество переворотов: {min_changes}')