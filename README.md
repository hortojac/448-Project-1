For our Battleship game, we used `Python` with the libraries of 
- [Tkinter](https://docs.python.org/3/library/tkinter.html) to implement an interactive GUI.
- [functools](https://docs.python.org/3/library/functools.html) to implement higher order functions (functions that return or pass in other functions)

# Playing the Game

The interactive GUI allows for button pressing and clicking on <abbr title="any Tkinter element that builds the interface">**widgets**</abbr> to perform actions. 

Here is a demo: 

[![Watch the video](https://cdn.discordapp.com/attachments/345868817320116226/940756176591802378/unknown.png)](https://youtu.be/eAZES9qJyAM)

# The Code

GUI programming is event-based programming, and this reflects as such in the code: instead of having linear code that executes `line 1`, `line 2`, `line 3`, etc. in order, code runs when its event is triggered. 

For example, in the following code block, even though `getName` is defined _before_ the `frame3_button`, it'll only run _after_ the frame3_button is _clicked_ by the user. The `command = lambda: [getName(), show_frame(frame4)]` defines what happens when the button is clicked. 

```python
def getName():
    message1 = e.get()
    message2 = b.get()

frame3_button = Button(frame3, text="Enter", command = lambda:[getName(), show_frame(frame4)]).grid()
```

## start.py

This handles the main sequence of scenes/frames/screens. 

<details closed>
<summary>Global Variable List <== **wip, should have name, default value, purpose**</summary>

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
</details>

### Frame List
1. The start screen, click button to move on
2. Select the number of ships to play with 
3. Enter in Player Names
4. Player 1 Ship Setup
5. Player 2 Ship Setup
6. Asks if Player 1 is ready
7. Player 1 attack screen
8. Asks if Player 2 is ready
9. Player 2 Attack screen
10. Win Screen

> Note: The attack phase loops through frames 6-9.

### Button Indexing

We store button locations not as x/y coordinates, but as a _single_ integer, where `index % 10` is the column number and `index / 10` is the row number. For example: 

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | 
| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 
| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 
| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 
| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 
| 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 
| 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 
| 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 
| 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 
| 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 | 

### Boards

In the Board object, we have 4 versions: `p1_set`, `p1_attack`, `p2_set`, and `p2_attack`.
The `set` boards are what each repsect player sees while they set-up/place ships. The ships are visible in this board. The `attack` boards are what the _other_ player sees while they attack. The ships are _not_ visible in this board.
So, during the attack phase, player 1 will see `p1_set` and `p2_attack`. 

`p1_set` will show them
- the current location of their ships
- where player 2 has fired at, and whether each guess was a hit/miss.

`p2_attack` will show them 
- where they have guessed so far, and whether each guess was a hit/miss

### Function List
| Function |Type | Arguements | Return Type | Purpose | 
| :--: | :--:  | :-- | :--: | :-- |
| shipcount | GUI |number of ships as `x` | None | Tells player how many ships they chose, calls `placeships` |
| placeships | GUI | None | None | <ul><li>Handles all ship placement interaction.</li><li>There are no undo's or resets.</li><li>Ships are placed onto the screen by clicking on buttons one by one.</li></ul>|
| int_to_char | Helper | integer as `x` | character | Converts given integer into to a character |
| char_to_int | Helper | character as `x` | integer | Converts given character into an integer |
| ValidMove | Helper | button index/location as `i` | boolean | Returns whether the given index is |
| change | GUI | button index as `i`, array of buttons as `button_ids` | None | Changes the button to a letter (or ship) |
| reset | GUI | array of buttons as `button_ids` | None | Resets entire board and variables so player 2 sees fresh board when placing their battleships |
| board | GUI | board type with 4 possible settings: <ul><li>`p1_set`: Ship placement board for Player 1</li><li>`p1_attack`: Attack board for Player 1</li><li>`p2_set`: Ship placement board for Player 2</li><li>`p1_attack`: Attack board for Player 2</li></ul> | None | Generates board depending on the type passed in as outlined [above](For our Battleship game, we used `Python` with the libraries of 
- [Tkinter](https://docs.python.org/3/library/tkinter.html) to implement an interactive GUI.
- [functools](https://docs.python.org/3/library/functools.html) to implement higher order functions (functions that return or pass in other functions)


