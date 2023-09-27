import os
os.system("cls")

class Phone:
    def brand(self):
        pass

class Redmi(Phone):
    def __init__(self):
        super().__init__()

    def brand(self):
        print("Redmi Note 11")

class Samsung(Phone):
    def __init__(self):
        super().__init__()

    def brand(self):
        print("Samsung S23 ultra")

class Iphone(Phone):
    def __init__(self):
        super().__init__()

    def brand(self):
        print("Iphone 15 pro max")

redmi = Redmi()
redmi.brand()

samsung = Samsung()
samsung.brand()

iphone = Iphone()
iphone.brand()