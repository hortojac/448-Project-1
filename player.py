class Player:
    def __init__(self):
        self.name = "NONE" #string for player's name
        self.my_board = [] # board to show player's full board
        self.enemy_board = [] #board to show player this player has marked on the other player's board
                              # all buttons in my_board array will be DISABLED so you can't click your own grid

         #A board will be a 100-element array that will stores the Tkinter IDs of each button
        #Ex:
        # [a1][a2][a3]....[b10]
        # [b1][b2][b3]....[b10]
        # .
        # .
        # .
        # .
        # [j1][j2][j3]....[j10]

    