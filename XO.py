print(f'{50 * '*'} Игра Крестики-Нолики {50 * '*'}')
pole = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]  # Игровое поле

count = 0  # Счетчик ходов
endgame = 0  # Переменная для остановки цикла. Почему то с Break Никак не получалось реализовать.


# Для проверяещего: Код и анотации мои, за исключением "Проверки на победу" Что то в голову совсем не шло.
# Хотел изначально сравнением списков,но потом понял что слишком много вариаций придется перебирать. Поэтому подглядел.

def find_number(num: int, player: str) -> bool:
    '''Находит индекст в матрице входящего числа.
    Если нашел то меняет его на Крестик или Нолик'''
    for i, j in enumerate(pole):
        for k, v in enumerate(j):
            if v == num:
                pole[i][k] = player
                return True
    return False


def check_winner(player: str) -> bool:
    '''Проверка на победу'''
    for i in pole:
        if i.count(player) == 3:
            return True
    for i in range(3):
        if pole[0][i] == pole[1][i] == pole[2][i]:
            return True
    if pole[0][0] == pole[1][1] == pole[2][2] or pole[0][2] == pole[1][1] == pole[2][0]:
        return True

    return False


def print_pole():
    'Функция для того что бы напечатать поле'
    print(f'Игровое поле:')
    for i in pole:
        print(i)


def two_player():
    '''Функция что игрок выбрал ячейку куда поставит O. Делается проверка для числа: Входит ли оно в матрицу.
     Не отсутствует ли в матрице. Являеетcя ли числом. Добавляет к счетчику ходов +1.
     Проверяет на Выйгрыш или Ничью. Если нет то передает ход к первому игроку'''
    global count
    global endgame
    while endgame == 0:
        player = 'O'
        while True:
            print(f'Ход второго игрока!')
            user_number = input('Введи номер ячейки 1-9: ')
            try:
                number = int(user_number)
                if 0 < number < 10:
                    if find_number(number, player):
                        break
                    else:
                        print(f'Данная ячейка занята! Пожалуйста выбери другую.')
                else:
                    print('Ячейка должна быть в пределах от 1 до 9!')
            except ValueError:
                print('Вы ввели не число! Введите пожалуйста целое число!')
        count += 1
        print_pole()
        if check_winner(player):
            print('YOU WIN!!! Победил второй игрок! Нолики никогда не проигрывают!')
            new_game(1)
            endgame += 1
        if count == 9:
            print('Ничья!')
            new_game(1)
            endgame += 1
        start_game()


def start_game():
    '''Функция что игрок выбрал ячейку куда поставит X. Делается проверка для числа: Входит ли оно в матрицу.
     Не отсутствует ли в матрице. Являеетcя ли числом. Добавляет к счетчику ходов +1. Проверяет на Выйгрыш или Ничью.
    Если нет то передает ход ко второму игроку'''
    global count
    global endgame
    print_pole()
    while endgame == 0:
        player = 'X'
        while True:
            print(f'Ход первого игрока!')
            user_number = input('Введи номер ячейки 1-9: ')
            try:
                number = int(user_number)
                if 0 < number < 10:
                    if find_number(number, player):
                        break
                    else:
                        print(f'Данная ячейка занята! Пожалуйста выбери другую.')
                else:
                    print('Ячейка должна быть в пределах от 1 до 9!')
            except ValueError:
                print('Вы ввели не число! Введите пожалуйста целое число!')
        count += 1
        print_pole()
        if check_winner(player):
            print('YOU WIN!!! Победил первый игрок! Крестики сильнее всех!')
            new_game(1)
            endgame += 1
        if count == 9:
            print('Ничья!')
            new_game(1)
            endgame += 1
        two_player()


def new_game(zanogo: int = 0):
    '''Функция для начала игры. По умолчанию принимает параметр 0. Если приходит параметр 1 - значит рестарт игры.
    Обнуляет Поле счетчик ходов и переменную Endgame'''
    global endgame
    global pole
    global count
    if zanogo == 0:
        start_game()
    else:
        ng = input(f'Начнем новую игру? [да|нет]')
        if ng.lower() == 'да':
            endgame = 0
            count = 0
            pole = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            start_game()
        elif ng.lower() == 'triniti':
            print('The Matrix has you..123..')
            new_game(1)
        else:
            print('Спасибо за игру!')


new_game()
