import unittest

import HelloWorld


class DivideTest(unittest.TestCase):
    def test_divide_one(self):
        self.assertEqual(1, HelloWorld.divide_two_numbers(1, 1))

    def test_divide_two(self):
        self.assertEqual(-2, HelloWorld.divide_two_numbers(-2, 1))

    def test_divide_three(self):
        self.assertEqual(0.5, HelloWorld.divide_two_numbers(-25, -50))


if __name__ == '__main__':
    unittest.main()
