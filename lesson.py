from abc import ABC, abstractmethod
import os
os.system("cls")
from math import *

''' 1 - misol
class Number:
    def __init__(self, son1):
        self.son1 = son1

    def ildiz(self):
        print(sqrt(self.son1))
    
    def kv(self):
        print(self.son1 * self.son1)
    
    def kub(self):
        print(self.son1 * self.son1 * self.son1)
    
class Number2:
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def yigindi(self):
        print(self.son1 + self.son2)

    def ayirma(self):
        print(self.son1 - self.son2)

    def kopaytma(self):
        print(self.son1 * self.son2)

    def bolinma(self):
        print(self.son1 / self.son2)

num = Number(9)
nums = Number2(9, 12)
'''

''' 2 - misol
class Car:
    def __init__(self):
        self.__model = 0
        self.__petrol = 0
        self.__engine = 0

    def set(self, new_model, new_petrol, new_engine):
        self.__model = new_model
        self.__petrol = new_petrol
        self.__engine = new_engine

    def get(self):
        print("Model:", self.__model)
        print("Petrol:", self.__petrol)
        print("Engine:", self.__engine)

car = Car()
car.set("Tesla", 73, "Zavad bo'lib turibdi")
car.get()
'''

class Son(ABC):
    @abstractmethod
    def __init__(self, son1, son2):
        super.__init__(self)
        self.son1 = son1
        self.son2 = son2

    @abstractmethod
    def yigindi(self):
        pass

    def ayirma(self):
        pass

class Yigindi(Son):
    def yigindi(self):
        print("Yig'indi =", self.son1 + self.son2)

class Ayirma(Son):
    def ayirma(self):
        print("Ayirma =", self.son1 - self.son2)

son = Son()
son.


