import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.p = [10,2,4,5,6]
    def test1(cls):
        cls.p2 = [10,2,4,5,6]
        cls.assertEqual((cls.p),cls.p2)
    def test2(cls):
        cls.assertEqual((cls.p[0]), 10)
    def test3(cls):
        cls.assertNotEqual((cls.p[0]), 9)
    def test4(cls):
        cls.assertGreater((sum(cls.p)), 10)

# slvhsnvfsfbsfbf

    def tearDown(cls):
        print("тесты завершены")