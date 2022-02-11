from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial
from itertools import product
from player import Player
from ship import Ship
from PIL import ImageTk, Image

def show_frame(frame):
    frame.tkraise()

### Global Variables
num_ships = 0
player1 = Player() #initialize player1
player2 = Player() #initialize player2

P1_ENEMY_CREATED = False
P2_ENEMY_CREATED = False
###

### Global Variables
num_ships = 0 #the amount of ships each player will have (chosen by the user)
text_variable = 'A' #the letter an empty button will change to when clicked by the user when they are placing their ships (either A B C D or E)
selected_ships=0 #once the player has placed all of their ships they will not be allowed to keep placing more letters
enter_amount=0 #the amount of times the user will click the board when placing their ships
placing_ships=0 #keeps track of what letter should appear next when the user is placing their ships
current_index=0 #stores the original index of where the first B, C, D, or E was placed
vertical_up = False #boolean to check if the users second move was above the original index
vertical_down = False #boolean to check if the users second move was below the original index
horizontal_right = False #boolean to check if the users second move was to the right the original index
horizontal_left = False #boolean to check if the users second move was to the left the original index
left_left = False #boolean to check if there are 2 letters to the left of the original index
left_right = False #boolean to check if there is 1 letter to the left of the original index and 1 letter to the right
right_right = False #boolean to check if there are 2 letters to the right of the original index
right_left = False #boolean to check if there is 1 letter to the left of the original index and 1 letter to the right 
up_up = False #boolean to check if there are 2 letters above the original index
up_down = False #boolean to check if there is 1 letter above the original index and 1 letter below
down_down = False #boolean to check if there are 2 letters below the original index
down_up = False #boolean to check if there is 1 letter above the original index and 1 letter below
lll = False #boolean to check if there are 3 letters to the left of the original index
llr = False #boolean to check if there are 2 letters to the left and 1 letter to the right
rrr = False #boolean to check if there are 3 letters to the right of the original index
rrl = False #boolean to check if there are 2 leters to the right and 1 letter to the left of the original index
uuu = False #boolean to check if there are 3 letters above the original index
uud = False #boolean to check if there are 2 letters above and 1 letter below the original index
ddu = False #boolean to check if there are 2 letters below and 1 leter above the original index
ddd = False #boolean to check if there are 3 letters below the original index
p1_fired = False
p2_fired = False

p1_hit_counter = 0
p2_hit_counter = 0
###

root = Tk()
root.state('zoomed')
root.title("Battleship")

### Images Used
image=Image.open("assets/sunk.jpeg")
img_s=image.resize((40,40))
img_sunk=ImageTk.PhotoImage(img_s)

image=Image.open("assets/hit.jpeg") #image for hit (bg for button will be set to red)
img_r=image.resize((40,40))
img_hit=ImageTk.PhotoImage(img_r)

image=Image.open("assets/miss.jpeg")
img_w=image.resize((40,40))
img_miss=ImageTk.PhotoImage(img_w)
###

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)
frame7 = Frame(root)
frame8 = Frame(root)
frame9 = Frame(root)
frame10 = Frame(root)
for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10):
    frame.grid(row=0, column=0, sticky = 'nsew')

show_frame(frame1)
#Frame code below functions


def set_player_names(): #sets player names, then makes a label with the corresponding player name for frames 4 and 5 respectively
    global player1
    global player2
    print(e.get())
    print(b.get())
    player1.name = e.get()
    player2.name = b.get()
    show_frame(frame4)

    #set up frame 4 label
    p1_label = "Player 1 (" + player1.name + ")"
    frame4_label = Label(frame4, text=p1_label).grid(row=2, column=22)

    #set up frame 5 label
    p2_label = "Player 2 (" + player2.name + ")"
    frame4_label = Label(frame5, text=p2_label).grid(row=2, column=22) 

def shipcount(x):
    global num_ships
    global player1
    global player2
    num_ships = x
    num = str(x) # get the number as a string
    mylabel = Label(frame4, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p1 on frame4
    mylabel = Label(frame5, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p2 on frame5
    choose_ship_number()
    #instantiate players' ships
    if(num_ships==1): 
        player1.ships = {
            "A": Ship(1)
        }
        player2.ships = {
            "A": Ship(1)
        }
    elif(num_ships==2):
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2)
        }
    elif(num_ships==3):
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3)
        }
    elif(num_ships==4):
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4)
        }
    else: 
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4),
            "E": Ship(5)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4),
            "E": Ship(5)
        }
    show_frame(frame4)

def choose_ship_number():
    global num_ships
    x = num_ships
    if x >= 1: 
        ship1 = Button(frame4, text="A", padx=20, pady=10, fg='red').grid(row = 3, column = 22)
        ship1 = Button(frame5, text="A", padx=20, pady=10, fg='red').grid(row = 3, column = 22)
        if x >= 2:
            ship2 = Button(frame4, text="BB", padx=40, pady=10, fg='blue').grid(row = 4, column = 22)
            ship2 = Button(frame5, text="BB", padx=40, pady=10, fg='blue').grid(row = 4, column = 22)
            if x >= 3:
                ship3 = Button(frame4, text="CCC", padx=60, pady=10, fg='orange').grid(row = 5, column = 22)
                ship3 = Button(frame5, text="CCC", padx=60, pady=10, fg='orange').grid(row = 5, column = 22)
                if x >= 4:
                    ship4 = Button(frame4, text="DDDD", padx=80, pady=10, fg='green').grid(row = 6, column = 22)
                    ship4 = Button(frame5, text="DDDD", padx=80, pady=10, fg='green').grid(row = 6, column = 22)
                    if x >= 5:
                        ship5 = Button(frame4, text="EEEEE", padx=100, pady=10, fg='purple').grid(row = 7, column = 22)
                        ship5 = Button(frame5, text="EEEEE", padx=100, pady=10, fg='purple').grid(row = 7, column = 22)

def int_to_char(x): #converts given integer into to a character
    return chr(x+64)

def char_to_int(x): #converts given character into an integer
    return int(x) - 64

def ValidMove_2(i): #is the second letter being placed on a valid button in relation to the original index?
    global current_index
    global vertical_up 
    global vertical_down
    global horizontal_right
    global horizontal_left
    if(i==current_index+1) and (i%10!=0): #if the second move is to the right of the original index and it is not wrapping around the sides of the board...
        horizontal_right = True #the players second move was to the right
        return(True)#this is a valid move
    if(i==current_index-1) and (i%10!=9): #if the second move is to the left of the original index and it is not wrapping around the sides of the board...
        horizontal_left = True #the players second move was to the left
        return(True)#this is a valid move
    if(i==current_index+10): #if the second move is below the original index...
        vertical_down = True #the players second move was down
        return(True)#this is a valid move
    if(i==current_index-10): #if the second move is above the original index...
        vertical_up = True #the players second move was up
        return(True)#this is a valid move
    else:
        return(False)#this is not a valid move

def ValidMove_3(i): #is the third letter being placed on a valid button in relation to the original index and the second letter?
    global current_index
    global vertical_up 
    global vertical_down
    global horizontal_right
    global horizontal_left
    global left_left
    global left_right
    global right_right
    global right_left
    global up_up
    global up_down
    global down_down
    global down_up
    if(horizontal_left): #if the players second move was to the left of the original index...
        if(i==current_index+1) and (i%10!=0): #if the third move is to the right of the original index and it is not wrapping around the sides of the board...
            left_right = True #the players third move is to the right of the original index 
            return(True) #this is a valid move
        if(i==current_index-2) and (i%10!=9): #if the third move is 2 to the left of the original index and it is not wrapping around the side of the board (or to the left of the second move)...
            left_left = True #the players third move is to the left of the second move
            return(True) #this is a valid move
    elif(horizontal_right): #if the players second move was to the right of the original index...
        if(i==current_index-1) and (i%10!=9):#if the third move is to the left of the original index and it is not wrapping around the sides of the board...
            right_left = True #the players third move is to the left of the original index
            return(True)#this is a valid move
        if(i==current_index+2) and (i%10!=0):#if the third move is 2 to the right of the original index and it is not wrapping around the sides of the board (or to the right of the second move)...
            right_right = True #the players third move is to the right of the second move
            return(True) #this is a valid move
    elif(vertical_down): #if the players second move was below the original index...
        if(i==current_index+20): #if the third move is 2 down from the original index (or below the second move)...
            down_down = True #the players third move is below the second move
            return(True) #this is a valid move
        if(i==current_index-10): #if the third move is above the original index
            down_up = True #the players third move is above the original index
            return(True) #this is a valid move
    elif(vertical_up): #if the players second move was above the original index...
        if(i==current_index-20): #if the third move is 2 above the original index (or 1 above the second move)
            up_up = True #the players third move is above the second move
            return(True) #this is a valid move
        if(i==current_index+10): #if the third move is below the original index
            up_down = True #the players third move is below the original index
            return(True) #this is a valid move

def ValidMove_4(i): #is the fourth letter being placed on a valid button in relation to the original index, the second letter, and the third letter?
    global current_index
    global left_left
    global left_right
    global right_right
    global right_left
    global up_up
    global up_down
    global down_down
    global down_up
    global llr
    global lll 
    global rrl
    global rrr
    global uud
    global uuu
    global ddu 
    global ddd
    if(left_left): #if the last two moves were to the left of the original index
        if(i==current_index+1) and (i%10!=0): #if the fourth move is to the right of the original index and it not wrapping around the sides of the board
            llr = True #the fourth move is to the right of the original index
            return(True) #this is a valid move
        if(i==current_index-3) and (i%10!=9): #if the fourth move is 3 to the left of the original index and is not wrapping around the sides of the board
            lll=True #the fourth move is to the left of the third move
            return(True) #this is a valid move
    elif(left_right or right_left): #if the last two moves were to the right and left of the original index
        if(i==current_index+2) and (i%10!=0): #if the fourth move is 2 to the right of the original index and is not wrapping around the sides of the board
            rrl = True #there are 2 letters to the right of the original index and 1 letter to the left of the original index
            return(True) #this is a valid move
        if(i==current_index-2) and (i%10!=9): #if the fourth move is 2 to the left of the original index and is not wrapping around the sides of the board
            llr = True #there are 2 letters to the left of the origianl index and 1 letter to the right of the origianl index
            return(True) #this is a valid move
    elif(right_right): #if the last two moves were to the right of the original index
        if(i==current_index-1) and (i%10!=9): #if the fourth move is to the left of the original index and is not wrapping around the sides of the board
            rrl = True #the fourth move is to the left of the original index
            return(True) #this is a valid move
        if(i==current_index+3) and (i%10!=0): #if the fourth move is to the right of the third move and is not wrappign around the sides of the board
            rrr = True #the fourth move is to the right of the third move
            return(True) #this is a valid move
    elif(up_up): #if the last two moves were above the original index
        if(i==current_index+10): #if the fourth move is below the original index
            uud = True #the fourth move is below the original index
            return(True) #this is a valid move
        if(i==current_index-30): #if the fourth move is above the third move
            uuu = True #the fourth move is above the third move
            return(True) #this is a valid move
    elif(up_down or down_up): #if the last two moves were above and below the original index
        if(i==current_index+20): #if the fourth move is 2 below the original index
            ddu = True #there are 2 letters below the original index and 1 letter above the original index
            return(True) #this is a valid move
        if(i==current_index-20): #if the fourth move is 2 above the original index
            uud = True #there are 2 letters above the original index and 1 letter below the original index
            return(True) #this is a valid move
    elif(down_down): #if the last two moves were below the original index
        if(i==current_index-10): #if the fourth move is above the original index
            ddu = True #the fourth move is above the original index 
            return(True) #this is a valid move
        if(i==current_index+30): #if the fourth move is below the third move
            ddd = True #the fourth move is below the third move
            return(True) #this is a valid move

def ValidMove_5(i): #is the fifth letter being placed on a valid button in relation to the original index, the second letter, the third letter, and the fourth letter?
    global current_index
    global llr
    global lll 
    global rrl
    global rrr
    global uud
    global uuu
    global ddu 
    global ddd
    if(llr): #if there are 2 letters to the left of the original index and 1 letter to the right of the original index
        if(i==current_index-3) and (i%10!=9): #if the fifth move is 3 to the left of the original index
            return(True) #this is a valid move
        if(i==current_index+2) and (i%10!=0): #if the fifth move is 2 to the right of the original index
            return(True) #this is a valid move
    elif(lll): #if there are 3 letters to the left of the original index
        if(i==current_index+1) and (i%10!=0): #if the fifth move is 1 to the right of the original index
            return(True) #this is a valid move
        if(i==current_index-4) and (i%10!=9): #if the fifth move is 4 to the left of the original index
            return(True) #this is a valid move
    elif(rrl): #if there are 2 letters to the right of the original index and 1 letter to the left of the original index
        if(i==current_index-2) and (i%10!=9): #if the fifth move is 2 to the left of the original index
            return(True) #this is a valid move
        if(i==current_index+3) and (i%10!=0): #if the fifth move is 3 to the right of the original index
            return(True) #this is a valid move
    elif(rrr): #if there are 3 letters to the right of the original index
        if(i==current_index-1) and (i%10!=9): #if the fifth move is 1 to the left of the original index
            return(True) #this is a valid move
        if(i==current_index+4) and (i%10!=0): #if the fifth move is 4 to the right of the original index
            return(True) #this is a valid move
    elif(uud): #if there are 2 letters above the original index and 1 letter below the original index
        if(i==current_index-30): #if the fifth move is 3 above the original index
            return(True) #this is a valid move
        if(i==current_index+20): #if the fifth move is 2 below the original index
            return(True) #this is a valid move
    elif(uuu): #if there are 3 letters above the original index
        if(i==current_index-40): #if the fifth move is 4 above the original index
            return(True) #this is a valid move
        if(i==current_index+10): #if the fifth move is 1 below the original index
            return(True) #this is a valid move
    elif(ddu): #if there are 2 letters below the original index and 1 letter above the original index
        if(i==current_index-20): #if the fifth move is 2 above the original index
            return(True) #this is a valid move
        if(i==current_index+30): #if the fifth move is 3 below the original index 
            return(True) #this is a valid move
    elif(ddd): #if there are 3 letters below the original index 
        if(i==current_index-10): #if the fifth move is 1 above the original index
            return(True) #this is a valid move
        if(i==current_index+40): #if the fifth move is 4 below the original index
            return(True) #this is a valid move

def reset_direction():#direction of vertical or horizontal and order of placement is reset once each ship has been finalized
    global vertical_up 
    global vertical_down
    global horizontal_right
    global horizontal_left
    global left_left
    global left_right
    global right_right
    global right_left
    global up_up
    global up_down
    global down_down
    global down_up
    global llr
    global lll 
    global rrl
    global rrr
    global uud
    global uuu
    global ddu 
    global ddd
    vertical_up = False
    vertical_down = False
    horizontal_right = False
    horizontal_left = False
    left_left = False
    left_right = False
    right_right = False
    right_left = False
    up_up = False
    up_down = False
    down_down = False
    down_up = False
    lll = False
    llr = False
    rrr = False
    rrl = False
    uuu = False
    uud = False
    ddu = False
    ddd = False

def EnoughSpace(i, button_ids):#is there enough space on the board to fit the entire ship here? are the spaces to the left/right/up/down empty?
    global placing_ships
    if(placing_ships==3): #is there 3 spaces for C to go?
        if((i+10)<=99) and ((i+20)<=99):#check 2 spaces above index
            if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                return(True)
        if((i-10)>=0) and ((i-20)>=0):#check 2 spaces below index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == ""):
                return(True)
        if((i-10)>=0) and ((i+10)<=99):#check 1 space below and 1 space above index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i+10].cget('text') == ""):
                return(True)
        if((i+1)<=99) and ((i+2)<=99):#check 2 spaces to right of index
            if((i+1)%10!=0) and ((i+2)%10!=0):
                if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                    return(True)
        if((i-1)>=0) and ((i-2)>=0):#check 2 spaces to left of index
            if((i-1)%10!=9) and ((i-2)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == ""):
                    return(True)
        if((i+1)<=99) and ((i-1)>=0):#check 1 space to the right of index and 1 space to the left of index
            if((i+1)%10!=0) and ((i-1)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i+1].cget('text') == ""):
                    return(True)
        else:
            return(False)#this is not a valid move because the user won't be able to fit their entire ship in any orientation
    elif(placing_ships==6): #is there 4 spaces for D to go?
        if((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99):#check 3 spaces above index
            if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == ""):
                return(True)
        if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0):#check 3 spaces below index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == ""):
                return(True)
        if((i-10)>=0) and ((i+10)<=99) and ((i+20)<=99):#check 1 space below and 2 spaces above index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                return(True)
        if((i+1)<=99) and ((i+2)<=99) and ((i+3)<=99):#check 3 spaces to right of index
            if((i+1)%10!=0) and ((i+2)%10!=0) and ((i+3)%10!=0):
                if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == ""):
                    return(True)
        if((i-1)>=0) and ((i-2)>=0) and ((i-3)>=0):#check 3 spaces to left of index
            if((i-1)%10!=9) and ((i-2)%10!=9) and ((i-3)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == ""):
                    return(True)
        if((i-10)>=0) and ((i-20)>=0) and ((i+10)<=99):#check 1 space above and 2 spaces below index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i+10].cget('text') == ""):
                return(True)
        if((i+1)<=99) and ((i-1)>=0) and ((i-2)>=0):#check 1 space to the right of index and 2 spaces to the left of index
            if((i+1)%10!=0) and ((i-1)%10!=9) and ((i-2)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i+1].cget('text') == ""):
                    return(True)
        if((i+1)<=99) and ((i+2)<=99) and ((i-1)>=0):#check 1 space to the left of index and 2 spaces to the right of index
            if((i+1)%10!=0) and ((i+2)%10!=0) and ((i-1)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                    return(True)
        else:
            return(False)#this is not a valid move because the user won't be able to fit their entire ship in any orientation
    elif(placing_ships==10): #is there 5 spaces for E to go?
        if((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99) and ((i+40)<=99): #check 4 spaces above index
            if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == "") and (button_ids[i+40].cget('text') == ""):
                return(True)
        if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0) and ((i-40)>=0):#check 4 spaces below index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == "") and (button_ids[i-40].cget('text') == ""):
                return(True)
        if((i+1)<=99) and ((i+2)<=99) and ((i+3)<=99) and ((i+4)<=99):#check 4 spaces to right of index
            if((i+1)%10!=0) and ((i+2)%10!=0) and ((i+3)%10!=0) and ((i+4)%10!=0):
                if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == "") and (button_ids[i+4].cget('text') == ""):
                    return(True)
        if((i-1)>=0) and ((i-2)>=0) and ((i-3)>=0) and ((i-4)>=0):#check 4 spaces to left of index
            if((i-1)%10!=9) and ((i-2)%10!=9) and ((i-3)%10!=9) and ((i-4)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == "") and (button_ids[i-4].cget('text') == ""):
                    return(True)
        if((i-10)>=0) and ((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99):#check 1 space below and 3 spaces above index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == ""):
                return(True)
        if((i-10)>=0) and ((i-20)>=0) and ((i+10)<=99) and ((i+20)<=99):#check 2 spaces below and 2 spaces above index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                return(True)
        if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0) and ((i+10)<=99):#check 1 space above and 3 spaces below index
            if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == "") and (button_ids[i+10].cget('text') == ""):
                return(True)
        if((i+1)<=99) and ((i+2)<=99) and ((i+3)<=99) and ((i-1)>=0):#check 1 space to the left of index and 3 spaces to the right of index
            if((i+1)%10!=0) and ((i+2)%10!=0) and ((i+3)%10!=0) and ((i-1)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == ""):
                    return(True)
        if((i+1)<=99) and ((i+2)<=99) and ((i-1)>=0) and ((i-2)>=0):#check 2 spaces to the left of index and 2 spaces to the right of index
            if((i+1)%10!=0) and ((i+2)%10!=0) and ((i-1)%10!=9) and ((i-2)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                    return(True)
        if((i+1)<=99) and ((i-1)>=0) and ((i-2)>=0) and ((i-3)>=0):#check 1 space to the right of index and 3 spaces to the left of index
            if((i+1)%10!=0) and ((i-1)%10!=9) and ((i-2)%10!=9) and ((i-3)%10!=9):
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == "") and (button_ids[i+1].cget('text') == ""):
                    return(True)
        else:
            return(False) #this is not a valid move because the user won't be able to fit their entire ship in any orientation
    else:
        return(True)

def EnoughSpace_2(i, button_ids):#is the user orientating their ship in the correct direction to fit the entire ship?
    global placing_ships
    global current_index
    if(placing_ships==4): #is the second C going to block the user from not being able to place the third C? 
        if(i==current_index+1): #if i is to the right of index...
            if((i+1)<=99) and ((i+1)%10!=0): #check that the next space to the right is empty
                if(button_ids[i+1].cget('text') == ""):
                    return(True)
            if((current_index-1)>=0) and ((current_index-1)%10!=9): #check that the space to the left of the original is empty
                if(button_ids[current_index-1].cget('text') == ""):
                    return(True)
        if(i==current_index-1): #if i is to the left of index...
            if((i-1)>=0) and ((i-1)%10!=9): #check that the next space to the left is empty
                if(button_ids[i-1].cget('text') == ""):
                    return(True)
            if((current_index+1)<=99) and ((current_index+1)%10!=0): #check that the space to the right of the original is empty
                if(button_ids[current_index+1].cget('text') == ""):
                    return(True)
        if(i==current_index+10): #if i is below the index...
            if((i+10)<=99): #check that the next space down is empty
                if(button_ids[i+10].cget('text') == ""):
                    return(True)
            if((current_index-10)>=0): #check that the space above the original is empty
                if(button_ids[current_index-10].cget('text') == ""):
                    return(True)
        if(i==current_index-10): #if i is above the index...
            if((i-10)>=0): #check that the next space up is empty
                if(button_ids[i-10].cget('text') == ""):
                    return(True)
            if((current_index+10)<=99): #check that the space below the original is empty
                if(button_ids[current_index+10].cget('text') == ""):
                    return(True)
        else:
            return(False) #this is not a valid move because the user won't be able to finish placing their ship
    elif(placing_ships==7): #is the second D going to block the user from not being able to place the third and fourth D?    
        if(i==current_index+1): #if i is to the right of index...
            if((i+1)<=99) and ((i+1)%10!=0) and ((i+2)<=99) and ((i+2)%10!=0): #check that the next 2 spaces to the right are empty
                if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                    return(True)
            if((current_index-1)>=0) and ((current_index-1)%10!=9) and ((current_index-2)>=0) and ((current_index-2)%10!=9): #check that 2 spaces to the left of the original index are empty
                if(button_ids[current_index-1].cget('text') == "") and (button_ids[current_index-2].cget('text') == ""):
                    return(True)
            if((i+1)<=99) and ((i+1)%10!=0) and ((current_index-1)>=0) and ((current_index-1)%10!=9):#check that the next space to the right is empty and 1 space to the left of the original index is empty
                if(button_ids[i+1].cget('text') == "") and (button_ids[current_index-1].cget('text') == ""):
                    return(True) 
        if(i==current_index-1): #if i is to the left of index...
            if((i-1)>=0) and ((i-1)%10!=9) and ((i-2)>=0) and ((i-2)%10!=9): #check that the next 2 spaces to the left are empty
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == ""):
                    return(True)
            if((current_index+1)<=99) and ((current_index+1)%10!=0) and ((current_index+2)<=99) and ((current_index+2)%10!=0): #check that 2 spaces to the right of the original index is empty
                if(button_ids[current_index+1].cget('text') == "") and (button_ids[current_index+2].cget('text') == ""):
                    return(True)
            if((i-1)>=0) and ((i-1)%10!=9) and ((current_index+1)<=99) and ((current_index+1)%10!=0): #check that the next space to the left is empty and 1 space to the right of the original index is empty
                if(button_ids[i-1].cget('text') == "") and (button_ids[current_index+1].cget('text') == ""):
                    return(True)
        if(i==current_index+10): #if i is below the index...
            if((i+10)<=99) and ((i+20)<=99): #check that the next 2 spaces down are empty
                if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                    return(True)
            if((current_index-10)>=0) and ((current_index-20)>=0): #check that 2 spaces above the original index is empty
                if(button_ids[current_index-10].cget('text') == "") and (button_ids[current_index-20].cget('text') == ""):
                    return(True)
            if((i+10)<=99) and ((current_index-10)>=0): #check that the next space down is empty and 1 space above the original index is empty
                if(button_ids[i+10].cget('text') == "") and (button_ids[current_index-10].cget('text') == ""):
                    return(True)
        if(i==current_index-10): #if i is above the index
            if((i-10)>=0) and ((i-20)>=0): #check that the next 2 spaces up are empty
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == ""):
                    return(True)
            if((current_index+10)<=99) and ((current_index+20)<=99): #check that 2 spaces below the original index is empty
                if(button_ids[current_index+10].cget('text') == "") and (button_ids[current_index+20].cget('text') == ""):
                    return(True)    
            if((i-10)>=0) and ((current_index+10)<=99): #check that the next space up is empty and 1 space below the original index is empty
                if(button_ids[i-10].cget('text') == "") and (button_ids[current_index+10].cget('text') == ""):
                    return(True)
        else:
            return(False) #this is not a valid move because the user won't be able to finish placing their ship
    elif(placing_ships==11): #is the second E going to block the user from not being able to place the third, fourth, and fifth E?
        if(i==current_index+1): #if i is to the right of index...
            if((i+1)<=99) and ((i+1)%10!=0) and ((i+2)<=99) and ((i+2)%10!=0) and ((i+3)<=99) and ((i+3)%10!=0): #check that the next 3 spaces to the right are empty
                if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == ""):
                    return(True)
            if((current_index-1)>=0) and ((current_index-1)%10!=9) and ((current_index-2)>=0) and ((current_index-2)%10!=9) and ((current_index-3)>=0) and ((current_index-3)%10!=9): #check that 3 spaces to the left of the original index are empty
                if(button_ids[current_index-1].cget('text') == "") and (button_ids[current_index-2].cget('text') == "") and (button_ids[current_index-3].cget('text') == ""):
                    return(True)
            if((i+1)<=99) and ((i+1)%10!=0) and ((i+2)<=99) and ((i+2)%10!=0) and ((current_index-1)>=0) and ((current_index-1)%10!=9):#check that the next 2 spaces to the right are empty and 1 space to the left of the original index is empty
                if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[current_index-1].cget('text') == ""):
                    return(True) 
            if((i+1)<=99) and ((i+1)%10!=0) and ((current_index-1)>=0) and ((current_index-1)%10!=9) and ((current_index-2)>=0) and ((current_index-2)%10!=9): #check that the next space to the right is empty and 2 spaces to the left of the original index is empty
                if(button_ids[i+1].cget('text') == "") and (button_ids[current_index-1].cget('text') == "") and (button_ids[current_index-2].cget('text') == ""):
                    return(True)
        if(i==current_index-1): #if i is to the left of index...
            if((i-1)>=0) and ((i-1)%10!=9) and ((i-2)>=0) and ((i-2)%10!=9) and ((i-3)>=0) and ((i-3)%10!=9): #check that the next 3 spaces to the left are empty
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == ""):
                    return(True)
            if((current_index+1)<=99) and ((current_index+2)<=99) and ((current_index+3)<=99) and ((current_index+1)%10!=0) and ((current_index+2)%10!=0) and ((current_index+3)%10!=0): #check that 3 spaces to the right of the original index are empty
                if(button_ids[current_index+1].cget('text') == "") and (button_ids[current_index+2].cget('text') == "") and (button_ids[current_index+3].cget('text') == ""):
                    return(True)
            if((i-1)>=0) and ((i-1)%10!=9) and ((i-2)>=0) and ((i-2)%10!=9) and ((current_index+1)<=99) and ((current_index+1)%10!=0): #check that the next 2 spaces to the left are empty and 1 space to the right of the original index is empty
                if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[current_index+1].cget('text') == ""):
                    return(True)
            if((i-1)>=0) and ((i-1)%10!=9) and ((current_index+1)<=99) and ((current_index+1)%10!=0) and ((current_index+2)<=99) and ((current_index+2)%10!=0): #check that the next space to the left is empty and 2 spaces to the right of the original index is empty
                if(button_ids[i-1].cget('text') == "") and (button_ids[current_index+1].cget('text') == "") and (button_ids[current_index+2].cget('text') == ""):
                    return(True)
        if(i==current_index+10): #if i is below the index...
            if((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99): #check that the next 3 spaces down are empty
                if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == ""):
                    return(True)
            if((current_index-10)>=0) and ((current_index-20)>=0) and ((current_index-30)>=0): #check that 3 spaces above the original index are empty
                if(button_ids[current_index-10].cget('text') == "") and (button_ids[current_index-20].cget('text') == "") and (button_ids[current_index-30].cget('text') == ""):
                    return(True)
            if((i+10)<=99) and ((i+20)<=99) and ((current_index-10)>=0): #check that the next 2 spaces down are empty and 1 space above the original index is empty
                if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[current_index-10].cget('text') == ""):
                    return(True)
            if((i+10)<=99) and ((current_index-10)>=0) and ((current_index-20)>=0): #check that the next space down is empty and 2 spaces above the original index is empty
                if(button_ids[i+10].cget('text') == "") and (button_ids[current_index-10].cget('text') == "") and (button_ids[current_index-20].cget('text') == ""):
                    return(True)
        if(i==current_index-10): #if i is above the index...
            if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0): #check that the next 3 spaces up are empty
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == ""):
                    return(True)
            if((current_index+10)<=99) and ((current_index+20)<=99) and ((current_index+30)<=99): #check that 3 spaces below the original index are empty
                if(button_ids[current_index+10].cget('text') == "") and (button_ids[current_index+20].cget('text') == "") and (button_ids[current_index+30].cget('text') == ""):
                    return(True)    
            if((i-10)>=0) and ((i-20)>=0) and ((current_index+10)<=99): #check that the next 2 spaces up are empty and 1 space below the original index is empty
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[current_index+10].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((current_index+10)<=99) and ((current_index+20)<=99): #check that the next space up is empty and 2 spaces below the original index is empty
                if(button_ids[i-10].cget('text') == "") and (button_ids[current_index+10].cget('text') == "") and (button_ids[current_index+20].cget('text') == ""):
                    return(True)
        else:
            return(False) #this is not a valid move because the user won't be able to finish placing their ship
    else:
        return(True)

def PlaceShip(i, button_ids): #sends the index to be changed to change function after checking if the placement is valid
    global num_ships
    global enter_amount
    global placing_ships
    global current_index
    global player1
    global player2
    if(num_ships==1): #if the user chose for each player to have one ship
        enter_amount = 1 #you will only be clicking the board once (A)
        #instantiate players' ship_lives
        player1.ships = {
            "A": Ship(1)
        }
        player2.ships = {
            "A": Ship(1)
        }
    elif(num_ships==2): #if the user chose for each player to have two ships
        enter_amount = 3 #you will be clicking the board 3 times (ABB)
        #instantiate players' ship_lives
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2)
        }
    elif(num_ships==3): #if the user chose for each player to have three ships
        enter_amount = 6 #you will be clicking the board 6 times (ABBCCC)
        #instantiate players' ship_lives
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3)
        }
    elif(num_ships==4): #if the user chose for each player to have four ships
        enter_amount = 10 #you will be clicking the board 10 times (ABBCCCDDDD)
        #instantiate players' ship_lives
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4)
        }
    else: #i.e. num_ships = 5
        enter_amount = 15 #you will be clicking the board 15 times (ABBCCCDDDDEEEEE)
        #instantiate players' ship_lives
        player1.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4),
            "E": Ship(5)
        }
        player2.ships = {
            "A": Ship(1),
            "B": Ship(2),
            "C": Ship(3),
            "D": Ship(4),
            "E": Ship(5)
        }

    player1.total_lives = enter_amount
    player2.total_lives = enter_amount
    if(placing_ships==0): #placing ship A
        change(i, button_ids)#the button will be changed to A. (A can be placed anywhere on the board)
    elif(placing_ships==1 or placing_ships==3 or placing_ships==6 or placing_ships==10):#placing first letter of ship
        reset_direction() #forget the previous orientations and reset for the next ship
        if(EnoughSpace(i, button_ids)):#before beginning to place a ship, it checks if there is even enough spaces on the board to fit the entire ship
            change(i, button_ids)#the button will be changed. (The first letter placed of a ship can be placed anywhere on the board)
            current_index = i #the index of the first letter of a ship placement is stored
    elif(placing_ships==2 or placing_ships==4 or placing_ships==7 or placing_ships==11):#placing second letter of ship
        if(EnoughSpace_2(i, button_ids)):#there is clearly enough space on the board to fit the entire ship. This check makes sure the user starts clicking in the right direction that has enough spaces. 
            if(ValidMove_2(i)): #if the index of the second letter to be placed is above/below the original index or to the right/left of the original index then this is a valid move
                change(i, button_ids)#the button will be changed to the letter of the ship being placed
    elif(placing_ships==5 or placing_ships==8 or placing_ships == 12):#placing third letter of ship
        if(ValidMove_3(i)):#if the third index of the third letter to be placed is either above/below the other 2 letters or to the right/left of the other 2 letters then this is a valid move
            change(i, button_ids)#the button will be changed to the letter of the ship being placed
    elif(placing_ships==9 or placing_ships==13):#placing fourth letter of ship
        if(ValidMove_4(i)):#if the fourth index of the fourth letter to be placed is either above/below the other 3 letters or to the right/left of the other 3 letters then this is a valid move
            change(i, button_ids)#the button will be changed to the letter of the ship being placed
    elif(placing_ships==14):#placing fifth letter of ship (only applies to ship E)
        if(ValidMove_5(i)):#if the final E is either above/below the other E's or to the right/left of the other E's then this is a valid move
            change(i, button_ids)#the button will be changed to E

def change(i, button_ids):#changes the button to a letter and the button ids are updated based on if the player 1 or player 2 buttons are being clicked
    global player1
    global player2
    global text_variable
    global selected_ships
    global enter_amount 
    global placing_ships 
    if (selected_ships < enter_amount) and (button_ids[i].cget('text') == ""):#you are only allowed to change a button if you have not finished placing all your ships and if that button hasn't been clicked yet 
        if(selected_ships==0): #if you haven't clicked the board yet, your first click will place ship A and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the ValidMove functions
            text_variable = 'A'
            placing_ships = placing_ships + 1 
        elif(selected_ships>0 and selected_ships<=2):#if you have clicked the board once, the next two clicks will place ship B and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the ValidMove functions
            text_variable = 'B'
            placing_ships = placing_ships + 1
        elif(selected_ships>2 and selected_ships<=5):#if you have clicked the board three times, you are now placing ship C and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the ValidMove functions
            text_variable = 'C'
            placing_ships = placing_ships + 1
        elif(selected_ships>5 and selected_ships<=9):#if you have clicked the board five times, you are now placing ships D and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the ValidMove functions
            text_variable = 'D'
            placing_ships = placing_ships + 1
        else: #else you are placing ship E and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the ValidMove functions
            text_variable = 'E'
            placing_ships = placing_ships + 1
         
        bname = (button_ids[i])#store the current button id in bname
        bname.configure(text=text_variable)#update the current button to be a different text (either A,B,C,D,E)
        selected_ships = selected_ships + 1 #every time a button is actually changed to a letter, selected_ships is updated. Once selected_ships==enter_amount then the user can't keep placing more letters/ships
        if(selected_ships==enter_amount): #once the player has clicked the placing ships board the full number of times so that every ship is placed then the Finalize Ship Placement button apears
            if(button_ids == player1.my_board):#have the button appear on player 1's screen if player 1's board was just finalized 
                frame4_button = Button(frame4, text="Finalize Ship\nPlacement", padx=20, pady=20, command=partial(setup_frame5)).grid(row = 11, column = 22)#when Finalize Ship Placement is pressed then setup_frame5 function is called
            else:#have the button appear on player 2's screen if player 2's board was just finalized 
                frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, command=partial(show_frame,frame6)).grid(row = 11, column = 22)#when Finalized Ship Placement is pressed then frame6 displays on the screen
            

def setup_frame5():#simple function that resets all the variables so player 2 sees a fresh board and frame 5 is shown so player 2 can start placing their ships.
    reset()#important that reset doesn't happen until Finalize Ship Placement is pressed otherwise variables will be reset too early and player 1 can keep placing more ships 
    show_frame(frame5)


def reset():#resets variables that handle the general board placement so player 2 sees fresh board when placing their battleships
    global text_variable
    global selected_ships
    global enter_amount
    global placing_ships
    global current_index
    text_variable = 'A'
    selected_ships = 0
    enter_amount = 0
    placing_ships = 0
    current_index = 0

# @drawBoard:Helper Function for drawing the boards for the player turn screens
    #frame = frame to draw board on 
    #type = "p1" or "p2" - specifies which enemy board to work with
    #size = size of button i.e. value of padx and pady
    #offset_r = number of rows to offset by
    #offset_c = number of columns to offset by
def drawBoards(type, size, offset_r, offset_c):
    print("test DRAWBOARDS")
    global player1
    global player2
    if type == "p1":
        print("HERE P1")
    
        #draw player board  
        for i in range(10):
            # shape the grid
            setsize2 = Canvas(frame7, width=size, height=0).grid(row=11, column=i)
            setsize2 = Canvas(frame7, width=0, height=size).grid(row=i, column=11)

        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            #copy important attributes of current button
            img= player1.my_board[i].cget("image")
            txt = player1.my_board[i].cget("text")
            b = player1.my_board[i].cget("bg")

            temp = player1.my_board[i]
            button = Button(master=frame7, image=img, text=txt, bg=b) #make a copy
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player1.my_board[i] = button #replace button with copied button
            temp.destroy() #destroy old button

            

       
        #draw enemy board
        for i in range(10):
            # shape the grid
            setsize1 = Canvas(frame7, width=size, height=0).grid(row=11, column=i+offset_c)
            setsize1 = Canvas(frame7, width=0, height=size).grid(row=i, column=11+offset_c)
        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            button = player1.enemy_board[i]
            button.grid(row=item[0], column=item[1]+offset_c, sticky="n,e,s,w")

    else: #type = "p2"
        #detach buttons from frame5 canvas

        #draw player board  
        for i in range(10):
            # shape the grid
            setsize2 = Canvas(frame9, width=size, height=0).grid(row=11, column=i)
            setsize2 = Canvas(frame9, width=0, height=size).grid(row=i, column=11)

        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            #copy important attributes of current button
            img= player2.my_board[i].cget("image")
            txt = player2.my_board[i].cget("text")
            b = player2.my_board[i].cget("bg")

            temp = player2.my_board[i]
            button = Button(master=frame9, image=img, text=txt, bg=b) #make a copy
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player2.my_board[i] = button #replace button with copied button
            temp.destroy()
       
        #draw enemy board
        for i in range(10):
            # shape the grid
            setsize1 = Canvas(frame9, width=size, height=0).grid(row=11, column=i+offset_c)
            setsize1 = Canvas(frame9, width=0, height=size).grid(row=i, column=11+offset_c)
        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            button = player2.enemy_board[i]
            button.grid(row=item[0], column=item[1]+offset_c, sticky="n,e,s,w")


def board(type, size): #size = width and length of the canvas
    global player1 
    global player2
    global P1_ENEMY_CREATED
    global P2_ENEMY_CREATED
    print(P1_ENEMY_CREATED)
    print(P2_ENEMY_CREATED)
    print(size)
    if type == 'p1_set': #it is player 1's turn and they are placing their ships
        pos = product(range(10), range(10))
        
        #initialize player 1's board
        for i in range(10):
            #shape the grid
            setsize = Canvas(frame4, width=size, height=0).grid(row=11, column=i)
            setsize = Canvas(frame4, width=0, height=size).grid(row=i, column=11)
        for i, item in enumerate(pos):
            button = Button(frame4, command=partial(PlaceShip, i, player1.my_board))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player1.my_board.append(button)
    if type == 'p1_attack': #it is player 1's turn and they are attacking 
        if not P1_ENEMY_CREATED:
            pos = product(range(10), range(10))
            #create
            for i in range(10):
                # shape the grid
                setsize = Canvas(frame7, width=size, height=0).grid(row=11, column=i)
                setsize = Canvas(frame7, width=0, height=size).grid(row=i, column=11)
            for i, item in enumerate(pos):
                button = Button(frame7, text="", command=partial(Attack, i, "p1"))
                button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
                player1.enemy_board.append(button)
            P1_ENEMY_CREATED = True   

        #draw the frame7 screen
        drawBoards("p1", size, offset_r=0, offset_c=14) #offset between boards
        show_frame(frame7)

    if type == 'p2_set': #it is player 1's turn and they are placing their ships
        pos = product(range(10), range(10))

        for i in range(10):
            # shape the grid
            setsize = Canvas(frame5, width=size, height=0).grid(row=11, column=i)
            setsize = Canvas(frame5, width=0, height=size).grid(row=i, column=11)
        
        for i, item in enumerate(pos):
            button = Button(frame5, command=partial(PlaceShip, i, player2.my_board))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player2.my_board.append(button)

    if type == 'p2_attack': #it is player 2's turn and they are attacking 
        if not P2_ENEMY_CREATED:
            pos = product(range(10), range(10))
            #create
            for i in range(10):
                # shape the grid
                setsize = Canvas(frame9, width=size, height=0).grid(row=11, column=i)
                setsize = Canvas(frame9, width=0, height=size).grid(row=i, column=11)

            for i, item in enumerate(pos):
                button = Button(frame9, text="", command=partial(Attack, i, "p2"))
                button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
                player2.enemy_board.append(button)
            #print(player2.enemy_board)
            P2_ENEMY_CREATED = True  
            frame5.forget()

        #draw the frame9 screen
        drawBoards("p2", size, offset_r=0, offset_c=14) #offset between boards
        show_frame(frame9)

def SetupFrame3(number_of_ships):
    shipcount(number_of_ships)
    show_frame(frame3)
    
myButton1 = Button(frame2, text="1 ship  ",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(shipcount, 1)).place(relx=.5,rely=.3,anchor= CENTER)
myButton2 = Button(frame2, text="2 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(shipcount, 2)).place(relx=.5,rely=.4,anchor= CENTER)
myButton3 = Button(frame2, text="3 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(shipcount, 3)).place(relx=.5,rely=.5,anchor= CENTER)
myButton4 = Button(frame2, text="4 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(shipcount, 4)).place(relx=.5,rely=.6,anchor= CENTER)
myButton5 = Button(frame2, text="5 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(shipcount, 5)).place(relx=.5,rely=.7,anchor= CENTER)

def show_done_button(type):
    global frame7_button
    global frame9_button
    if type == "p1":
        frame9_button.configure(state=DISABLED)
        frame7_button.configure(state=NORMAL)
    elif type == "p2":
        frame7_button.configure(state=DISABLED)
        frame9_button.configure(state=NORMAL)

#Attack_Method
def Attack(i, type): #playerId = "p1" or "p2"
    global player1
    global player2
    global enter_amount
    global p1_hit_counter 
    global p2_hit_counter 
    print(p1_hit_counter)
    print(p2_hit_counter)

    global p1_fired
    global p2_fired
    global img_miss
    global img_hit
    if(type == "p1"): #miss
        p2_fired = False
        if not p1_fired:
            btn_text = player2.my_board[i].cget("text")
            if(btn_text == ""): #miss!
                player1.enemy_board[i].configure(bg="white", image=img_miss, compound = "center", state ='disabled') #miss
                player2.my_board[i].configure(bg="white", image=img_miss, compound = "center", state ='disabled')
                show_done_button("p1")
            else: #hit! there is a ship at i
                print(btn_text)
                player2.ships[btn_text].lives = int(player2.ships[btn_text].lives) - 1 #update lives for hit ship
                player2.total_lives -= 1 #update total lives for player two

                
                player1.enemy_board[i].configure(bg="red", image=img_hit, compound = "center", state ='disabled')
                player2.my_board[i].configure(bg="red", image=img_hit, compound = "center", state ='disabled')
                show_done_button("p1")
            p1_fired = True
    elif(type == "p2"):
        p1_fired = False
        if not p2_fired:
            btn_text = player1.my_board[i].cget("text")
            if(player1.my_board[i].cget("text") == ""): #miss
                player2.enemy_board[i].configure(bg="white", image=img_miss, compound = "center", state ='disabled') #miss
                player1.my_board[i].configure(bg="white", image=img_miss, compound = "center", state ='disabled')
                show_done_button("p2")
            else: #hit! there is a ship at i
                player1.ships[btn_text].lives = int(player1.ships[btn_text].lives) - 1 #update lives for hit ship
                player1.total_lives -= 1 #update total lives for player one

                player2.enemy_board[i].configure(bg="red", image=img_hit, compound = "center", state ='disabled')   
                player1.my_board[i].configure(bg = 'red', image=img_hit, compound = "center", state ='disabled')
                show_done_button("p2")
            p2_fired = True

#Frame 1 code
myLabel1 = Label(frame1, text="Battleship!\nPress start to begin playing.",font=("Arial", 25)).place(relx=.5, rely=.2,anchor= CENTER)
frame1_button = Button(frame1, text="Start",font=("Arial",70, BOLD), command=partial(show_frame,frame2), bg="white", padx=20,pady=20).place(relx=.50, rely=.5,anchor= CENTER)

#Frame 2 code
myLabel2 = Label(frame2, text="Choose the number of ships each player will have.",font=("Arial",30, BOLD)).place(relx=.51, rely=.2,anchor= CENTER)

#Frame 3 code
e = Entry(frame3,width=50)
e.place(anchor=CENTER, relx=0.5, rely=0.45)
e.insert(0, "Enter Player 1 Name Here")
b = Entry(frame3, width=50)
b.place(anchor=CENTER, relx=0.5, rely=0.5)
b.insert(0, "Enter Player 2 Name Here")
#button
frame3_button = Button(frame3, text="Enter", command=partial(set_player_names), padx= 15, pady=15).place(anchor=CENTER, relx=0.5, rely=0.55,)

#Frame 4 code   
    #label created inside set_player_names function
board('p1_set', 40)

#frame 5 code
   #label created inside set_player_names function
board('p2_set', 40)

def checkWin(nextFrame):
    global player1
    global player2
    
    p1_lives = 0
    for k in player1.ships.keys():
        num = player1.ships[k].lives
        p1_lives += num

    p2_lives = 0
    for k in player2.ships.keys():
        num = player2.ships[k].lives
        p2_lives += num


    if p2_lives == 0:
        show_frame(frame10)
        label_10_p1 = Label(frame10, text="Player 1 Wins!!!", padx=20, pady=20).grid(row=1, column=0)
    elif p1_lives == 0:
        show_frame(frame10)
        label_10_p2 = Label(frame10, text="Player 2 Wins!!!", padx=20, pady=20).grid(row=1, column=0)
    else:
        show_frame(nextFrame)

#frame 6 code = popup player 1
frame6_button = Button(frame6, text="Ready Player 1?", padx=20, pady=20, command=partial(board, "p1_attack", 40)).place(anchor=CENTER, relx=0.5, rely=0.3,)


#frame 7 = player 1 turn
mylabel = Label(frame7, text="Select a grid to attack").grid(row=1, column=12)
label_key_red = Label(frame7, text="Red = HIT", fg='red', bg='grey').grid(row=2, column=12)
label_key_white = Label(frame7, text="White = MISS", fg='white', bg='black').grid(row=3, column=12)
label_key_black = Label(frame7, text="Black = SUNK", fg='black', bg='white').grid(row=4, column=12)
my_board_label = Label(frame7, text="Your Board").grid(row=12, column=3, columnspan=3)
enemy_board_label = Label(frame7, text="Enemy Board").grid(row=12, column=17,columnspan=3)

frame7_button = Button(frame7, text="Player 1 Done", padx=20, pady=20, state = DISABLED, command=partial(checkWin, frame8))
frame7_button.grid(row=14, column=12)

#frame 8 = popup player 2   
frame8_button = Button(frame8, text="Ready Player 2?", padx=20, pady=20, command=partial(board, "p2_attack",40)).place(anchor=CENTER, relx=0.5, rely=0.3,)

#frame 9 = player 2 turn
mylabel = Label(frame9, text="Select a grid to attack").grid(row=1, column=12)
label_key_red = Label(frame9, text="Red = HIT", fg='red', bg='grey').grid(row=2, column=12)
label_key_white = Label(frame9, text="White = MISS", fg='white', bg='black').grid(row=3, column=12)
label_key_black = Label(frame9, text="Black = SUNK", fg='black', bg='white').grid(row=4, column=12) 
my_board_label = Label(frame9, text="Your Board").grid(row=12, column=3, columnspan=3)
enemy_board_label = Label(frame9, text="Enemy Board").grid(row=12, column=17,columnspan=3)  

frame9_button = Button(frame9, text="Player 2 Done", padx=20, pady=20, state=DISABLED, command=partial(checkWin, frame6))
frame9_button.grid(row=14, column=12)

#Frame 10 = endscreen
frame10_button = Button(frame10, text="Press to Quit", padx=20, pady=20, command=root.destroy).grid(row=2, column = 0)

root.mainloop()