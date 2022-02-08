from calendar import c
from select import select
from tkinter import *
from functools import partial
from xml.etree.ElementTree import TreeBuilder
from player import Player
from itertools import product

button_ids_p1 = []
button_ids_p2 = []

positions = product(range(10), range(10))
positions_2 = product(range(10), range(10))

def show_frame(frame):
    frame.tkraise()

### Global Variables
num_ships = 0
text_variable = 'A'
selected_ships=0
enter_amount=0
placing_ships=0
current_index=0
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


player1 = Player() #initialize players
player2 = Player()
###



root = Tk()

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
#Frame 1 code
myLabel1 = Label(frame1, text="Battleship!\nPress start to begin playing.", fg="blue").grid(row=0, column=0)
frame1_button = Button(frame1, text="Start", padx=25, pady=25, command=partial(show_frame,frame2), fg="black").grid(row=1, column=0)

#Frame 2 code
myLabel2 = Label(frame2, text="Choose the number of ships each player will have.", fg="black", bg="white").grid(row=0, column=0)

def shipcount(x):
    global num_ships
    global player1
    global player2
    num_ships = x
    num = str(x) # get the number as a string

    myLabel = Label(frame2, text="Ships per player: " + num, fg="red").grid(row=6, column=0)
    mylabel = Label(frame4, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p1 on frame4
    mylabel = Label(frame5, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p2 on frame5
    placeships()


def placeships():
    global num_ships
    x = num_ships
    print("num_ships: " + str(x))
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

def changeBoard(): #helper function for board 
    return

def ValidMove_2(i):
    global current_index
    global vertical_up 
    global vertical_down
    global horizontal_right
    global horizontal_left
    if(i==current_index+1) and (i%10!=0):
        horizontal_right = True
        return(True)
    if(i==current_index-1) and (i%10!=9):
        horizontal_left = True
        return(True)
    if(i==current_index+10):
        vertical_up = True
        return(True)
    if(i==current_index-10):
        vertical_down = True
        return(True)

def ValidMove_3(i):
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
    if(horizontal_left):
        if(i==current_index+1) and (i%10!=0):
            left_right = True
            return(True)
        if(i==current_index-2) and (i%10!=9):
            left_left = True
            return(True)
    elif(horizontal_right):
        if(i==current_index-1) and (i%10!=9):
            right_left = True
            return(True)
        if(i==current_index+2) and (i%10!=0):
            left_right = True
            return(True)
    elif(vertical_down):
        if(i==current_index+10):
            down_up = True
            return(True)
        if(i==current_index-20):
            down_down = True
            return(True)
    elif(vertical_up):
        if(i==current_index-10):
            up_down = True
            return(True)
        if(i==current_index+20):
            up_up = True
            return(True)

def ValidMove_4(i):
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
    if(left_left):
        if(i==current_index+1) and (i%10!=0):
            llr = True
            return(True)
        if(i==current_index-3) and (i%10!=9):
            lll=True
            return(True)
    elif(left_right or right_left):
        if(i==current_index+2) and (i%10!=0):
            rrl = True
            return(True)
        if(i==current_index-2) and (i%10!=9):
            llr = True
            return(True)
    elif(right_right):
        if(i==current_index-1) and (i%10!=9):
            rrl = True
            return(True)
        if(i==current_index+3) and (i%10!=0):
            rrr = True
            return(True)
    elif(up_up):
        if(i==current_index-10):
            uud = True
            return(True)
        if(i==current_index+30):
            uuu = True
            return(True)
    elif(up_down or down_up):
        if(i==current_index+20):
            uud = True
            return(True)
        if(i==current_index-20):
            ddu = True
            return(True)
    elif(down_down):
        if(i==current_index+10):
            ddu = True
            return(True)
        if(i==current_index-30):
            ddd = True
            return(True)

def ValidMove_5(i):
    global current_index
    global llr
    global lll 
    global rrl
    global rrr
    global uud
    global uuu
    global ddu 
    global ddd
    if(llr):
        if(i==current_index-3) and (i%10!=9):
            return(True)
        if(i==current_index+2) and (i%10!=0):
            return(True)
    elif(lll):
        if(i==current_index+1) and (i%10!=0):
            return(True)
        if(i==current_index-4) and (i%10!=9):
            return(True)
    elif(rrl):
        if(i==current_index-2) and (i%10!=9):
            return(True)
        if(i==current_index+3) and (i%10!=0):
            return(True)
    elif(rrr):
        if(i==current_index-1) and (i%10!=9):
            return(True)
        if(i==current_index+4) and (i%10!=0):
            return(True)
    elif(uud):
        if(i==current_index+30):
            return(True)
        if(i==current_index-20):
            return(True)
    elif(uuu):
        if(i==current_index+40):
            return(True)
        if(i==current_index-10):
            return(True)
    elif(ddu):
        if(i==current_index+20):
            return(True)
        if(i==current_index-30):
            return(True)
    elif(ddd):
        if(i==current_index+10):
            return(True)
        if(i==current_index-40):
            return(True)

def reset_direction():#direction of vertical or horizontal is reset once each ship is finalized
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

def PlaceShip(i, button_ids): #sends the index to be changed to change function after checking if the placement is valid
    global num_ships
    global enter_amount
    global placing_ships
    global current_index
    global button_ids_p2
    global button_ids_p1
    if(num_ships==1):
        enter_amount = 1 #you will only be clicking the board once (A)
    elif(num_ships==2):
        enter_amount = 3 #you will be clicking the board 3 times (ABB)
    elif(num_ships==3):
        enter_amount = 6 #you will be clicking the board 6 times (ABBCCC)
    elif(num_ships==4):
        enter_amount = 10 #you will be clicking the board 10 times (ABBCCCDDDD)
    else:
        enter_amount = 15 #you will be clicking the board 15 times (ABBCCCDDDDEEEEE)

    if(placing_ships==0): #placing ship A
        change(i, button_ids)#the button will be changed to A. (A can be placed anywhere on the board)
    elif(placing_ships==1 or placing_ships==3 or placing_ships==6 or placing_ships==10):#placing first letter of ship
        change(i, button_ids)#the button will be changed. (The first letter placed of a ship can be placed anywhere on the board)
        current_index = i #the index of the first letter of a ship placement is stored
        reset_direction() #forget the previous orientations and reset for the next ship
    elif(placing_ships==2 or placing_ships==4 or placing_ships==7 or placing_ships==11):#placing second letter of ship
        if(ValidMove_2(i)): #if the index of the second letter to be placed is above/below the original index or to the right/left of the original index then this is a valid move
            change(i, button_ids)#the button will be changed to the letter of the ship being placed
    elif(placing_ships==5 or placing_ships==8 or placing_ships == 12):#placing third letter of ship
        if(ValidMove_3(i)):#if the third index of the third letter to be placed is either above/below the other 2 letters or to the right/left of the other 2 letters then this is a valid move
            change(i, button_ids)#the button will be changed to the letter of the ship being placed
    elif(placing_ships==9 or placing_ships==13):#placing fourth letter of ship
        if(ValidMove_4(i)):#if the fourth index of the fourth letter to be placed is either above/below the other 3 letters or to the right/left of the other 3 letters then this is a valid move
            change(i, button_ids)#the button will be changed to the letter of the ship being placed
    elif(placing_ships==14):
        if(ValidMove_5(i)):
            change(i, button_ids)

def change(i, button_ids):#changes the button to a letter (or ship)
    global button_ids_p1
    global button_ids_p2
    global text_variable
    global selected_ships
    global enter_amount 
    global placing_ships 
    if (selected_ships < enter_amount) and (button_ids[i].cget('text') == ""):
        if(selected_ships==0): #if you haven't clicked the board yet, your first click will be placing A
            text_variable = 'A'
            placing_ships = placing_ships + 1
        elif(selected_ships>0 and selected_ships<=2):#if you have clicked the board once, the next two clicks will place ship B
            text_variable = 'B'
            placing_ships = placing_ships + 1
        elif(selected_ships>2 and selected_ships<=5):#if you have clicked the board three times, you are now placing ship C
            text_variable = 'C'
            placing_ships = placing_ships + 1
        elif(selected_ships>5 and selected_ships<=9):
            text_variable = 'D'
            placing_ships = placing_ships + 1
        else:
            text_variable = 'E'
            placing_ships = placing_ships + 1
         
        bname = (button_ids[i])
        bname.configure(text=text_variable)
        selected_ships = selected_ships + 1
        if(selected_ships==enter_amount):
            reset(button_ids)

def reset(button_ids):#resets entire board and variables so player 2 sees fresh board when placing their battleships
    global button_ids_p2
    global button_ids_p1
    global text_variable
    global selected_ships
    global enter_amount
    global placing_ships
    global current_index
    global vertical_up 
    global vertical_down
    global horizontal_right
    global horizontal_left
    text_variable = 'A'
    selected_ships = 0
    enter_amount = 0
    placing_ships = 0
    current_index = 0
    vertical_up = False
    vertical_down = False
    horizontal_right = False
    horizontal_left = False
    if(button_ids == button_ids_p1):
        frame4_button = Button(frame4, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(show_frame,frame5)).grid(row = 11, column = 22)
    else:
        frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(show_frame,frame6)).grid(row = 11, column = 22)

def board(type):
    if type == 'p1_set': 
        for i in range(10):
            # shape the grid
            setsize = Canvas(frame4, width=30, height=0).grid(row=11, column=i)
            setsize = Canvas(frame4, width=0, height=30).grid(row=i, column=11)

        for i, item in enumerate(positions):
            button = Button(frame4, command=partial(PlaceShip, i, button_ids_p1))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            button_ids_p1.append(button)

    if type == 'p1_attack':
        for row_num in range(1,11): #iterate through rows
            row_letter = int_to_char(row_num) # 1 = A, 2 = B, etc...
            for col_num in range(1,11): #iterate through columns
                Button(frame9, text=(row_letter,col_num), padx=25, pady=25, fg='black').grid(row=row_num, column=col_num, sticky='nsew')

    if type == 'p2_set':
        for i in range(10):
            # shape the grid
            setsize = Canvas(frame5, width=30, height=0).grid(row=11, column=i)
            setsize = Canvas(frame5, width=0, height=30).grid(row=i, column=11)

        for i, item in enumerate(positions_2):
            button = Button(frame5, command=partial(PlaceShip, i, button_ids_p2))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            button_ids_p2.append(button)

    if type == 'p2_attack':
        for row_num in range(1,11): #iterate through rows
            row_letter = int_to_char(row_num) # 1 = A, 2 = B, etc...
            for col_num in range(1,11): #iterate through columns
                Button(frame7, text=(row_letter,col_num), padx=25, pady=25, fg='black').grid(row=row_num, column=col_num, sticky='nsew')

myButton1 = Button(frame2, text="1 ship ", padx=25, pady=25, command=partial(shipcount, 1), fg="black").grid(row=1, column=0)
myButton2 = Button(frame2, text="2 ships", padx=25, pady=25, command=partial(shipcount, 2), fg="black").grid(row=2, column=0)
myButton3 = Button(frame2, text="3 ships", padx=25, pady=25, command=partial(shipcount, 3), fg="black").grid(row=3, column=0)
myButton4 = Button(frame2, text="4 ships", padx=25, pady=25, command=partial(shipcount, 4), fg="black").grid(row=4, column=0)
myButton5 = Button(frame2, text="5 ships", padx=25, pady=25, command=partial(shipcount, 5), fg="black").grid(row=5, column=0)
myButton6 = Button(frame2, text="Next", padx=5, pady=5, fg="black", command=partial(show_frame,frame3)).grid(row=7, column=0)

            
#Frame 3 code
e = Entry(frame3,width=50)
e.grid()
e.insert(0, "Enter Player 1 Name Here")
b = Entry(frame3, width=50)
b.grid()
b.insert(0, "Enter Player 2 Name Here")

def set_player_names(): #sets player names, then makes a label with the corresponding player name for frames 4 and 5 respectively
    global player1
    global player2
    print(e.get())
    print(b.get())
    player1.name = e.get()
    player2.name = b.get()

    #set up frame 4 label
    p1_label = "Player 1 (" + player1.name + ")"
    frame4_label = Label(frame4, text=p1_label).grid(row=2, column=22)  
    
    #set up frame 4 label
    p2_label = "Player 2 (" + player2.name + ")"
    frame4_label = Label(frame5, text=p2_label).grid(row=2, column=22) 

    show_frame(frame4)

frame3_button = Button(frame3, text="Enter", command=partial(set_player_names)).grid()

#Frame 4 code   
    #label created inside set_player_names function
board('p1_set')

#frame 5 code
   #label created inside set_player_names function
#frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(show_frame,frame6)).grid(row = 11, column = 22)
board('p2_set')


def checkWin(nextFrame):
    win = 'false' #for now
    if win == 'true':
        show_frame(frame10) #show win frame
    else:
        show_frame(nextFrame)

#frame 6 code = popup player 1
frame6_button = Button(frame6, text="Ready Player 1?", padx=20, pady=20, fg='black', command=partial(checkWin, frame7)).grid()

#frame 7 = player 1 turn
mylabel = Label(frame7, text="Select a grid to attack").grid(row=1, column=11)
frame7_button = Button(frame7, text="Player 1 Done", padx=20, pady=20, fg='black', command=partial(checkWin, frame8)).grid(row=2, column=11)
board('p2_attack')

#frame 8 = popup player 2   
frame8_button = Button(frame8, text="Ready Player 2?", padx=20, pady=20, fg='black', command=partial(checkWin, frame9)).grid()

#frame 9 = player 2 turn
#frame 6 = player 1 turn
mylabel = Label(frame9, text="Select a grid to attack").grid(row=1, column=11)   
frame9_button = Button(frame9, text="Player 2 Done", padx=20, pady=20, fg='black', command=partial(checkWin, frame6)).grid(row=2, column=11)
board('p1_attack')

#Frame 10 = endscreen
frame10_button = Button(frame10, text="Yay Player x Wins!!", padx=20, pady=20, fg='black', command=partial(checkWin, frame8)).grid()

root.mainloop()
