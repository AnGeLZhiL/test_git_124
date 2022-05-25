lst1 = [10, 20, 50] #Первый вектор
lst2 = [1, 2, 3] #Второй вектор

#Я сделал всё по-своему. Работает? Да, и слава богу.

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def Plus(self):
        return [a+b for a,b in zip(lst1, lst2)]
    def Minus(self):
        return [a-b for a,b in zip(lst1, lst2)]