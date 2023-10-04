import os
import sys
import time

class Application:
    def __init__(self):
        self.name = None
        self.surname = None
        self.__email = None
        self.__password = None
        self.choose_keys = [1, 2, 3]
        self.username = None
        self.__password2 = None

    def main_window(self):
        self.clear()
        print("""Salom, Instagramga xush kelibsiz!!!
              Login [1]
              Register [2]
              Log out [3]""")
        selection = int(input("Select section: "))
        while not selection in self.choose_keys:
            self.clear()
            print("""Salom, Instagramga xush kelibsiz!!!
              Login [1]
              Register [2]
              Log out [3]""")
            selection = int(input("Bo'limni tanlang: "))
        if selection == 1:
            self.login()
        if selection == 2:
            self.register()
        if selection == 3:
            self.exit()

    def register(self):
        self.clear()
        print("""          Register          """)
        self.name = input("Ismni kiriting: ").strip()
        self.surname = input("Familiyani kiriting: ").strip()
        self.__email = input("Emailni kiriting: ")
        self.__password = input("Parolni kiriting: ").strip()
        while not len(self.name) > 2:
            self.clear()
            self.name = input("Ismni qaytadan kiriting: ").strip()
        while not len(self.surname) > 2:
            self.clear()
            self.surname = input("Familiyani qaytdan kiriting: ").strip()
        while not (len(self.__email) >= 8 and len(self.__password) >= 8):
            self.clear()
            self.__email = input("Emailni qaytadan kiriting: ").strip()
            self.__password = input("Parolni kiriting: ").strip()
        while not self.check_email(self.__email):
            self.clear()
            self.__email = input("Mavjud emailni kiritdingiz: ").strip()
        while not self.check_password(self.__password):
            self.clear()
            self.__password = input("Mavjud parolni kiritdingiz: ").strip()
        with open("users.txt", "a") as file:
            file.write(f"{self.name}#{self.surname}#{self.__email}#{self.__password}\n")
        print("Qabul qilindi!!!")
        time.sleep(3)
        self.clear()
        print("Muvaffaqiyatli o'tdingiz!!!")
        time.sleep(3)
        self.main_window()

    def check_email(self, email):
        self.clear()
        with open("users.txt", "r") as file:
            users = file.read().split('\n')[:-1]
            for user in users:
                if user.split("#")[2] == email:
                    return False
        return True
    
    def check_password(self, password):
        with open("users.txt", "r") as file:
            users = file.read().split('\n')[:-1]
            for user in users:
                user_password = user.split("#")[2:4]
                if user.split("#")[-1] == password:
                    return False
        return True

    def login(self):
        self.clear()

        print("          Login          ")
        self.username = input("Loginni kiriting: ")
        self.__password2 = input("Parolni kiriting: ")

        while not self.check_login(self.username):
            self.clear()
            self.username = input("Mavjud loginni kiritdingiz: ").strip()

        while not self.check_password2(self.__password2):
            self.clear()
            self.__password2 = input("Mavjud parolni kiritdingiz: ").strip()

        with open("login.txt", "a") as login:
            login.write(f"{self.username}#{self.__password2}\n")
            self.clear()
        print("Muvaffaqiyatli o'tdingiz!!!")
            
    def check_login(self, username):
        self.clear()
        with open("login.txt", "r") as login:
            logins = login.read().split("\n")[:-1]
            for i in logins:
                if i.split("#")[0] == username:
                    return False
        return True
            
    def check_password2(self, password2):
        with open("login.txt", "r") as password:
            passwords = password.read().split('\n')[:-1]
            for j in passwords:
                user_password2 = j.split("#")[1]
                if j.split("#")[-1] == password2:
                    return False
        return True

    @staticmethod
    def clear():
        os.system("cls")

    @staticmethod
    def exit():
        sys.exit()

app = Application()
app.main_window()