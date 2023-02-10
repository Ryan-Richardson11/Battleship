# Import the unit test module as well as the file containing the main program being tested
import unittest

from richardsonr3 import isGameOver
# Creates a class for both unit tests to be placed
class GameOverTest(unittest.TestCase):
 # Creates a function for the first unit test that will check if the game is over by placing all "X"'s in the grid so there will be no ships left
    def test_isGameOver(self):
        grid = [["X" for j in range(10)] for i in range(10)]
        self.assertTrue(isGameOver(grid))
 # Creates a function for the second unit test that will check if teh game is not over by placing all "S"'s on the grid showing there is still more to be sunk 
    def test_not_game_over(self):
        grid = [["S" for j in range(10)] for i in range(10)]
        self.assertFalse(isGameOver(grid))
        

# calls for a unit test to be run for the main function
if __name__ == "__main__":
    unittest.main()

