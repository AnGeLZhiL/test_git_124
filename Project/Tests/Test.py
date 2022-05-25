#Я ЭТО СДЕЛАЛ, ИИСУСЕ ХРИСТОСЕ АААААААААААААААААА

import unittest
from Project.MyFunc import *


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = Vector(lst1, lst2) #Вызов функции из __init__.py
        #Проверка значений через вывод на экран
        print(cls.p.Plus())
        print(cls.p.Minus())

    #Тест равноценности листов с данными о векторах
    def test_EqualityPlus(cls):
        cls.assertEqual((cls.p).Plus(), [11, 22, 53])
    def test_EqualityMinus(cls):
        cls.assertEqual((cls.p).Minus(), [9, 18, 47])
    def tearDown(self):
        print("AAAAAAAAAAAAAAA")