from lib import *
text = input('Enter text: ')

phrases = text.split(' ')

vowels_in_every_phase = list(map(vowel_count, phrases))

same = all_elements_same(vowels_in_every_phase)
print("Парам пам-пам" if same else "Пам парам")