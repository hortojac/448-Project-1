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
frame4 = Frame(root,)

for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky = 'nsew')

show_frame(frame1)
#Frame 1 code
myLabel1 = Label(frame1, text="Battleship!\nPress start to begin playing.", fg="blue").grid(row=0, column=0)
frame1_button = Button(frame1, text="Start", padx=25, pady=25, command=lambda:show_frame(frame2), fg="black").grid(row=1, column=0)

#Frame 2 code
myLabel2 = Label(frame2, text="Choose the number of ships each player will have.", fg="black", bg="white").grid(row=0, column=0)

def myClick1():
    myLabel = Label(frame2, text="Each player will have 1 ship", fg="red").grid(row=6, column=0)

def myClick2():
    myLabel = Label(frame2, text="Each player will have 2 ships", fg="red").grid(row=6, column=0)

def myClick3():
    myLabel = Label(frame2, text="Each player will have 3 ships", fg="red").grid(row=6, column=0)

def myClick4():
    myLabel = Label(frame2, text="Each player will have 4 ships", fg="red").grid(row=6, column=0)

def myClick5():
    myLabel = Label(frame2, text="Each player will have 5 ships", fg="red").grid(row=6, column=0)

myButton = Button(frame2, text="1 ship ", padx=25, pady=25, command=myClick1, fg="black").grid(row=1, column=0)
myButton = Button(frame2, text="2 ships", padx=25, pady=25, command=myClick2, fg="black").grid(row=2, column=0)
myButton = Button(frame2, text="3 ships", padx=25, pady=25, command=myClick3, fg="black").grid(row=3, column=0)
myButton = Button(frame2, text="4 ships", padx=25, pady=25, command=myClick4, fg="black").grid(row=4, column=0)
myButton = Button(frame2, text="5 ships", padx=25, pady=25, command=myClick5, fg="black").grid(row=5, column=0)
myButton = Button(frame2, text="Next", padx=5, pady=5, fg="black", command=lambda:show_frame(frame3)).grid(row=7, column=0)

            
#Frame 3 code
e = Entry(frame3, width=50)
e.grid()
e.insert(0, "Enter Player 1 Name Here")
b = Entry(frame3, width=50)
b.grid()
b.insert(0, "Enter Player 2 Name Here")

def getName():
    message1 = e.get()
    message2 = b.get()
    #show_frame(frame4)

myButton = Button(frame3, text="Enter", command = lambda:[getName(), show_frame(frame4)]).grid()

#Frame 4 code
def getboard1():
    for x in range(1,11):
        for y in range(1,11):
            Button(frame4, text=(x,y), padx=25, pady=25, fg='black').grid(row=y, column=x, sticky='nsew')
    myLabel = Label(frame4, text="Place your battle ships player 1.").grid(row = 1, column = 20)
    ship1 = Button(frame4, text="A", padx=10, pady=10, fg='red').grid(row = 2, column = 20)
    ship2 = Button(frame4, text="BB", padx=20, pady=10, fg='blue').grid(row = 3, column = 20)
    ship3 = Button(frame4, text="CCC", padx=30, pady=10, fg='orange').grid(row = 4, column = 20)
    ship4 = Button(frame4, text="DDDD", padx=40, pady=10, fg='green').grid(row = 5, column = 20)
    ship5 = Button(frame4, text="EEEE", padx=50, pady=10, fg='purple').grid(row = 6, column = 20)

getboard1()

#frame 5 code

root.mainloop()