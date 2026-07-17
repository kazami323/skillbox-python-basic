numbers_count = int(input('Количество чисел: '))
sequence = []

for _ in range(numbers_count):
    sequence.append(int(input('Число: ')))

print('Последовательность:', sequence)

numbers_to_add = []
for start_index in range(len(sequence)):
    remaining_sequence = sequence[start_index:]
    if remaining_sequence == remaining_sequence[::-1]:
        numbers_to_add = sequence[:start_index][::-1]
        break

print('Нужно приписать чисел:', len(numbers_to_add))
print('Сами числа:', numbers_to_add)
