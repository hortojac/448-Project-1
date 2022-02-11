class Ship:
    def __init__(self):
        self.name = "" #name of ship, i.e. "A" or "B" or "C" etc...
        self.positions = [] #indices on board where the ship has been placed
        self.lives = 0 #changes based on name

    def set_lives(self): #set the number of lives based on the type of ship
        if self.name == "A":
            self.lives = 1
        elif self.name == "B":
            self.lives = 2
        elif self.name == "C":
            self.lives = 3
        elif self.name == "D":
            self.lives = 4
        elif self.name == "E":
            self.lives = 5
    def to_string(self): #used for debugging mainly, prints out lives of each ship
        out ="SHIP!\nname: " + self.name + "\nlives: " + str(self.lives)
        return out
