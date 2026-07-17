people_count = int(input('Количество человек: '))
step = int(input('Какое число в считалке? '))
people = list(range(1, people_count + 1))
current_index = 0

print(f'Значит, выбывает каждый {step}-й человек')

while len(people) > 1:
    print('\nТекущий круг людей:', people)
    print('Начало счёта с номера', people[current_index])
    current_index = (current_index + step - 1) % len(people)
    removed_person = people.pop(current_index)
    print('Выбывает человек под номером', removed_person)
    current_index %= len(people)

print('\nОстался человек под номером', people[0])
