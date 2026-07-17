text = input('Введите строку: ')
first_h_index = text.index('h')
last_h_index = text.rindex('h')
reversed_part = text[last_h_index - 1:first_h_index:-1]

print('Развёрнутая последовательность между первым и последним h:',
      reversed_part)
