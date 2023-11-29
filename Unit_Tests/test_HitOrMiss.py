# Import the unit test module as well as the file containing the main program being tested
import unittest

from richardsonr3 import hitOrMiss
# Creates a class for both unit tests to be placed
class HitORMissTest(unittest.TestCase):
# Creates a function for the first unit test that will check for ships that are hit
    def test_ShipHit(self):
# Places a ship in every position throughout the grid
        grid_size = 10
        grid = [ ['S']*grid_size for i in range(grid_size) ]
# tests the random coordinates (0,0) to see if an X is printed when the ship is hit
        hitOrMiss(grid, 0, 0)
        self.assertEqual(grid[0][0], 'X')
# Creates a function for the second unit test that will check for shots that are missed 
    def test_ShipMiss(self):

        grid_size = 10
# Places a "." representing water in every position in the grid
        grid = [ ['.']*grid_size for i in range(grid_size) ]
# Picks the test coordinates (0,0) to see if an O is printed when the shot is missed
        hitOrMiss(grid, 0, 0)
        self.assertEqual(grid[0][0], 'O')
        


# calls for a unit test to be run for the main function
if __name__ == "__main__":
    unittest.main()
