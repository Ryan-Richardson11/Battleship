# Import the unit test module as well as the file containing the main program being tested
import unittest

from richardsonr3 import setupBoard
# Creates a class for both unit tests to be placed
class SetUpTest(unittest.TestCase):
# Creates a function for the first unit test that will check for the correct amount of ships to be placed
    def test_ShipsPlaced(self):
# Initialize variables
        grid_size = 10
        grid = [ [""]*grid_size for i in range(grid_size) ]
        num_of_ships = 5

        setupBoard(grid)
        ships_count = 0
        for i in range(grid_size):
            for j in range(grid_size):
# If a cell on the grid is "S", add 1 to ships_counts
                if grid[i][j] == "S":
                    ships_count += 1
# Checks that ships_count is equal to num_of_ships
        self.assertEqual(ships_count, num_of_ships)
# Creates a function for the second unit test that will check for the rest of the spaces to be filled with "." which represents water
    def test_BoardFilled(self):
# Initialize variables
        grid_size = 10
        grid = [ [""]*grid_size for i in range(grid_size) ]
        num_of_ships = 5
# Checks that all the cells that do not equal "S", or a ship, are filled with "."
        setupBoard(grid)
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] != "S":
                    grid[i][j] = "."
# there should be 95 spaces of water when you subtract the 5 ships from the 10x10 grid
        self.assertEqual(100 - num_of_ships, 95)
# calls for a unit test to be run for the main function
if __name__ == "__main__":
    unittest.main()

