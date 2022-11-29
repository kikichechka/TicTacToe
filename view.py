import controller
import emoji
from colorama import init, Fore, Back, Style
init(convert=True)

def play_tic_tac_toe():
    init(autoreset=True)
    print(Fore.BLUE + Style.BRIGHT + '\n******* Крестики' + emoji.emojize(':cross_mark:') + ' нолики' + emoji.emojize(':hollow_red_circle: ') + '********')
    
    while True:
        move_man_play_tic_tac_toe(controller.tic_tac_toe)
        if controller.check(controller.man) == 1:
            controller.print_field(controller.tic_tac_toe)
            init(autoreset=True)
            print(Fore.RED +'Конец игры! Ничья.')
            break
        if controller.check(controller.man) == 2:
            controller.print_field(controller.tic_tac_toe) 
            init(autoreset=True)
            print(Fore.RED + 'Конец игры! Поздравляем, Вы выиграли.' + emoji.emojize(':1st_place_medal:') + emoji.emojize(':party_popper:'))
            break
        controller.move_bot_play_tic_tac_toe(controller.tic_tac_toe)
        if controller.check(controller.bot) == 1:
            init(autoreset=True)
            print(Fore.RED + 'Конец игры! Ничья.')
            break
        if controller.check(controller.bot) == 2:
            init(autoreset=True)
            print(Fore.RED +'Конец игры! К сожалению Вы проиграли' + emoji.emojize(':disappointed_face:'))
            break

def move_man_play_tic_tac_toe(tic_tac_toe):
    while True:
        x,y = map(int,input('Ваш ход. Введите координаты через пробел: ').split())       
        if 1 <= x <= 3 and 1 <= x <= 3 and '•' in tic_tac_toe[y - 1][x - 1]:
            tic_tac_toe[y - 1][x - 1] = 'x'
            break
