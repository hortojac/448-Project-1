class Player:
    def __init__(self):
        self.name = "NONE" #string for player's name
        self.my_board = [] # board to show player's full board
        self.enemy_board = [] #board to show player this player has marked on the other player's board
                              # all buttons in my_board array will be DISABLED so you can't click your own grid

        #Our 10x10 board will be represented by a 100-element array that will store 100 Buttons, one for each grid space 
        #Ex:
        # [a1][a2][a3]....[b10]
        # [b1][b2][b3]....[b10]
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # [j1][j2][j3]....[j10]
        self.ship_lives = {} #blank dicttionary (hashmap) of number of lives left of each ship belonging this player

        '''Example of a ship_lives dictionary at the start of a 5 ship game
        player1.ship_lives = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
        }
        '''

    
