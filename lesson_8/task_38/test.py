from lib import NumbersCatalog
		

catalog_fst = NumbersCatalog('catalog.txt')

not_exit = True
while not_exit:
	print('Что необходимо сделать со справоником?')
	print()
	print('1 - просмотреть справочник')
	print('2 - добавить запись')
	print('3 - Найти запись по телефону, имени и/или фамилии')
	print('4 - изменить запись')
	print('5 - удалить запись')
	print('0 - Выход')
	print()
	choice = int(input('Введите ваш выбор:'))
	print()

	if choice == 1:
		print()
		catalog_fst.output_all()
	elif choice == 2:
		surname = input('Введите фамилию:')
		name = input('Введите имя:')
		phone_number= input('Введите телефон:')

		catalog_fst.add_record(surname, name, phone_number)
	

	elif choice == 0:
		not_exit = False
	print()

