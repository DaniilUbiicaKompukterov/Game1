name = input('Введите ваше имя:')     # Пользователь вводит его имя
print('Здраствуйте,', name)           # Приветствие пользователя
x = 40      # загаданное число
cnt = 0     # число попыток

while True:
    user_num = int(input('я загадал число от 1 до 40, угадай его!'))    # предложение огтгадать число
    cnt += 1                                                            # Начальное кол-во попыток
    if user_num == x:                                                   # если пользователь ввёл правильное число
        print(name, 'Ты угадал число за', cnt, 'попыток')                 # поздравления пользователя
        print('Спасибо за игру!')                                       # благодарность
        break                                                           # Конец
    elif user_num > x:                                                  # если пользователь ввёл число меньше
        print('Наше число меньше того, которое ты ввел')
    else:                                                               # если пользователь ввёл число больше
        print('Наше число больше того, которое ты ввел')
