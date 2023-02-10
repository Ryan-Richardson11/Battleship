# Import the random module
import random

# defining the global variables used in this code
grid_size = 10
grid = [ [""]*grid_size for i in range(grid_size) ]
num_of_ships = 5
column_list = "    0   1   2   3   4   5   6   7   8   9"

# Defining the function drawboard() which creates the grid for the game
def drawBoard(myBoard):
# Column list taken from the global variables to represent the labeling for each column
    print(column_list)
# Creating the boarders of the grid along with for loop that creates the rows per the grid size
    print("  +---+---+---+---+---+---+---+---+---+---+")
# Creates the labeling down the rows of the grid and cuts off using end:""
    for i in range(grid_size):
        print(f"{i} |", end="")
        for j in range(grid_size):
# Creates the rest of the cells for the grid through both the rows and the columns.
            print(f" {myBoard[i][j]} |", end="")
        print()
        print("  +---+---+---+---+---+---+---+---+---+---+")
 
# Define setupBoard() function which sets all the ships and water on the board using the random import
def setupBoard(myBoard):
# Creates the variable random_ships to represent the ships placed
    random_ships = 0
    for i in range(grid_size):
        for j in range(grid_size):
# Fills the board with water
            myBoard[i][j] = "."
# Creates a while loop to continue printing random ships until it is equal to the number of ships to account for ship overlaps when randomly generated.
    while random_ships < num_of_ships:
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)
# This will check if another randomly generated ship is placed in the same position and if it is not 1 will be added to random_ships until it is 5
        if myBoard[randomRow][randomCol] != "S":
            myBoard[randomRow][randomCol] = "S"
            random_ships += 1

# Defining a function called hitOrMiss() which detects what will be done to the cell based on if it was water or a ship
def hitOrMiss(myBoard, row, col):
# If the guess is a hit, the board will print the "S" as an "X" 
    if myBoard[row][col] == "S":
        print("Hit!")
        myBoard[row][col] = "X"
# If the guess is a miss, the board will print the "S" as an O
    else:
        print("Miss!")
        myBoard[row][col] = "O"

# Defining a function called isGameOver to test if the game has ended and the user has won
def isGameOver(myBoard):
    for i in range(grid_size):
        for j in range(grid_size):
# If there is still a ship on the board labeled "S", then the gam will continue
            if myBoard[i][j] == "S":
                return False
# Returns true if all the ships have been hit and are no longer on the board in which the game will be over
    return True

# Defining a main() function to call all the previous functions and create the game.
def main(myBoard):
# SetupBoar() is called to initialize everything on the board including random ship positions 
    setupBoard(myBoard)
# Checks if the game is over and if it is not the drawBoard() function is called and the game will print out the boards current state
    while not isGameOver(myBoard):
        drawBoard(myBoard)
        try:
# Asking for a row input from the user
            row = int(input("Please enter a row from 0-9: "))
            if row not in range(grid_size):
                raise ValueError
# Asking for a column input from the user
            col = int(input("Please enter a column from 0-9: "))
            if col not in range(grid_size):
                raise ValueError
# If a value that is not 0-9 is asked, a value error is raised above and accepted as a string that will prompt the user for a new input
        except ValueError:
            print("Sorry that is invalid, please enter a value from 0 to 9.")
            continue
# HitOrMiss function from above is called and checks where the users input correlates on the grid. Such as a hit or miss
        hitOrMiss(myBoard, row, col)
# Alternative to the while loop. If the ships are all sunk and the game IS over. GAME OVER will be printed.
    print("GAME OVER!")

# The global varible "grid" which is a 2D array is passed through main as the argument which is being held by myBoard, syntax used for unit testing.
if __name__ == "__main__":
    main(grid)

