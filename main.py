import view

while True:    
    view.play_tic_tac_toe()
    repeat2 = int(input('Повторить игру?(да - 1, нет - 0):'))
    if repeat2 == 0:
        break
    