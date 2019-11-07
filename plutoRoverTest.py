import unittest
from plutoRover import plutoRover

class TestPlutoRover(unittest.TestCase):

    def test_x_coordinate(self):
        self.assertEqual(plutoRover([0, 0, "E"], "F", [100, 100]).main(), (1, 0, 'E'))

if __name__ == '__main__':
    unittest.main()