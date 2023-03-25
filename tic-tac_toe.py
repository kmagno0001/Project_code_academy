# lets build a game alike tic tac toe
from Logic import Logic
import os

game = Logic()

while game.game_running == True:
    os.system('cls')    
    
    game.drawing()

    if game.input_logic(1) == True:
        break
    if game.game_logic(1):
        break

    if game.input_logic(2) == True:
        break
    if game.game_logic(2):
        break

game.drawing()    
game.print_the_winner()    
   