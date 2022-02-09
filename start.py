from tkinter import *
from functools import partial
from itertools import product
from player import Player
from PIL import ImageTk, Image



##my_img = ImageTk.PhotoImage(Image.open("assets/white.png"))
#btn = Button(text="HELLO", compound="center", fg="black", image=my_img)
#lol = btn.cget("image")


button_ids_p1 = []
button_ids_p2 = []
button_ids_p1_enemy = []
button_ids_p2_enemy = []



# positions_p1 = product(range(10), range(10))
# positions_p2 = product(range(10), range(10))
# positions_p1_enemy = product(range(10), range(10))
# positions_p2_enemy = product(range(10), range(10))

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
myLabel1 = Label(frame1, text="Battleship!\nPress start to begin playing.", fg="white").grid(row=0, column=0)
frame1_button = Button(frame1, text="Start", padx=25, pady=25, command=partial(show_frame,frame2), fg="black", bg="white").grid(row=1, column=0)

#Frame 2 code
myLabel2 = Label(frame2, text="Choose the number of ships each player will have.", fg="white").grid(row=0, column=0)

def shipcount(x):
    global num_ships
    global player1
    global player2
    num_ships = x
    num = str(x) # get the number as a string

    myLabel = Label(frame2, text="Ships per player: " + num, fg="red").grid(row=6, column=0)
    mylabel = Label(frame4, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p1 on frame4
    mylabel = Label(frame5, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p2 on frame5
    choose_ship_number()


def choose_ship_number():
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
            right_right = True
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

def EnoughSpace(i,button_ids):
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
            return(False)
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
            return(False)
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
            return(False)
    else:
        return(True)


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
        reset_direction() #forget the previous orientations and reset for the next ship
        if(EnoughSpace(i, button_ids)):#before beginning to place a ship, it checks if there is even enough spaces on the board to fit the entire ship
            change(i, button_ids)#the button will be changed. (The first letter placed of a ship can be placed anywhere on the board)
            current_index = i #the index of the first letter of a ship placement is stored
    elif(placing_ships==2 or placing_ships==4 or placing_ships==7 or placing_ships==11):#placing second letter of ship
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
            if(button_ids == button_ids_p1):
                frame4_button = Button(frame4, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(setup_frame5)).grid(row = 11, column = 22)
            else:
                frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(show_frame,frame6)).grid(row = 11, column = 22)
            

def setup_frame5():
    reset()
    show_frame(frame5)


def reset():#resets entire board and variables so player 2 sees fresh board when placing their battleships
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

# @drawBoard:Helper Function for drawing the boards for the player turn screens
    #frame = frame to draw board on 
    #type = "p1" or "p2" - specifies which enemy board to work with
    #size = size of button i.e. value of padx and pady
    #offset_r = number of rows to offset by
    #offset_c = number of columns to offset by
def drawBoards(type, size, offset_r, offset_c):
    print("test DRAWBOARDS")
    
    if type == "p1":
        print("HERE P1")
        global button_ids_p1
        global button_ids_p1_enemy

        #draw player board  
        for i in range(10):
            # shape the grid
            setsize2 = Canvas(frame7, width=size, height=0).grid(row=11, column=i)
            setsize2 = Canvas(frame7, width=0, height=size).grid(row=i, column=11)

        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            #copy important attributes of current button
            img= button_ids_p1[i].cget("image")
            txt = button_ids_p1[i].cget("text")
            b = button_ids_p1[i].cget("bg")
         
            button = Button(master=frame7, image=img, text=txt, bg=b) #make a copy
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            button_ids_p1[i] = button #replace button with copied button

       
        #draw enemy board
        for i in range(10):
            # shape the grid
            setsize1 = Canvas(frame7, width=size, height=0).grid(row=11, column=i+offset_c)
            setsize1 = Canvas(frame7, width=0, height=size).grid(row=i, column=11+offset_c)
        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            button = button_ids_p1_enemy[i]
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
            img= button_ids_p2[i].cget("image")
            txt = button_ids_p2[i].cget("text")
            b = button_ids_p2[i].cget("bg")
         
            button = Button(master=frame9, image=img, text=txt, bg=b) #make a copy
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            button_ids_p2[i] = button #replace button with copied button

       
        #draw enemy board
        for i in range(10):
            # shape the grid
            setsize1 = Canvas(frame9, width=size, height=0).grid(row=11, column=i+offset_c)
            setsize1 = Canvas(frame9, width=0, height=size).grid(row=i, column=11+offset_c)
        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            button = button_ids_p2_enemy[i]
            button.grid(row=item[0], column=item[1]+offset_c, sticky="n,e,s,w")


def board(type, size): #size = width and length of the canvas
    global P1_ENEMY_CREATED
    global P2_ENEMY_CREATED
    print(P1_ENEMY_CREATED)
    print(P2_ENEMY_CREATED)
    if type == 'p1_set': #it is player 1's turn and they are placing their ships
        pos = product(range(10), range(10))
        global button_ids_p1
        #initialize player 1's board
        for i in range(10):
            #shape the grid
            setsize = Canvas(frame4, width=30, height=0).grid(row=11, column=i)
            setsize = Canvas(frame4, width=0, height=30).grid(row=i, column=11)
        for i, item in enumerate(pos):
            button = Button(frame4, command=partial(PlaceShip, i, button_ids_p1))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            button_ids_p1.append(button)
 
    
    if type == 'p1_attack': #it is player 1's turn and they are attacking 
        if not P1_ENEMY_CREATED:
            global button_ids_p1_enemy
            pos = product(range(10), range(10))
            #create
            for i in range(10):
                # shape the grid
                setsize = Canvas(frame7, width=30, height=0).grid(row=11, column=i)
                setsize = Canvas(frame7, width=0, height=30).grid(row=i, column=11)
            for i, item in enumerate(pos):
                button = Button(frame7, text="", command=partial(PlaceShip, i, button_ids_p1_enemy))
                button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
                button_ids_p1_enemy.append(button)
            #print(button_ids_p1_enemy)
            P1_ENEMY_CREATED = True   

        #draw the frame7 screen
        drawBoards("p1", size, offset_r=0, offset_c=14) #offset between boards
        show_frame(frame7)

    if type == 'p2_set': #it is player 1's turn and they are placing their ships
        global button_ids_p2
        pos = product(range(10), range(10))

        for i in range(10):
            # shape the grid
            setsize = Canvas(frame5, width=30, height=0).grid(row=11, column=i)
            setsize = Canvas(frame5, width=0, height=30).grid(row=i, column=11)
        
        for i, item in enumerate(pos):
            button = Button(frame5, command=partial(PlaceShip, i, button_ids_p2))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            button_ids_p2.append(button)

    if type == 'p2_attack': #it is player 2's turn and they are attacking 
        if not P2_ENEMY_CREATED:
            global button_ids_p2_enemy
            pos = product(range(10), range(10))
            #create
            for i in range(10):
                # shape the grid
                setsize = Canvas(frame9, width=30, height=0).grid(row=11, column=i)
                setsize = Canvas(frame9, width=0, height=30).grid(row=i, column=11)

            for i, item in enumerate(pos):
                button = Button(frame9, text="", command=partial(PlaceShip, i, button_ids_p2_enemy))
                button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
                button_ids_p2_enemy.append(button)
            #print(button_ids_p2_enemy)
            P2_ENEMY_CREATED = True  
            frame5.forget()
       
        #draw the frame9 screen
        drawBoards("p2", size, offset_r=0, offset_c=14) #offset between boards
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
    show_frame(frame4)

#set up frame 4 label
p1_label = "Player 1 (" + player1.name + ")"
frame4_label = Label(frame4, text=p1_label).grid(row=2, column=22)  

#set up frame 5 label
p2_label = "Player 2 (" + player2.name + ")"
frame4_label = Label(frame5, text=p2_label).grid(row=2, column=22) 


frame3_button = Button(frame3, text="Enter", command=partial(set_player_names)).grid()

#Frame 4 code   
    #label created inside set_player_names function
#frame4_button = Button(frame4, text="Finalize Ship\nPlacement", padx=20, pady=20, fg='black', command=partial(show_frame,frame5)).grid(row = 9, column = 22)

board('p1_set', 30)

#frame 5 code
   #label created inside set_player_names function
board('p2_set', 30)

def checkWin(nextFrame):
    win = False #for now
    if win == True:
        show_frame(frame10) #show win frame
    else:
        show_frame(nextFrame)

#frame 6 code = popup player 1
frame6_button = Button(frame6, text="Ready Player 1?", padx=20, pady=20, fg='black', command=partial(board, "p1_attack", 10)).place(anchor=CENTER, relx=0.5, rely=0.3,)


#frame 7 = player 1 turn
mylabel = Label(frame7, text="Select a grid to attack").grid(row=1, column=12)
my_board_label = Label(frame7, text="Your Board", fg="white").grid(row=12, column=3, columnspan=3)
enemy_board_label = Label(frame7, text="Enemy Board", fg="white").grid(row=12, column=17,columnspan=3)
frame7_button = Button(frame7, text="Player 1 Done", padx=20, pady=20, fg='black', command=partial(checkWin, frame8)).grid(row=14, column=12)



#frame 8 = popup player 2   
frame8_button = Button(frame8, text="Ready Player 2?", padx=20, pady=20, fg='black', command=partial(board, "p2_attack", 10)).place(anchor=CENTER, relx=0.5, rely=0.3,)

#frame 9 = player 2 turn
mylabel = Label(frame9, text="Select a grid to attack").grid(row=1, column=12) 
my_board_label = Label(frame9, text="Your Board", fg="white").grid(row=12, column=3, columnspan=3)
enemy_board_label = Label(frame9, text="Enemy Board", fg="white").grid(row=12, column=17,columnspan=3)  
frame9_button = Button(frame9, text="Player 2 Done", padx=20, pady=20, fg='black', command=partial(checkWin, frame6)).grid(row=14, column=12)

#Frame 10 = endscreen
frame10_button = Button(frame10, text="Yay Player x Wins!!", padx=20, pady=20, fg='black').grid()

root.mainloop()