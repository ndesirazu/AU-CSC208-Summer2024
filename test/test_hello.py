import HelloWorld
import unittest


class HelloTest(unittest.TestCase):
    def test_hello_one(self):
        self.assertEqual("Hello World!", HelloWorld.hello())

    def test_hello_two(self):
        self.assertEqual("Hello World!\n", HelloWorld.hello_line())


if __name__ == '__main__':
    unittest.main()
