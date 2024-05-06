import random
res_player = 0
res_pc = 0
while True:
    print('Ваш ход: выберете к, н или б. Если хотите завершить игру, введите 1')
    player_choice = input()
    if player_choice == '1':
        break
    if player_choice != 'к' and player_choice != 'б' and player_choice != 'н':
        print('Введите корректный входные данные')
        continue
    pc_choice = random.randint(1, 3)
    if pc_choice == 1:
        pc_choice = 'к'
    elif pc_choice == 2:
        pc_choice = 'н'
    else:
        pc_choice = 'б'
    if player_choice == 'к':
        if pc_choice == 'к':
            print('Ничья')
        elif pc_choice == 'н':
            print('Вы победили')
            res_player += 1
        else:
            print('Компьюетр победил')
            res_pc += 1
    elif player_choice == 'н':
        if pc_choice == 'к':
            print('Компьюетр победил')
            res_pc += 1
        elif pc_choice == 'н':
            print('Ничья')
        else:
            print('Вы победили')
            res_player += 1
    else: #б
        if pc_choice == 'к':
            print('Вы победили')
            res_player += 1
        elif pc_choice == 'н':
            print('Компьютер победил')
            res_pc += 1
        else:
            print('Ничья')
    print(f'Исход: ваш счёт {res_player}, счет пк: {res_pc}')