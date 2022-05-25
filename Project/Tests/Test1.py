import unittest

from Project.MyFunc import add
class TestSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,6), 9)

if __name__ == "__main__":
    unittest.main()