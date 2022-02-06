from tkinter import *
from functools import partial
from itertools import product

from player import Player

def show_frame(frame):
    frame.tkraise()

### Global Variables
num_ships = 0
player1 = Player() #initialize player1
player2 = Player() #initialize player1
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


# @drawBoard:Helper Function for Board
    #frame = frame to draw board on 
    #board = board to draw (pass the array itself ex: player1.my_board)
    #size = size of button i.e. value of padx and pady
    #offset_r = number of rows to offset by
    #offset_c = number of columns to offset by
def drawBoard(frame, board, size, offset_r, offset_c):
    #Doesn't work right now. For now it will just creates a new board. 
    for row_num in range(1,11): #iterate through rows
        row_letter = int_to_char(row_num) # 1 = A, 2 = B, etc...
        for col_num in range(1,11): #iterate through columns
            button = Button(frame, text=(row_letter,col_num), padx=size, pady=size, fg='black').grid(row=row_num+offset_r, column=col_num+offset_c, sticky='nsew') 

def board(type, size):
    if type == 'p1_set':
        #initialize player 1's board

        #draw it
        drawBoard(frame4, player1.my_board, size, offset_r=0, offset_c=0)
        
    if type == 'p1_attack':
        drawBoard(frame7, player1.my_board, size, offset_r=0, offset_c=0)
        drawBoard(frame7, player1.enemy_board, size, offset_r=0, offset_c=12)
        show_frame(frame7)

    if type == 'p2_set':
        #initialize player 2's board

        #draw it
        drawBoard(frame5, player2.my_board, size, offset_r=0, offset_c=0)

    if type == 'p2_attack': #Draw p2's board
        drawBoard(frame9, player2.my_board, size, offset_r=0, offset_c=0)
        drawBoard(frame9, player2.enemy_board, size, offset_r=0, offset_c=12)
        show_frame(frame9)


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
    
    #set up frame 5 label
    p2_label = "Player 2 (" + player2.name + ")"
    frame4_label = Label(frame5, text=p2_label).grid(row=2, column=22) 

    show_frame(frame4)

frame3_button = Button(frame3, text="Enter", command=partial(set_player_names)).grid()

#Frame 4 code   
    #label created inside set_player_names function
frame4_button = Button(frame4, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(show_frame,frame5)).grid(row = 9, column = 22)
board('p1_set', 20)

#frame 5 code
   #label created inside set_player_names function
frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(show_frame,frame6)).grid(row = 9, column = 22)
board('p2_set', 20)

def checkWin(nextFrame):
    win = False #for now
    if win == True:
        show_frame(frame10) #show win frame
    else:
        show_frame(nextFrame)

#frame 6 code = popup player 1
frame6_button = Button(frame6, text="Ready Player 1?", padx=20, pady=20, fg='black', command=partial(board, "p1_attack", 10)).place(anchor=CENTER, relx=0.5, rely=0.3,)


#frame 7 = player 1 turn
mylabel = Label(frame7, text="Select a grid to attack").grid(row=1, column=11)
frame7_button = Button(frame7, text="Player 1 Done", padx=20, pady=20, fg='black', command=partial(checkWin, frame8)).grid(row=12, column=11)


#frame 8 = popup player 2   
frame8_button = Button(frame8, text="Ready Player 2?", padx=20, pady=20, fg='black', command=partial(board, "p2_attack", 10)).place(anchor=CENTER, relx=0.5, rely=0.3,)

#frame 9 = player 2 turn
mylabel = Label(frame9, text="Select a grid to attack").grid(row=1, column=11)   
frame9_button = Button(frame9, text="Player 2 Done", padx=20, pady=20, fg='black', command=partial(checkWin, frame6)).grid(row=14, column=11)

#Frame 10 = endscreen
frame10_button = Button(frame10, text="Yay Player x Wins!!", padx=20, pady=20, fg='black').grid()

root.mainloop()