sum = int(input('Введите сумму двух чисел: '))
multiplication = int(input('Введите произведение двух чисел: '))

flag = True 
first_number = 1 
second_number = 1

while flag and first_number <= 1000:
	while flag and second_number <= 1000:
		condition_fst = (first_number + second_number) == sum
		condition_snd = (first_number * second_number) == multiplication

		if condition_fst and condition_snd:
			print(f'Загаданные числа : {first_number}, {second_number}')
			flag = False
		second_number += 1
	    

	first_number += 1
	second_number = 1

