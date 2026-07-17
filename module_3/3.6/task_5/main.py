numbers = [1, 4, -3, 0, 10]

print('Изначальный список:', numbers)

for current_index in range(1, len(numbers)):
    current_number = numbers[current_index]
    previous_index = current_index - 1

    while previous_index >= 0 and numbers[previous_index] > current_number:
        numbers[previous_index + 1] = numbers[previous_index]
        previous_index -= 1

    numbers[previous_index + 1] = current_number

print('Отсортированный список:', numbers)
