########################################### QUESTION 1 ###########################################

#class Rectangle:
#    def __init__(self, width, height):
#        self.width = width
#        self.height = height

#    def area(self):
#        return self.width * self.height

#rect = Rectangle(15, 10)
#print(rect.area())

########################################### QUESTION 2 ###########################################

#class Circle:
#    def __init__(self, radius):
#        self.radius = radius

#    def circumference(self):
#        return 2 * 3.14159 * self.radius

#circle = Circle(15)
#print(circle.circumference())

########################################### QUESTION 3 ###########################################

#class Employee:
#    def __init__(self, name, age, salary):
#        self.name = name
#        self.age = age
#        self.salary = salary

#    def raise_salary(self, percentage):
#        self.salary *= (1 + percentage / 100)

#employee = Employee("Salma", 23, 5000)
#employee.raise_salary(20)
#print(employee.salary)

########################################### QUESTION 4 ###########################################

#class Book:
#    def __init__(self, title, author):
#        self.title = title
#        self.author = author

#    def display(self):
#        print(f"{self.title} by {self.author}")

#book = Book("The Catcher in the Rye", "J. D. Salinger")
#book.display()

########################################### QUESTION 5 ###########################################

#class Car:
#    def __init__(self, make, model, year, mileage):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.mileage = mileage

#    def drive(self, miles):
#        self.mileage += miles

#car = Car("BMW", "iX1", 2023, 200000)
#car.drive(100)
#print(car.mileage)

########################################### QUESTION 6 ###########################################

#class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def __del__(self):
#        print(f"{self.name}'s object has been destroyed")

#person = Person("Salma", 23)

########################################### QUESTION 7 ###########################################

#class BankAccount:
#    def __init__(self, account_number, balance):
#        self.account_number = account_number
#        self.balance = balance

#    def __del__(self):
#        print(f"Account {self.account_number} has been closed")

#account = BankAccount("123456789", 6000)

########################################### QUESTION 8 ###########################################

#class Vehicle:
#    def __init__(self, speed):
#        self.speed = speed


#class Car(Vehicle):
#    def __init__(self, speed, brand):
#        super().__init__(speed)
#        self.brand = brand

#    def get_info(self):
#        return f"Brand: {self.brand}, Speed: {self.speed}"

#my_car = Car(180, "BMW")
#print(my_car.get_info())

########################################### QUESTION 9 ###########################################

#class Animal:
#    def __init__(self, name):
#        self.name = name


#class Pet:
#    def __init__(self, owner):
#        self.owner = owner

#class PetAnimal(Animal, Pet):
#    def __init__(self, name, owner):
#        Animal.__init__(self, name)
#        Pet.__init__(self, owner)

#my_pet = PetAnimal("Kittie", "Salma")
#print("The pet's name is : ", my_pet.name)
#print("The pet's owner name is : ", my_pet.owner)

########################################### QUESTION 10 ###########################################

#class Dog(Animal, Pet):
#    def __init__(self, name, owner, breed):
#        Animal.__init__(self, name)
#        Pet.__init__(self, owner)
#        self.breed = breed

#    def get_info(self):
#        return f"Name: {self.name}, Owner: {self.owner}, Breed: {self.breed}"

#my_dog = Dog("Bailey", "Salma", "Border Collie")
#print(my_dog.get_info())

########################################### QUESTION 11 ###########################################

#class Person:
#    def __init__(self, name):
#        my_manager = Manager("Salma", 40000, "Development")

#self.name = name

#class Employee(Person):
#    def __init__(self, name, salary):
#        super().__init__(name)
#        self.salary = salary

#class Manager(Employee):
#    def __init__(self, name, salary, department):
#        super().__init__(name, salary)
#        self.department = department

#    def get_info(self):
#        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"
#print(my_manager.get_info())

########################################### QUESTION 12 ###########################################

#class Shape:
#    def __init__(self, color):
#        self.color = color


#class Rectangle(Shape):
#    def __init__(self, color, width, height):
#        super().__init__(color)
#        self.width = width
#        self.height = height

#my_rectangle = Rectangle("black", 8, 15)
#print("Rectangle color : ", my_rectangle.color, "  -  Rectangle width : ", my_rectangle.width, "  -  Rectangle height : ",my_rectangle.height)   # Output: red

########################################### QUESTION 13 ###########################################

#import math


#class Circle(Shape):
#    def __init__(self, color, radius):
#        super().__init__(color)
#        self.radius = radius

#    def get_area(self):
#        return math.pi * self.radius ** 2


#class Rectangle(Shape):
#    def __init__(self, color, width, height):
#        super().__init__(color)
#        self.width = width
#        self.height = height

#    def get_area(self):
#        return self.width * self.height

#my_circle = Circle("magenta", 3)
#print(my_circle.get_area())

#my_rectangle = Rectangle("black", 8, 15)
#print(my_rectangle.get_area())

########################################### QUESTION 14 ###########################################

#class BankAccount:
#    def __init__(self, initial_balance=0):
#        self.__balance = initial_balance

#    def deposit(self, amount):
#        self.__balance += amount

#    def withdraw(self, amount):
#        if self.__balance >= amount:
#            self.__balance -= amount
#        else:
#            print("Insufficient balance")

#    def get_balance(self):
#        return self.__balance

#my_account = BankAccount(2000)
#print("Balance : ", my_account.get_balance())

#my_account.deposit(1500)
#print("Deposit : ", my_account.get_balance())

#my_account.withdraw(1500)
#print("Insufficient balance : ", my_account.get_balance())

#my_account.withdraw(1000)
#print("Withdraw : ", my_account.get_balance())

########################################### QUESTION 15 ###########################################

#from abc import ABC, abstractmethod

#class Animal(ABC):
#    @abstractmethod
#    def speak(self):
#        pass

#class Dog(Animal):
#    def speak(self):
#        print("Woof!")

#class Cat(Animal):
#    def speak(self):
#        print("Meow!")

#my_dog = Dog()
#my_cat = Cat()

#my_dog.speak()
#my_cat.speak()

########################################### QUESTION 16 ###########################################

#class Calculator:
#    @classmethod
#    def add(cls, n1, n2):
#        return n1 + n2

#result = Calculator.add(10, 15)
#print(result)
