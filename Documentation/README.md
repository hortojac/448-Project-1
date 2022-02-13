# Our Timesheet
https://docs.google.com/spreadsheets/d/1lUsOUC2fbRDljCjvxWwighowklgWpwoVV_gzfDf-2TM/edit?usp=sharing)

# Use this video to learn the basics of Tkinter
https://www.youtube.com/watch?v=YXPyB4XeYLA

# Playing the Game

The interactive GUI allows for button pressing and clicking on <abbr title="any Tkinter element that builds the interface">**widgets**</abbr> to perform actions. You can enter in your names, and click on buttons to both place your ships and attack your enemy's board. 

Here is a demo: 

[Video embed]

# The Code

For our Battleship game, we used `Python` v3.10.0 with the imported libraries of 
- [Tkinter](https://docs.python.org/3/library/tkinter.html) to implement an interactive GUI.
- [functools](https://docs.python.org/3/library/functools.html) to implement partial functions for some Tkinter buttons.
- [itertools](https://docs.python.org/3/library/itertools.html) to more easily implement double for loops
- [PIL/Pillow](https://pillow.readthedocs.io/en/stable/) for image integration (need to install through the terminal)

GUI programming is event-based programming, and this reflects as such in the code: instead of having linear code that executes `line 1`, `line 2`, `line 3`, etc. in order, code runs when its event is triggered. 

For example, in the following code block, even though `setup_frame3` is defined _before_ the `myButton1`, it'll only run _after_ the myButton1 is _clicked_ by the user. The `command = partial(setup_frame3, 1)` defines the function call when the button is clicked. 

```python
def setup_frame3(number_of_ships):
    ship_count(number_of_ships) # passes num_ships into frames 4,5 to set up ship placement 
    show_frame(frame3)

myButton1 = Button(frame2, 
    text="1 ship",
    font=("Arial",20, BOLD), 
    padx=25, pady=25, 
    command=partial(setup_frame3, 1)
    ).place(
      relx=.5, rely=.3,
      anchor= CENTER)
```

### Module List
- start.py - handles GUI
- player.py - tracks player information (names, ships)
- ship.py - tracks ship information (positions, life counter)
- place_board.py - handles ship placement 


## start.py
This handles the main sequence of scenes/frames/screens and all of the GUI. 

<details open>
<summary>Frame List</summary>

- **Frame 1:** The start screen
- **Frame 2:** Select the number of ships to play with
- **Frame 3:** Enter in Player Names
- **Frame 4:** Player 1 Ship Setup
- **Frame 5:** Player 2 Ship Setup
- **Frame 6:** Asks if Player 1 is ready
- **Frame 7:** Player 1 attack screen
- **Frame 8:** Asks if Player 2 is ready
- **Frame 9:** Player 2 Attack screen
- **Frame 10:** Win Screen

> Note: The attack phase loops through frames 6-9.

</details>

<details open>
<summary>Global Variable List</summary>

| Variable and Default/Initalized Value | Where is it Used | Purpose | 
| :--: | :-- | :-- |
| `num_ships = 0` | Set in Frame 2, used in Frames 4-5 | Tracks number of ships selected by player |
| `player1 = Player("Player 1")`  `player2 = Player("Player 2")` | <ul><li>`.name` set in Frame 3, used in Frames 4-10</li><li>`.ships` used in Frames 7, 9</li></ul>  | Creates Player Objects, which track Player information |
| `P1_ENEMY_CREATED = False` `P2_ENEMY_CREATED = False` | Frames 7, 9 | Prevents duplicate board creation |
| `p1_fired = False` `p2_fired = False` | Frames 7, 9 | Determines whether the player can move on to the next frame |
</details>

<details open>
<summary>Button Indexing</summary>

We store button locations not as x/y coordinates, but as a _single_ integer, where 
- `index % 10` is the column number (A-J on an official Battleship board) 
- `ceil(index / 10)` is the row number (1-10 on an official Battleship board)

For example: 

<table>
  <tr>
    <th></th>
    <th>A</th>
    <th>B</th>
    <th>C</th>
    <th>D</th>
    <th>E</th>
    <th>F</th>
    <th>G</th>
    <th>H</th>
    <th>I</th>
    <th>J</th>
  </tr>
  <tr>
    <th>1</th>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>9</td>
    <td>10</td>
  </tr>
  <tr>
    <th>2</th>
    <td>11</td>
    <td>12</td>
    <td>13</td>
    <td>14</td>
    <td>15</td>
    <td>16</td>
    <td>17</td>
    <td>18</td>
    <td>19</td>
    <td>20</td>
  </tr>
  <tr>
    <th>3</th>
    <td>21</td>
    <td>22</td>
    <td>23</td>
    <td>24</td>
    <td>25</td>
    <td>26</td>
    <td>27</td>
    <td>28</td>
    <td>29</td>
    <td>30</td>
  </tr>
  <tr>
    <th>4</th>
    <td>31</td>
    <td>32</td>
    <td>33</td>
    <td>34</td>
    <td>35</td>
    <td>36</td>
    <td>37</td>
    <td>38</td>
    <td>39</td>
    <td>30</td>
  </tr>
  <tr>
    <th>5</th>
    <td>41</td>
    <td>42</td>
    <td>43</td>
    <td>44</td>
    <td>45</td>
    <td>46</td>
    <td>47</td>
    <td>48</td>
    <td>49</td>
    <td>50</td>
  </tr>
  <tr>
    <th>6</th>
    <td>51</td>
    <td>52</td>
    <td>53</td>
    <td>54</td>
    <td>55</td>
    <td>56</td>
    <td>57</td>
    <td>58</td>
    <td>59</td>
    <td>60</td>
  </tr>
  <tr>
    <th>7</th>
    <td>61</td>
    <td>62</td>
    <td>63</td>
    <td>64</td>
    <td>65</td>
    <td>66</td>
    <td>67</td>
    <td>68</td>
    <td>69</td>
    <td>70</td>
  </tr>
  <tr>
    <th>8</th>
    <td>71</td>
    <td>72</td>
    <td>73</td>
    <td>74</td>
    <td>75</td>
    <td>76</td>
    <td>77</td>
    <td>78</td>
    <td>79</td>
    <td>80</td>
  </tr>
  <tr>
    <th>9</th>
    <td>81</td>
    <td>82</td>
    <td>83</td>
    <td>84</td>
    <td>85</td>
    <td>86</td>
    <td>87</td>
    <td>88</td>
    <td>89</td>
    <td>90</td>
  </tr>
  <tr>
    <th>100</th>
    <td>91</td>
    <td>92</td>
    <td>93</td>
    <td>94</td>
    <td>95</td>
    <td>96</td>
    <td>97</td>
    <td>98</td>
    <td>99</td>
    <td>100</td>
  </tr>
</table>

</details>

### Functions

| Function |Type | Arguments | Return Type | Purpose | 
| :--: | :--:  | :-- | :-- | :-- |
| drawBoards |  |  |  |  |
| assign_positions |  |  |  |  |
| board | GUI | board type with 4 possible settings: <ul><li>`p1_set`: Ship placement board for Player 1</li><li>`p1_attack`: Attack board for Player 1</li><li>`p2_set`: Ship placement board for Player 2</li><li>`p1_attack`: Attack board for Player 2</li></ul> | None | Generates board depending on the type passed in as outlined [above](https://gitlab.ku.edu/448-group-11/project-1/-/edit/main/README.md#boards). |
| set_player_names | GUI | None | None | sets player names, then makes a label with the corresponding player name for frames 4 and 5 respectively |
| setup_frame3 |  |  |  |  |
| set_player_names |  |  |  |  |
| ship_count |  |  |  |  |
| choose_ship_number |  |  |  |  |
| p1_place_ships |  |  |  |  |
| setup_frame5 |  |  |  |  |
| p2_place_ships |  |  |  |  |
| attack |  |  |  |  |
| show_done_button |  |  |  |  |
| check_win |  |  |  |  |

## place_board.py

| Function | Arguments  | Purpose | 
| :--: |  :-- |  :-- |
| <ul><li>valid_move_2</li><li>valid_move_3</li><li>valid_move_4</li><li>valid_move_5</li></ul> | button index/location as `i`  | Returns whether the given index is a valid move for the 2nd/3rd/4th/5th ship placement |
| place_ships | None  | <ul><li>Handles all ship placement interaction.</li><li>There are no undo's or resets.</li><li>Ships are placed onto the screen by clicking on buttons one by one.</li></ul>|
| change | button index as `i`, array of buttons as `button_ids`  | Changes the button to a letter (or ship) |
| reset | array of buttons as `button_ids`  | Resets entire board and variables so player 2 sees fresh board when placing their battleships |
| reset | array of buttons as `button_ids`  | Resets entire board and variables so player 2 sees fresh board when placing their battleships |
| set_player_names   | None | sets player names, then makes a label with the corresponding player name for frames 4 and 5 respectively |

## ship.py

Member Variables:
- `positions` - the location(s) of each ship
- `lives` - how many lives a ship has. At the start of the game, this is initalized based on the ship type (e.g. A has 1, B has 2, etc.) and decreases as players land hits. 

Member functions: 
- `to_string()` - prints ship information 

## player.py

Member Variables: 
- `name` - the player name; retrieved during frame 3, used in labels and popups throughout gameplay
- `my_board` - displays the player's board with ships visible
- `enemy_board` - displays the enemy's board with no ships visible UNLESS the player has landed hits/sinks
- `ships` - a dictionary of the player's ships. See code for structure. 

Member functions: 
- `set_ships(num_ships)` - updates `player.ships` depending on the number of ships chosen by the player
- `to_string()` - prints player information except boards 
