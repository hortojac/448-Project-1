class Ship:
    def __init__(self, lives):
        self.positions = [] #indices on board where the ship has been placed
        self.lives = lives #changes lives to value passed
    
    def shipToString(self):
        print("positions: " + str(self.positions))
        print("lives: " + str(self.lives))