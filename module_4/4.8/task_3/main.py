import random


first_team = [round(random.uniform(5, 10), 2)
              for participant_index in range(20)]
second_team = [round(random.uniform(5, 10), 2)
               for participant_index in range(20)]
winners = [max(first_team[participant_index], second_team[participant_index])
           for participant_index in range(20)]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winners)
