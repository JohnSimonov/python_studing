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

	elif choice == 3:
		print()
		print('Введите 1 для поиска по номеру телефона.')
		print('Введите 2 для поиска по фамилии и/или имени')
		sub_choice = int(input('Введите ваш выбор:'))

		if sub_choice == 1:
			phone_number = input('Введите номер телефона:')
			result = catalog_fst.search_by_phone_number(phone_number)
			print()
			print("Записи с таким номером нет" if len(result) == 0 else result[0])
		elif sub_choice == 2:
			name = input('Введите имя (Нажмите Enter если нет данных):')
			surname = input('Введите фамилию (Нажмите Enter если нет данных):')
			result = catalog_fst.search_by_name_and_or_surname(name, surname)
			print()
			print("Записи с такими данными нет" if len(result) == 0 else result[0])
	elif choice == 4:
		print()
		old_surname = input('Введите старую фамилию записи:')
		old_name = input('Введите старое имя записи:')
		old_phone_number = input('Введите старый номер телефона записи:')
		print()

		new_surname = input('Введите новую фамилию записи:')
		new_name = input('Введите новое имя записи:')
		new_phone_number = input('Введите новый номер телефона записи:')

		catalog_fst.change_record(old_surname, old_name, old_phone_number, new_surname, new_name, new_phone_number )
	elif choice == 5:
		print()
		surname = input('Введите  фамилию удаляемой записи:')
		name = input('Введите  имя удаляемой записи:')
		phone_number = input('Введите  номер телефона удаляемой записи:')
		catalog_fst.del_record(surname, name, phone_number)

	elif choice == 0:
		not_exit = False
	print()

