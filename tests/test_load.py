import os
import unittest
from unittest import TestCase

from xl_sudoku_solver import load_from_text
from xl_sudoku_solver.exceptions import FormatError

class TestLoad(unittest.TestCase):

    def test_load(self):
        with self.assertRaises(FormatError):
            load_from_text(None)
        with self.assertRaises(FormatError):
            load_from_text('')
        with self.assertRaises(FormatError):
            load_from_text('123456789')
        with self.assertRaises(FormatError):
            load_from_text('123456789\n123456789')
        with self.assertRaises(FormatError):
            load_from_text('123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789')
        with self.assertRaises(FormatError):
            load_from_text('123d26789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789')
        with self.assertRaises(FormatError):
            load_from_text('i1xxxx64x\n5xx1x328x\nxxx75xy1x\n8x4325xxx\n96xxxx7xx\nxxx97685x\n698x37421\n421x895xx\n3x7241x6x')
        with self.assertRaises(FormatError):
            load_from_text("""
            123456789
            12x456789
            123456789
            12345678
            123456789
            123456789
            123456789
            123456789
            12345678x""")
        with self.assertRaises(FormatError):
            load_from_text("""
            123456789
            12x456789
            123456789
            12345678xx
            123456789
            123456789
            123456789
            123456789
            12345678x""")

        self.assertEqual(load_from_text('123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789\n123456789'),
            [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
        self.assertEqual(load_from_text("""
                             12345        6789
                            12345          6789
                           12345            6789
                          12345              6789
                        12345                 6789
                         12345                 6789
                          12345                 6789
                            12345                6789
                              12345               6789"""),
            [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
        self.assertEqual(load_from_text("""
            123456789
            12x456789
            123456789
            123456789
            123456789
            123456789
            123456789
            123456789
            12345678x"""),
            [[1,2,3,4,5,6,7,8,9],[1,2,None,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,None]])
        self.assertNotEqual(load_from_text("""
            123456789
            12x456789
            123456789
            123456789
            123456789
            123x56789
            123456789
            123456789
            12345678x"""),
            [[1,2,3,4,5,6,7,8,9],[1,2,None,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,None]])
