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
    

if __name__ == '__main__':
    unittest.main()