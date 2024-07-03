import unittest

import HelloWorld


class SubTest(unittest.TestCase):
    def test_sub_one(self):
        self.assertEqual(0, HelloWorld.subtract_two_numbers(1, 1))

    def test_sub_two(self):
        self.assertEqual(-3, HelloWorld.subtract_two_numbers(-2, 1))

    def test_sub_three(self):
        self.assertEqual(25, HelloWorld.subtract_two_numbers(-25, -50))


if __name__ == '__main__':
    unittest.main()
