print("""
Правила игры:
1. Играют два игрока, один играет за "X" второй за "O".
2. Игроки совершают ходы по очереди, указвая координаты в одну строчку через пробел.
Первая координата - это горизонталь, вторая - вертикаль.
3. Побеждает тот, кто соберет три символа по вертикали, горизонтали или диагонали.
ПОЕХАЛИ!!!
""")
# счетчик ходов
counter = 0

# игровое поле
playing_field = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-'],
                 ]

# вывод ирового поля до первого хода
print(f'  0 1 2\n'
      f'0 {playing_field[0][0]} {playing_field[0][1]} {playing_field[0][2]}\n'
      f'1 {playing_field[1][0]} {playing_field[1][1]} {playing_field[1][2]}\n'
      f'2 {playing_field[2][0]} {playing_field[2][1]} {playing_field[2][2]}\n')


# ировая фунция
def game(move, playing_field):
    coordinates = input(f'Ход игрока {move}. Введи координаты от 0 до 2: ')
    coordinates = coordinates.split(" ")
    try:
        coordinates = list(map(int, coordinates))
# проверка параметров хода игроков
        if playing_field[coordinates[0]][coordinates[1]] == '-':
            playing_field[coordinates[0]][coordinates[1]] = move
            print(f'  0 1 2\n'
                  f'0 {playing_field[0][0]} {playing_field[0][1]} {playing_field[0][2]}\n'
                  f'1 {playing_field[1][0]} {playing_field[1][1]} {playing_field[1][2]}\n'
                  f'2 {playing_field[2][0]} {playing_field[2][1]} {playing_field[2][2]}\n')
        else:
            print(f'Ход был уже сделан игроком играющим за {playing_field[coordinates[0]][coordinates[1]]}.'
                  f'Будь внимательнее. Сделай ход еще раз.')
            game(move, playing_field)
# перечень выигрышных комбинаций
        victory_condition = [
            playing_field[0][0] == playing_field[0][1] == playing_field[0][2] != '-',
            playing_field[1][0] == playing_field[1][1] == playing_field[1][2] != '-',
            playing_field[2][0] == playing_field[2][1] == playing_field[2][2] != '-',
            playing_field[0][0] == playing_field[1][0] == playing_field[2][0] != '-',
            playing_field[0][1] == playing_field[1][1] == playing_field[2][1] != '-',
            playing_field[0][2] == playing_field[1][2] == playing_field[2][2] != '-',
            playing_field[0][0] == playing_field[1][1] == playing_field[2][2] != '-',
            playing_field[2][0] == playing_field[1][1] == playing_field[0][2] != '-'

        ]
# проверка на наличие выигрышной комбинации
        if any(victory_condition) == True:
            print(f'Победил игрок, играющий за {move}.')
            global counter
            counter = 9
# возвращает игровое поле при отсутствии выигрышной комбинации
        else:
            return playing_field
# отлов ошибки при неверно введенных координатах
    except ValueError:
        print("Некорректные координаты, сделай ход еще раз.")
        game(move, playing_field)
# отлов ошибки при некорректно введенных индексах
    except IndexError:
        print("Некорректные координаты, сделай ход еще раз.")
        game(move, playing_field)

# цикл запуска игры
while counter < 9:
    counter += 1
    if counter == 9:
        print('У вас ничья.')
        counter = 9
# определение хода игрока
    elif counter % 2 != 0:
        game("X", playing_field)
# определение хода игрока
    elif counter % 2 == 0:
        game("O", playing_field)
# завершение игры
    else:
        print('Игра окончена.')
