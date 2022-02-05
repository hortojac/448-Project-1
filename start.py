from tkinter import *

def show_frame(frame):
    frame.tkraise()

root = Tk()
#root.geometry('1200x800')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

### Global Variables
#num_ships = Entry(value=)
###

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
frame1_button = Button(frame1, text="Start", padx=25, pady=25, command=lambda:show_frame(frame2), fg="black").grid(row=1, column=0)

#Frame 2 code
myLabel2 = Label(frame2, text="Choose the number of ships each player will have.", fg="black", bg="white").grid(row=0, column=0)

def shipcount(x):
    if x == 1:
        myLabel = Label(frame2, text="Each player will have 1 ship", fg="red").grid(row=6, column=0)
        mylabel = Label(frame4, text="Place your 1 ship").grid(row=1, column=20)
        mylabel = Label(frame5, text="Place your 1 ship").grid(row=1, column=20)
    elif x == 2:
        myLabel = Label(frame2, text="Each player will have 2 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 2 ships").grid(row=1, column=20)
        mylabel = Label(frame5, text="Place your 2 ships").grid(row=1, column=20)
    elif x == 3:
        myLabel = Label(frame2, text="Each player will have 3 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 3 ships").grid(row=1, column=20)
        mylabel = Label(frame5, text="Place your 3 ships").grid(row=1, column=20)
    elif x == 4:
        myLabel = Label(frame2, text="Each player will have 4 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 4 ships").grid(row=1, column=20)
        mylabel = Label(frame5, text="Place your 4 ships").grid(row=1, column=20)
    else:
        myLabel = Label(frame2, text="Each player will have 5 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 5 ships").grid(row=1, column=20)
        myLabel = Label(frame5, text="Place your 5 ships").grid(row=1, column=20)

def placeships(x):
    if x >= 1:
        ship1 = Button(frame4, text="A", padx=10, pady=10, fg='red').grid(row = 3, column = 20)
        ship1 = Button(frame5, text="A", padx=10, pady=10, fg='red').grid(row = 3, column = 20)
        if x >= 2:
            ship2 = Button(frame4, text="BB", padx=20, pady=10, fg='blue').grid(row = 4, column = 20)
            ship2 = Button(frame5, text="BB", padx=20, pady=10, fg='blue').grid(row = 4, column = 20)
            if x >= 3:
                ship3 = Button(frame4, text="CCC", padx=30, pady=10, fg='orange').grid(row = 5, column = 20)
                ship3 = Button(frame5, text="CCC", padx=30, pady=10, fg='orange').grid(row = 5, column = 20)
                if x >= 4:
                    ship4 = Button(frame4, text="DDDD", padx=40, pady=10, fg='green').grid(row = 6, column = 20)
                    ship4 = Button(frame5, text="DDDD", padx=40, pady=10, fg='green').grid(row = 6, column = 20)
                    if x >= 5:
                        ship5 = Button(frame4, text="EEEEE", padx=50, pady=10, fg='purple').grid(row = 7, column = 20)
                        ship5 = Button(frame5, text="EEEEE", padx=50, pady=10, fg='purple').grid(row = 7, column = 20)


myButton1 = Button(frame2, text="1 ship ", padx=25, pady=25, command=lambda:[shipcount(1), placeships(1)], fg="black").grid(row=1, column=0)
myButton2 = Button(frame2, text="2 ships", padx=25, pady=25, command=lambda:[shipcount(2), placeships(2)], fg="black").grid(row=2, column=0)
myButton3 = Button(frame2, text="3 ships", padx=25, pady=25, command=lambda:[shipcount(3), placeships(3)], fg="black").grid(row=3, column=0)
myButton4 = Button(frame2, text="4 ships", padx=25, pady=25, command=lambda:[shipcount(4), placeships(4)], fg="black").grid(row=4, column=0)
myButton5 = Button(frame2, text="5 ships", padx=25, pady=25, command=lambda:[shipcount(5), placeships(5)], fg="black").grid(row=5, column=0)
myButton6 = Button(frame2, text="Next", padx=5, pady=5, fg="black", command=lambda:show_frame(frame3)).grid(row=7, column=0)

            
#Frame 3 code
e = Entry(frame3,width=50)
e.grid()
e.insert(0, "Enter Player 1 Name Here")
b = Entry(frame3, width=50)
b.grid()
b.insert(0, "Enter Player 2 Name Here")

def getName():
    message1 = e.get()
    message2 = b.get()
    #show_frame(frame4)

frame3_button = Button(frame3, text="Enter", command = lambda:[getName(), show_frame(frame4)]).grid()

#Frame 4 code

def int_to_char(x): #converts given integer into to a character
    return chr(x+64)

def char_to_int(x): #converts given character into an integer
    return int(x) - 64

def getboard1(f): #takes a frame
    for row_num in range(1,11): #iterate through rows
        row_letter = int_to_char(row_num) # 1 = A, 2 = B, etc...
        for col_num in range(1,11): #iterate through columns
            Button(frame4, text=(row_letter,col_num), padx=25, pady=25, fg='black').grid(row=row_num, column=col_num, sticky='nsew')
            myLabel = Label(frame4, text="Player 1").grid(row=2, column=20)
    
frame4_button = Button(frame4, text="Finalize Ship Placement", padx=20, pady=20, fg='black', command=lambda:show_frame(frame5)).grid(row = 8, column = 20)

getboard1()

#frame 5 code
def getboard2():
    for row_num in range(1,11): #iterate through rows
        row_letter = int_to_char(row_num) # 1 = A, 2 = B, etc...
        for col_num in range(1,11): #iterate through columns
            Button(frame5, text=(row_letter,col_num), padx=25, pady=25, fg='black').grid(row=row_num, column=col_num, sticky='nsew')
            myLabel = Label(frame5, text="Player 2").grid(row=2, column=20)
            
frame5_button = Button(frame5, text="Finalize Ship Placement", padx=20, pady=20, fg='black', command=lambda:show_frame(frame6)).grid(row = 8, column = 20)

getboard2()

def checkWin(nextFrame):
    win = False #for now
    if win:
        show_frame(frame10) #show win frame
    else:
        show_frame(nextFrame)

#frame 6 code = popup player 1
frame6_button = Button(frame6, text="Ready Player 1?", padx=20, pady=20, fg='black', command=lambda:show_frame(frame7)).grid(row = 8, column = 20)


#frame 7 = player 1 turn
frame7_button = Button(frame7, text="Player 1 Done", padx=20, pady=20, fg='black', command=lambda:checkWin(frame8)).grid(row = 8, column = 20)
getboard1()

getboard2()
#frame 8 = popup player 2   
frame8_button = Button(frame8, text="Ready Player 2?", padx=20, pady=20, fg='black', command=lambda:show_frame(frame9)).grid(row = 8, column = 20)

#frame 9 = player 2 turn
    #frame 6 = player 1 turn
frame9_button = Button(frame9, text="Player 2 Done", padx=20, pady=20, fg='black', command=lambda:checkWin(frame6)).grid(row = 8, column = 20)

#Frame 10 = endscreen
frame10_button = Button(frame10, text="Yay Player x Wins!!", padx=20, pady=20, fg='black', command=lambda:exit()).grid(row = 8, column = 20)

root.mainloop()