numbers = [1, 2, 3, 4, 5]
shift = int(input('Сдвиг: '))

print('Изначальный список:', numbers)

shift %= len(numbers)
if shift:
    numbers = numbers[-shift:] + numbers[:-shift]

print('Сдвинутый список:', numbers)
