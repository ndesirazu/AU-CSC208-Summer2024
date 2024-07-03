import unittest

import HelloWorld


class AddTest(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(2, HelloWorld.add_two_numbers(1, 1))

    def test_add_two(self):
        self.assertEqual(-1, HelloWorld.add_two_numbers(-2, 1))

    def test_add_three(self):
        self.assertEqual(-75, HelloWorld.add_two_numbers(-25, -50))


if __name__ == '__main__':
    unittest.main()
