def input_int_arr(elements_number, arr_name = ''):
	arr = []
	for i in range(elements_number):
		element = int(input(f'Введите элемент {i + 1} массива {arr_name}: '))
		arr.append(element)
	return arr

def elements_in_range_indexes(arr, minimum, maximum):
	result = []
	for i in range(len(arr)):
		if arr[i] >= minimum and arr[i] <= maximum:
			result.append(i)

	return result