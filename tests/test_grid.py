import os
import unittest

from sudokuless.grid import Grid

class TestGrid(unittest.TestCase):

    def test_getitem(self):
        grid = Grid([0,0,0,0,0,0,6,0,3,
                     0,0,0,0,1,0,0,4,0,
                     2,0,0,0,0,6,0,0,0,
                     1,9,2,0,3,7,4,8,0,
                     8,0,0,0,0,0,5,0,9,
                     3,5,0,6,0,0,2,0,7,
                     0,6,1,9,8,2,3,0,4,
                     7,0,8,0,4,6,9,5,1,
                     9,4,3,0,5,1,8,0,2,])
        self.assertEqual(grid[1,1], 0)
        self.assertEqual(grid[4,3], 0)
        self.assertEqual(grid[8,8], 2)
        self.assertEqual(grid[8], [9,4,3,0,5,1,8,0,2])
        self.assertEqual(grid[0], [0,0,0,0,0,0,6,0,3])
        self.assertEqual(grid[3], [1,9,2,0,3,7,4,8,0])
        self.assertEqual(grid[3,1:3], [9,2])
        self.assertEqual(grid[:,3], [0,0,0,0,0,6,9,0,0])
        self.assertEqual(grid[1:5,0], [0,2,1,8])
        self.assertEqual(grid[2:6,4], [0,3,0,0])
        self.assertEqual(grid[1:3,2:4], [[0,0],[0,0]])
        self.assertEqual(grid[3:6,2:5], [[2,0,3],[0,0,0],[0,6,0]])

    def test_is_over(self):
        grid_no = Grid([0,0,0,0,0,0,6,0,3,
                        0,0,0,0,1,0,0,4,0,
                        2,0,0,0,0,5,0,0,0,
                        1,9,2,0,3,7,4,8,0,
                        8,0,0,0,0,0,5,0,9,
                        3,5,0,6,0,0,2,0,7,
                        0,6,1,9,8,2,3,0,4,
                        7,0,8,0,4,6,9,5,1,
                        9,4,3,0,5,1,8,0,2,])
        grid_yes = Grid([4,1,5,8,7,9,6,2,3,
                        6,8,9,2,1,3,7,4,5,
                        2,3,7,4,6,5,1,9,8,
                        1,9,2,5,3,7,4,8,6,
                        8,7,6,1,2,4,5,3,9,
                        3,5,4,6,9,8,2,1,7,
                        5,6,1,9,8,2,3,7,4,
                        7,2,8,3,4,6,9,5,1,
                        9,4,3,7,5,1,8,6,2,])
        self.assertFalse(grid_no.is_over)
        self.assertTrue(grid_yes.is_over)
        