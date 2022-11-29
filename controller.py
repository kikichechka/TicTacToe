from random import randint
from model import tic_tac_toe
from model import man
from model import bot

def print_field(tic_tac_toe):
    print('  1   2   3')
    for i in range(len(tic_tac_toe)):
        print(i + 1, end= ' ')
        print(*tic_tac_toe[i], sep=' | ')
        print(' -----------')

def move_bot_play_tic_tac_toe(tic_tac_toe):
    for i in range(len(tic_tac_toe)):
        for j in range(0, 3):
            if '•' in tic_tac_toe[i][j]:
                tic_tac_toe[i][j] = '0'
                if check(bot) == 2:
                    print_field(tic_tac_toe)
                    return
                else: 
                    tic_tac_toe[i][j] = '•'

    for i in range(len(tic_tac_toe)):
        for j in range(0, 3):
            if '•' in tic_tac_toe[i][j]:
                tic_tac_toe[i][j] = 'x'
                if check(man) == 2:
                    tic_tac_toe[i][j] = '0'
                    print_field(tic_tac_toe)
                    return
                else: 
                    tic_tac_toe[i][j] = '•'

    while True:
        lst = [randint(0, 2) for _ in range(2)]
        if '•' in tic_tac_toe[lst[0]][lst[1]]:
            tic_tac_toe[lst[0]][lst[1]] = '0'
            print_field(tic_tac_toe)
            break

def check(player): 
    if tic_tac_toe[0].count(player) == 3: return 2
    if tic_tac_toe[1].count(player)== 3: return 2
    if tic_tac_toe[2].count(player) == 3: return 2
    if '•' not in [element for a_list in tic_tac_toe for element in a_list]: return 1
    if tic_tac_toe[0][0] == player and tic_tac_toe[1][1] == player and tic_tac_toe[2][2] == player: return 2
    if tic_tac_toe[0][2] == player and tic_tac_toe[1][1] == player and tic_tac_toe[2][0] == player: return 2
    if tic_tac_toe[0][0] == player and tic_tac_toe[1][0] == player and tic_tac_toe[2][0] == player: return 2
    if tic_tac_toe[0][1] == player and tic_tac_toe[1][1] == player and tic_tac_toe[2][1] == player: return 2
    if tic_tac_toe[0][2] == player and tic_tac_toe[1][2] == player and tic_tac_toe[2][2] == player: return 2
    return 0
