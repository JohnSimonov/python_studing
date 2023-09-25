import shutil

class NumbersCatalog:
	def __init__(self, path):
		self.path = path
		file = open(path, 'a')
		file.close()

	def output_all(self):
		with open(self.path, 'r') as file:
			for line in file:
				print(line)

	def add_record(self, surname, name, phone_number):
		with open(self.path, 'r+') as file:
			not_inside = True
			new_record = f'{surname} {name} {phone_number}\n'
			for record in file:
				if record == new_record:
					not_inside = False
			if not_inside :
				file.write(new_record)

	def del_record(self, surname, name, phone_number):
		with open(self.path, 'r') as old_file:
			del_record = f'{surname} {name} {phone_number}\n'
			new_file = open('temp.txt', 'w')
			for record in old_file:
				if record != del_record:
					new_file.write(record)
			new_file.close()
			shutil.copy('temp.txt', self.path)

	def change_record(self, old_surname, old_name, old_phone_number, new_surname, new_name, new_phone_number ):
		with open(self.path, 'r') as old_file:
			del_record = f'{old_surname} {old_name} {old_phone_number}\n'
			new_record = f'{new_surname} {new_name} {new_phone_number}\n'
			new_file = open('temp.txt', 'w')
			for record in old_file:
				if record != del_record:
					new_file.write(record)
				else:
					new_file.write(new_record)

			new_file.close()
			shutil.copy('temp.txt', self.path)


	def search_by_phone_number(self, phone_number ):	
		if phone_number != '':
			with open(self.path, 'r') as file:
				found_records = []
				for record in file:
						record_splitted = record.split()
						if phone_number == record_splitted[2]:
						 found_records.append(record)
				return found_records
		else:
			return []

	def search_by_name_and_or_surname(self, name = None, surname = None):
		name = None if name == '' else name 
		surname = None if surname == '' else surname
		found_records = []
		if name and surname:
			with open(self.path, 'r') as file:
				for record in file:
					record_splitted = record.split()
					if record_splitted[1] == name and record_splitted[0] == surname:
						found_records.append(record)
		elif surname or name:
			with open(self.path, 'r') as file:
				for record in file:
					record_splitted = record.split()
					condition_fst = surname and record_splitted[0] == surname
					condition_snd = name and record_splitted[1] == name
					if  condition_fst or condition_snd :
						found_records.append(record)
		return found_records

