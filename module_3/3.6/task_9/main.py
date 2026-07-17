skates_count = int(input('Количество роликов: '))
skates_sizes = []
for pair_number in range(1, skates_count + 1):
    size = int(input(f'Размер пары {pair_number}: '))
    skates_sizes.append(size)

people_count = int(input('\nКоличество людей: '))
people_sizes = []
for person_number in range(1, people_count + 1):
    size = int(input(f'Размер ноги человека {person_number}: '))
    people_sizes.append(size)

people_with_skates = 0
for foot_size in people_sizes:
    if foot_size in skates_sizes:
        people_with_skates += 1
        skates_sizes.remove(foot_size)

print('\nНаибольшее количество людей, которые могут взять ролики:',
      people_with_skates)
