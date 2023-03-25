
width = 3
hight = 3    
parallel = 5

x_ = ["x    x", " x  x ", "  xx  ", " x  x ", "x    x"]
o_ = [" oooo ", "o    o", "o    o", "o    o", " oooo "]
empty_space = ["******", "*    *", "*    *","*    *", "******"]

class Logic:
    board = [[0 for i in range(hight) ] for j in range(width)]

    winner = 0

    def __init__(self) -> None:
        self.game_running = True

    def drawing(self) -> None:
        for row in range(hight):
            for par in range(parallel):
                for col in range(width):
                    if self.board[row][col] == 0:
                        print(empty_space[par], end=' ')
                    if self.board[row][col] == 1:
                        print(x_[par], end=' ')
                    if self.board[row][col] == 2:
                        print(o_[par], end=' ')        
                print()
            print()    

    def game_logic(self, player:int) -> None:
       
        def checking_winner(player):
            count = 0
            possible_plays = [[[0,0], [0,1], [0,2]], [[1,0], [1,1], [1,2]], [[2,0], [2,1], [2,2]], [[0,0], [1,0], [2,0]], [[0,1], [1,1], [2,1]], [[0,2], [1,2], [2,2]], [[0,0], [1,1], [2,2]], [[0,2], [1,1], [2,0]]]
            
            for play in possible_plays:
                for plays in play:
                    if self.board[plays[0]][plays[1]] == player:
                        count += 1
                if count == 3:
                    break;
                else:
                    count = 0

            return count 
        
        if checking_winner(player) == 3:
           self.game_running = False 
           self.winner = player 
           return True        
                    

    def input_logic(self, player) -> bool:
        position = int(input(f"Player {'X' if player == 1 else 'O'} , Enter your Position ? "))

        pos_x = 0 
        pos_y = 0

        if position == 10:
            self.game_running = False
            return True
        elif position in [1,2,3]:
            pos_x = 0
            pos_y = position - 1

        elif position in [4,5,6]:
            pos_x = 1
            pos_y = position - 4

        elif position in [7,8,9]:
            pos_x = 2
            pos_y = position - 7

        if self.board[pos_x][pos_y] == 0:
            self.board[pos_x][pos_y] = player
            return False
    def print_the_winner(self)-> None:

        print(f"Winner of the game was {'X' if self.winner == 1 else 'O' } Player")    
        
       
  

    
            