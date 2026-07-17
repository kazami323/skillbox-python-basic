list_length = int(input('Введите длину списка: '))
numbers = [1 if number_index % 2 == 0 else number_index % 5
           for number_index in range(list_length)]

print('Результат:', numbers)
