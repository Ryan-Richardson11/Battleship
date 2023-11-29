import random

grid_size = 10
grid = [[""]*grid_size for i in range(grid_size)]
num_of_ships = 5
column_list = "    0   1   2   3   4   5   6   7   8   9"

def drawBoard(myBoard):
    print(column_list)
    print("  +---+---+---+---+---+---+---+---+---+---+")

    for i in range(grid_size):
        print(f"{i} |", end="")
        for j in range(grid_size):
            if myBoard[i][j] == " " or myBoard[i][j] == "S":
                print(" . |", end="")
            else:
                print(f" {myBoard[i][j]} |", end="")
        print()
        print("  +---+---+---+---+---+---+---+---+---+---+")

def setupBoard(myBoard):
    random_ships = 0
    for i in range(grid_size):
        for j in range(grid_size):
            myBoard[i][j] = "."

    while random_ships < num_of_ships:
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)

        if myBoard[randomRow][randomCol] != "S":
            myBoard[randomRow][randomCol] = "S"
            random_ships += 1

def hitOrMiss(myBoard, row, col):
    if myBoard[row][col] == "S":
        print("Hit!")
        myBoard[row][col] = "X"
    else:
        print("Miss!")
        myBoard[row][col] = "O"

def isGameOver(myBoard):
    for i in range(grid_size):
        for j in range(grid_size):
            if myBoard[i][j] == "S":
                return False
    return True

def main(myBoard):
    setupBoard(myBoard)
    while not isGameOver(myBoard):
        drawBoard(myBoard)
        try:
            row = int(input("Please enter a row from 0-9: "))
            if row not in range(grid_size):
                raise ValueError
            col = int(input("Please enter a column from 0-9: "))
            if col not in range(grid_size):
                raise ValueError
        except ValueError:
            print("Sorry that is invalid, please enter a value from 0 to 9.")
            continue

        hitOrMiss(myBoard, row, col)

    print("GAME OVER!")


if __name__ == "__main__":
    main(grid)
