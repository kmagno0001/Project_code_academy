# lets build a game alike tic tac toe
from Logic import Logic

game = Logic()

while game.game_running == True:
    game.drawing()

    game.input_logic(1) 
        
    if game.game_logic(1):
        break

    game.input_logic(2)
        
    if game.game_logic(2):
        break
    
    
game.print_the_winner()    
   