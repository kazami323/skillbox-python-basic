text = input('Введите текст: ')
vowels = 'ауоыиэяюёе'
vowels_in_text = [letter for letter in text.lower() if letter in vowels]

print('Список гласных букв:', vowels_in_text)
print('Длина списка:', len(vowels_in_text))
