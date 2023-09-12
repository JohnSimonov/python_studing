n = int(input("Введите количество элементов в первом наборе: "))
m = int(input("Введите количество элементов во втором наборе: "))

print()

set_fst = set()

for i in range(n):
	element = int(input(f"Введите элемент {i + 1} набора 1: "))
	set_fst.add(element)

print()

set_snd = set()

for i in range(m):
	element = int(input(f"Введите элемент {i + 1} набора 2: "))
	set_snd.add(element)

list_both = list(set_fst.intersection(set_snd))
list_both_size = len(list_both)

no_replace = False 

while not no_replace:
	no_replace = True
	for i in range( list_both_size - 1): 
		if list_both[i] > list_both[i + 1]:
			temp = list_both[i]
			list_both[i] = list_both[i + 1]
			list_both[i + 1] = temp
			no_replace = False

print(list_both)
