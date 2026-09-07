#inheritance and multiple inheritance

#-------------------------------------------------------
#inheritance 
#-------------------------------------------------------
# Inheritance is a fundamental concept in object-oriented programming (OOP)
#  that allows a class (called a child or subclass) to inherit properties and behaviors
# (methods) from another class (called a parent or superclass). 
# This promotes code reusability and establishes a hierarchical relationship between classes.


class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

dog = Dog()

dog.bark()  
# Output: Dog is barking.
dog.eat()   
# Output: Animal is eating.


#super() function
#-------------------------------------------------------
# The super() function is used to call a method from the parent class in a child class

# super() is particularly useful in the context of inheritance, as it allows you to 
# access and invoke methods from the parent class without explicitly naming the parent class.
#  This is especially helpful when dealing with multiple inheritance or when you want
#  to ensure that the correct method resolution order (MRO) is followed.


class Person:
    def __init__(self):
        print("Person constructor called.")

class Student(Person):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Person). 
        print("Student constructor called.")

s=Student()  

print(s)

class Animal:
    def __init__(self):
        self.name = "animal"

class Dog(Animal):
    def show_name(self):
        print(self.name)

dog = Dog()
dog.show_name()  # Output: animal

# overriding methods and overloading methods
#-------------------------------------------------------

#overriding methods: In object-oriented programming, method overriding is a feature 
# that allows a subclass (child class) to provide a specific implementation of a method 
# that is already defined in its superclass (parent class).

# When a method in a subclass has the same name, return type, and parameters as a method 
# in its superclass, the subclass's method overrides the superclass's method. 
# This allows the subclass to customize or extend the behavior of the inherited method.

# eg 1:
a= 10
a= 20
b= 30
a+b #output: 50 in here overriding the value of 'a' from 10 to 20

#eg 2:
class Animal:
    def sound(self):
        return "Animal makes a sound."

class Dog(Animal):
    def sound(self):
        return "Dog barks."

dog = Dog()
animal = Animal()

print(dog.sound())   
 # Output: Dog barks.
print(animal.sound()) 
# Output: Animal makes a sound.

#eg 3:
class Animal:
    def sound(self):
        print("Animal makes a soound.")

class Dog(Animal):
    def sound(self):
        super().sound()  # Call the sound method of the parent class (Animal).
        print("Dog baaarks.")

dog = Dog()
animal = Animal()

animal.sound() 
 # Output: Animal makes a sound.
dog.sound()    
 # Output: Dog barks.

#ex 4:
class Animal:
    def eat(self):
        print(f"{self.__class__.__name__} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.__class__.__name__} is barking.")

bruno=Dog()
dog=Animal()
dog.eat() 
 # Output: Animal is eating.
bruno.eat()  
# Output: Dog is eating.
bruno.bark() 
# Output: Dog is barking.

# ex 5:
class vehicle:
    def start(self):
        print(f"{self.__class__.__name__} is starting.")

class car(vehicle):
    def start(self):
        print(f"{self.__class__.__name__} is starting with a roar.")

car=car()
car.start()
# Output: Car is starting with a roar.

# method overloading: Method overloading is a feature in object-oriented programming (OOP)
#  that allows a class to have multiple methods with the same name but different 
# parameter lists.

# eg 1:

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calc = Calculator()
# print(calc.add(2, 3))     
# here the second add method overrides the first one, so only the second method is available.
# so it shows an error because the first add method is not available anymore. 
print(calc.add(2, 3, 4))  
 # Output: 9   here the second add method overrides the first one, 
 # so only the second method is available.


#IS-A and HAS-A relationship
#-------------------------------------------------------

#IS-A relationship: In object-oriented programming (OOP), the "IS-A" relationship is a 
# fundamental concept that describes the relationship between classes in an 
# inheritance hierarchy.
# It indicates that one class (the subclass or derived class) is a specialized version 
# of another class (the superclass or base class). In other words, the subclass "is a" 
# type of the superclass.

#HAS-A relationship: In object-oriented programming (OOP), the "HAS-A" relationship 
# is a concept that describes the relationship between classes based on composition or 
# aggregation. It indicates that one class contains or possesses another class 
# as a part of its structure. In other words, one class "has a" reference to another class.


# ex 1:

class Engine:
    def start(self):
        print("Engine started.")

class car:
    def __init__(self):
        self.engine = Engine()  # HAS-A relationship: Car has an Engine.

    def start_car(self):
        self.engine.start()  # Delegating the start action to the Engine.
        print("Car started.")

car = car()
car.start_car()


#mixing classes
#-------------------------------------------------------

class camera:
    def take_photo(self):
        print("Taking a photo.")

class phone:
    def make_call(self):
        print("Making a call.")

class smartphone(camera, phone):
    pass  # Inherits from both camera and phone classes.

phone = smartphone()
phone.take_photo()  
# Output: Taking a photo.
phone.make_call()
# Output: Making a call.

#-------------------------------------------------------
#multiple inheritance
#-------------------------------------------------------


#multiple inheritance is a feature in object-oriented programming (OOP) that allows
# a class to inherit from more than one parent class.
# This means that a subclass can inherit attributes and methods from multiple 
# superclasses, allowing for greater flexibility and code reuse.

class father:
    def driving(self):
        print( f"{self.__class__.__name__} has programming skills.")

class mother:
    def painting(self):
        print( f"{self.__class__.__name__} has cooking skills.")

class child(father, mother):
    pass  # Inherits from both father and mother classes.

child = child()
child.driving()
child.painting()

#MRO (Method Resolution Order)
#-------------------------------------------------------

# MRO (Method Resolution Order) is a concept in object-oriented programming (OOP) that
#  defines the order in which methods are looked up and resolved in a class hierarchy,
#  especially in the context of multiple inheritance.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show() 
 # Output: Class B

print(D.mro()) # here the method resolution order is D -> B -> C -> A -> object,
# which means that when you call d.show(), Python looks for the show() method in class D 
# first, then in class B, then in class C, and finally in class A. Since class B has 
# a show() method, it is invoked, and "Class B" is printed.