import unittest

import HelloWorld


class ExpoTest(unittest.TestCase):
    def test_expo_one(self):
        self.assertEqual(2, HelloWorld.exponent(2, 1))

    def test_expo_two(self):
        self.assertEqual(8, HelloWorld.exponent(2, 3))

    def test_expo_three(self):
        self.assertEqual(32, HelloWorld.exponent(2, 5))

    def test_expo_four(self):
        self.assertEqual(4, HelloWorld.exponent(16, 0.5))

    def test_expo_five(self):
        self.assertEqual(0.1, HelloWorld.exponent(10, -1))


if __name__ == '__main__':
    unittest.main()
