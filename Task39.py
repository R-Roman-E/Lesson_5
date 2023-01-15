# Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество 
# конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, 
# соответственно внедрить этот алгоритм боту )


def correct_value(value, players, turn):
    result = input(f'{players[turn]}, твоя очередь брать конфеты: ')
    while not result.isdigit or not (29 > int(result) > 0) or int(result) > value:
        if value >= 28:
            result = input(f'{players[turn]}, можно вводить значения только от 1 до 28: ')
        else:
            result = input(f'{players[turn]}, можно вводить значения только от 1 до {value}: ')
    return int(result)


def player_init():
    player1 = input('\nВведите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    return player1, player2


def players_draw(player1, player2):
    from random import randint 
    draw = randint(1, 2)
    if draw == 1:
        print(f'\nПо результатам жеребьевки первым ходит {player1}!')
        return {1: player1, 2: player2}
    else:
        print(f'\nПо результатам жеребьевки первым ходит {player2}!')
        return {1: player2, 2: player1}


def game_candies(value, players):
    turn = 1
    while value > 0:
        if turn == 1:
            move = correct_value(value, players, turn)
            value -= move
            if value == 0:
                print(f'\n{players[turn]} ПОБЕДИЛ!!!')
                break
            print(f'\nОсталось конфет: {value}\n')
            turn = 2
        if turn == 2:
            move = correct_value(value, players, turn)
            value -= move
            if value == 0:
                print(f'\n{players[turn]} ПОБЕДИЛ!!!')
                break
            print(f'\nОсталось конфет: {value}\n')
            turn = 1


count_candies = 221
print('___ИГРА В КОНФЕТЫ___')
print('Брать со стола можно от 1 до 28 конфет за раз')
print('Кто последний делает ход - тот победил!')
player_1, player_2 = player_init()
players = players_draw(player_1, player_2)
print(f'\nКолличество конфет на столе: {count_candies}\n')
game_candies(count_candies, players)