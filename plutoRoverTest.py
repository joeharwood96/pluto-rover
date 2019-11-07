import unittest
from plutoRover import plutoRover

class TestPlutoRover(unittest.TestCase):

    def test_x_coordinate_forward(self):
        self.assertEqual(plutoRover([0, 0, "E"], "F", [100, 100]).main(), (1, 0, 'E'))

    def test_x_coordinate_backwards(self):
        self.assertEqual(plutoRover([2, 0, "E"], "B", [100, 100]).main(), (1, 0, 'E'))

    def test_y_coordinate_forward(self):
        self.assertEqual(plutoRover([0, 0, "N"], "F", [100, 100]).main(), (0, 1, 'N'))

    def test_y_coordinate_backwards(self):
        self.assertEqual(plutoRover([0, 2, "N"], "B", [100, 100]).main(), (0, 1, 'N'))

    def test_leftRotation(self):
        self.assertEqual(plutoRover([0, 0, "E"], "L", [100, 100]).main(), (0, 0, 'N'))

    def test_rightRotation(self):
        self.assertEqual(plutoRover([0, 0, "E"], "R", [100, 100]).main(), (0, 0, 'S'))
    
    def test_Errors(self):
        self.assertEqual(plutoRover([0, 0, "N"], "T", [100, 100]).main(), "Sorry, command not found: T")
        self.assertEqual(plutoRover([0, 0, "T"], "F", [100, 100]).main(), "Sorry, direction not found: T")

    def test_multiple_commands(self):
        self.assertEqual(plutoRover([0, 0, "N"], "FFRFF", [100, 100]).main(), (2, 2, 'E'))

if __name__ == '__main__':
    unittest.main()