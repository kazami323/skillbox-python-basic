def encrypt_caesar(message, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encrypted_message = ''

    for symbol in message:
        if symbol in alphabet:
            symbol_index = alphabet.index(symbol)
            new_index = (symbol_index + shift) % len(alphabet)
            encrypted_message += alphabet[new_index]
        else:
            encrypted_message += symbol

    return encrypted_message


user_message = input('Введите сообщение: ').lower()
user_shift = int(input('Введите сдвиг: '))

print('Зашифрованное сообщение:', encrypt_caesar(user_message, user_shift))
