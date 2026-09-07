# Inheritance and Multiple Inheritance in Python

## Table of Contents
1. [Inheritance](#inheritance)
2. [Super() Function](#super-function)
3. [Method Overriding and Overloading](#method-overriding-and-overloading)
4. [IS-A and HAS-A Relationships](#is-a-and-has-a-relationships)
5. [Multiple Inheritance](#multiple-inheritance)
6. [Method Resolution Order (MRO)](#method-resolution-order-mro)

---

## Inheritance

### What is Inheritance?
**Inheritance** is a fundamental concept in object-oriented programming (OOP) that allows a class (called a **child** or **subclass**) to inherit properties and behaviors (methods) from another class (called a **parent** or **superclass**). This promotes code reusability and establishes a hierarchical relationship between classes.

### Basic Example
```python
class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

dog = Dog()
dog.bark()  # Output: Dog is barking.
dog.eat()   # Output: Animal is eating. (inherited method)
```

---

## Super() Function

### What is super()?
The `super()` function is used to call a method from the parent class in a child class. It's particularly useful for:
- Accessing parent class methods
- Following the correct method resolution order (MRO) in multiple inheritance
- Avoiding explicitly naming the parent class

### Example 1: Constructor Chaining
```python
class Person:
    def __init__(self):
        print("Person constructor called.")

class Student(Person):
    def __init__(self):
        super().__init__()  # Calls the parent class constructor
        print("Student constructor called.")

s = Student()
# Output:
# Person constructor called.
# Student constructor called.
```

### Example 2: Using Inherited Attributes
```python
class Animal:
    def __init__(self):
        self.name = "animal"

class Dog(Animal):
    def show_name(self):
        print(self.name)

dog = Dog()
dog.show_name()  # Output: animal
```

---

## Method Overriding and Overloading

### Method Overriding
**Method overriding** allows a subclass to provide a specific implementation of a method that is already defined in its superclass. When a method in a subclass has the same name, return type, and parameters as a method in its superclass, the subclass's method overrides the superclass's method.

#### Example 1: Simple Override
```python
class Animal:
    def sound(self):
        return "Animal makes a sound."

class Dog(Animal):
    def sound(self):
        return "Dog barks."

dog = Dog()
animal = Animal()

print(dog.sound())     # Output: Dog barks.
print(animal.sound())  # Output: Animal makes a sound.
```

#### Example 2: Override with super()
```python
class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        super().sound()  # Calls parent method
        print("Dog barks.")

animal = Animal()
dog = Dog()

animal.sound()  
# Output: Animal makes a sound.

dog.sound()
# Output:
# Animal makes a sound.
# Dog barks.
```

#### Example 3: Using __class__.__name__
```python
class Animal:
    def eat(self):
        print(f"{self.__class__.__name__} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.__class__.__name__} is barking.")

bruno = Dog()
dog = Animal()

dog.eat()    # Output: Animal is eating.
bruno.eat()  # Output: Dog is eating.
bruno.bark() # Output: Dog is barking.
```

#### Example 4: Class Override
```python
class Vehicle:
    def start(self):
        print(f"{self.__class__.__name__} is starting.")

class Car(Vehicle):
    def start(self):
        print(f"{self.__class__.__name__} is starting with a roar.")

car = Car()
car.start()  # Output: Car is starting with a roar.
```

### Method Overloading
**Method overloading** is a feature that allows a class to have multiple methods with the same name but different parameter lists.

> **Note in Python:** Python doesn't support traditional method overloading like Java. If you define multiple methods with the same name, the last definition overrides the previous ones.

#### Example
```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):  # This overrides the previous add method
        return a + b + c

calc = Calculator()
# calc.add(2, 3)     # ❌ Error - only the second method exists
print(calc.add(2, 3, 4))  # Output: 9 ✓
```

---

## IS-A and HAS-A Relationships

### IS-A Relationship
The **"IS-A"** relationship describes the relationship between classes in an inheritance hierarchy. It indicates that one class (the subclass) **is a** specialized version of another class (the superclass).

- Implemented through **inheritance**
- Example: `Dog IS-A Animal`

### HAS-A Relationship
The **"HAS-A"** relationship describes a composition or aggregation relationship. It indicates that one class **contains** or **possesses** another class as a part of its structure.

- Implemented through **object composition**
- Example: `Car HAS-A Engine`

### Example: HAS-A Relationship
```python
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # HAS-A relationship

    def start_car(self):
        self.engine.start()     # Delegating to the Engine
        print("Car started.")

car = Car()
car.start_car()
# Output:
# Engine started.
# Car started.
```

---

## Multiple Inheritance

### What is Multiple Inheritance?
**Multiple inheritance** is a feature that allows a class to inherit from **more than one parent class**. This means a subclass can inherit attributes and methods from multiple superclasses, allowing for greater flexibility and code reuse.

### Example 1: Multiple Classes
```python
class Camera:
    def take_photo(self):
        print("Taking a photo.")

class Phone:
    def make_call(self):
        print("Making a call.")

class Smartphone(Camera, Phone):
    pass  # Inherits from both Camera and Phone

phone = Smartphone()
phone.take_photo()  # Output: Taking a photo.
phone.make_call()   # Output: Making a call.
```

### Example 2: Inheritance Properties
```python
class Father:
    def driving(self):
        print(f"{self.__class__.__name__} has programming skills.")

class Mother:
    def painting(self):
        print(f"{self.__class__.__name__} has cooking skills.")

class Child(Father, Mother):
    pass  # Inherits from both Father and Mother

child = Child()
child.driving()   # Output: Child has programming skills.
child.painting()  # Output: Child has cooking skills.
```

---

## Method Resolution Order (MRO)

### What is MRO?
**Method Resolution Order (MRO)** defines the order in which methods are looked up and resolved in a class hierarchy, especially in the context of multiple inheritance. Python uses the **C3 Linearization algorithm** to determine the MRO.

### Understanding MRO
When you call a method on an object, Python searches for it in this order:
1. The instance's class
2. Parent classes according to the MRO

### Example
```python
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
d.show()  # Output: Class B

print(D.mro())
# Output: [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

**MRO Explanation:**
- When `d.show()` is called, Python looks for the `show()` method in this order:
  - `D` → `B` → `C` → `A` → `object`
- Since class `B` has the `show()` method, it is invoked first
- Output: **"Class B"**

### How to View MRO
```python
# Using .mro() method
print(D.mro())

# Using __mro__ attribute
print(D.__mro__)

# Using help() function
help(D)
```

---

## Key Takeaways

✅ **Inheritance** promotes code reusability through parent-child relationships  
✅ **super()** helps call parent class methods while respecting MRO  
✅ **Method Overriding** allows customizing parent class behavior  
✅ **IS-A** (inheritance) vs **HAS-A** (composition) relationships  
✅ **Multiple Inheritance** enables inheriting from multiple parent classes  
✅ **MRO** ensures predictable method resolution order in complex hierarchies
