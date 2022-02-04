from tkinter import *

def show_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry('1200x800')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)

for frame in (frame1, frame2, frame3, frame4, frame5):
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
        mylabel = Label(frame4, text="Place your 1 ship").grid(row=1, column=22)
        mylabel = Label(frame5, text="Place your 1 ship").grid(row=1, column=22)
    elif x == 2:
        myLabel = Label(frame2, text="Each player will have 2 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 2 ships").grid(row=1, column=22)
        mylabel = Label(frame5, text="Place your 2 ships").grid(row=1, column=22)
    elif x == 3:
        myLabel = Label(frame2, text="Each player will have 3 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 3 ships").grid(row=1, column=22)
        mylabel = Label(frame5, text="Place your 3 ships").grid(row=1, column=22)
    elif x == 4:
        myLabel = Label(frame2, text="Each player will have 4 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 4 ships").grid(row=1, column=22)
        mylabel = Label(frame5, text="Place your 4 ships").grid(row=1, column=22)
    else:
        myLabel = Label(frame2, text="Each player will have 5 ships", fg="red").grid(row=6, column=0)
        myLabel = Label(frame4, text="Place your 5 ships").grid(row=1, column=22)
        myLabel = Label(frame5, text="Place your 5 ships").grid(row=1, column=22)

def placeships(x):
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

def getboard1():
    for row_num in range(1,11): #iterate through rows
        row_letter = int_to_char(row_num) # 1 = A, 2 = B, etc...
        for col_num in range(1,11): #iterate through columns
            Button(frame4, text=(row_letter,col_num), padx=25, pady=25, fg='black').grid(row=row_num, column=col_num, sticky='nsew')
            myLabel = Label(frame4, text="Player 1").grid(row=2, column=22)
    
frame4_button = Button(frame4, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=lambda:show_frame(frame5)).grid(row = 9, column = 22)

getboard1()

#frame 5 code
def getboard2():
    for row_num in range(1,11): #iterate through rows
        row_letter = int_to_char(row_num) # 1 = A, 2 = B, etc...
        for col_num in range(1,11): #iterate through columns
            Button(frame5, text=(row_letter,col_num), padx=25, pady=25, fg='black').grid(row=row_num, column=col_num, sticky='nsew')
            myLabel = Label(frame5, text="Player 2").grid(row=2, column=22)
            
frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black').grid(row = 9, column = 22)

getboard2()

root.mainloop()