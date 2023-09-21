def vowel_count(str_in):
	vowel_letters = ['ё', 'у', 'е', 'э', 'о', 'а', 'ы', 'я', 'и', 'ю']
	count = 0
	for el in str_in:
		if el in vowel_letters:
			count += 1
	return count

def all_elements_same(list_in):
	result = True
	el_fst = list_in[0]
	for i in range(1, len(list_in)):
		result = result and (list_in[i] == el_fst)
	return result