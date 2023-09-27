import os
os.system("cls")

class Employee:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary

class Enterprise_employee(Employee):
    def __init__(self, surname, position, salary, rating):
        super().__init__(surname, position, salary)
        self.rating = rating

    def ish_haqini_oshirish(self):
        if self.rating >= 60 and self.rating < 75:
            self.salary = self.salary + self.salary * 0.2
        elif self.rating >= 75 and self.rating < 90:
            self.salary = self.salary + self.salary * 0.4
        elif self.rating >= 90 and self.rating <= 100:
            self.salary = self.salary + self.salary * 0.6

person1 = Enterprise_employee(surname = input("Ism-familiyani kiriting: "), position = input("Lavozimini kiriting: "), salary = int(input("Maoshini kiriting: ")), rating = int(input("Ratingini kiriting: ")))
person2 = Enterprise_employee(surname = input("Ism-familiyani kiriting: "), position = input("Lavozimini kiriting: "), salary = int(input("Maoshini kiriting: ")), rating = int(input("Ratingini kiriting: ")))
person3 = Enterprise_employee(surname = input("Ism-familiyani kiriting: "), position = input("Lavozimini kiriting: "), salary = int(input("Maoshini kiriting: ")), rating = int(input("Ratingini kiriting: ")))
person4 = Enterprise_employee(surname = input("Ism-familiyani kiriting: "), position = input("Lavozimini kiriting: "), salary = int(input("Maoshini kiriting: ")), rating = int(input("Ratingini kiriting: ")))
person5 = Enterprise_employee(surname = input("Ism-familiyani kiriting: "), position = input("Lavozimini kiriting: "), salary = int(input("Maoshini kiriting: ")), rating = int(input("Ratingini kiriting: ")))

person1.ish_haqini_oshirish()
person2.ish_haqini_oshirish()
person3.ish_haqini_oshirish()
person4.ish_haqini_oshirish()
person5.ish_haqini_oshirish()

print('Surname:', person1.surname, ' | ', 'Position:', person1.position, ' | ', 'Salary:', person1.salary, ' | ', 'Rating:', person1.rating)
print('Surname:', person2.surname, ' | ', 'Position:', person2.position, ' | ', 'Salary:', person2.salary, ' | ', 'Rating:', person2.rating)
print('Surname:', person3.surname, ' | ', 'Position:', person3.position, ' | ', 'Salary:', person3.salary, ' | ', 'Rating:', person3.rating)
print('Surname:', person4.surname, ' | ', 'Position:', person4.position, ' | ', 'Salary:', person4.salary, ' | ', 'Rating:', person4.rating)
print('Surname:', person5.surname, ' | ', 'Position:', person5.position, ' | ', 'Salary:', person5.salary, ' | ', 'Rating:', person5.rating)