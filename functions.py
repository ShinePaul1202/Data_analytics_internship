# PYTHON FUNCTIONS AND OOP NOTES
# =============================
#
# Contents
# 1. Strings, lists, copying, and exceptions
# 2. Functional programming: filter, map, and reduce
# 3. Functions as objects and decorators
# 4. Recursion and the call stack
# 5. Generators and yield
# 6. Classes, objects, and attributes
#
# Sections 1-4 contain optional commented examples. Sections 5-6 are active
# demonstrations that run when this file is executed.


# 1. STRINGS, LISTS, COPYING, AND EXCEPTIONS
# ------------------------------------------
# Reverse a string by adding each character to the front.
# # ch="hello"
# # m=""
# # for i in ch:
# #     m=i+m
# # print(m)

# Copying a list.
# # l1=[1,2,3,4,5]
# # a=l1.copy()
# # print(a)

# # import copy
# # l2=[1,2,3,4,5]
# # b=copy.deepcopy(l2) #deepcopy() creates a new object and recursively adds copies of nested objects found in the original.

# # # or

# # b=copy.copy(l2) #copy() creates a new object but does not create copies of nested objects, instead it references them.
# # print(b)

# Handling a specific exception.
# # try:
# #     print(10/0)
# # except ZeroDivisionError:
# #     print("Error: Division by zero is not allowed.")

# Catching a general exception and always running cleanup code.

# try:
#     print(10/0)
# except Exception as e:   # This will catch any exception. e is a variable that holds the exception object, which can be used to get more information about the error. expection object is an instance of the Exception class or one of its subclasses.
#     print("An error occurred:", e)
# finally:  #finally block is used to execute code that must run regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
#     print("This block will always execute, regardless of whether an exception occurred or not.")


# 2. FUNCTIONAL PROGRAMMING
# -------------------------
# filter() selects values, map() transforms values, and reduce() combines
# values into one result.
# from functools import reduce
# prices = [300,600, 800,450,1000,250]
# # total_price =reduce(lambda x, y: x + y, map(lambda x: x*0.9, filter(lambda x: x > 500, prices)))
# # print(total_price)  

# filtered = filter(lambda x: x > 500, prices)
# discounted = map(lambda x: x * 0.9, filtered)
# total = reduce(lambda a, b: a + b, discounted)
# print(total)

# # ============================================================
# 3. FUNCTIONS AS OBJECTS AND DECORATORS
# --------------------------------------
# Calculator example.
# # ============================================================

# def calculater(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "sub":
#         return a - b
#     elif operation == "mul":
#         return a * b
#     elif operation == "div":
#         return a / b
#     else:
#         return "Invalid operation"


# # ============================================================
# Patching the calculator with try-except.
# # ============================================================

# def patch_calculater(a, b, operation):
#     try:
#         v = calculater(a, b, operation)
#         return v
#     except Exception as e:
#         print("An error occurred:", e)


# print(patch_calculater(10, 0, "div"))


# # ============================================================
# A function stored in another variable.
# # ============================================================

# def greet():
#     print("hello")


# my_greet = greet       # Don't use ()
# my_greet()             # Now call the function


# # ============================================================
# Decorator syntax without @.
# # ============================================================

# def my_decorator(func):

#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")

#     return wrapper


# greet = my_decorator(greet)

# greet()


# # ============================================================
# Decorator syntax using @.
# # ============================================================

# def my_decorator(func):

#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")

#     return wrapper


# @my_decorator
# def greet():
#     print("hello")


# greet()


# 4. RECURSION AND THE CALL STACK
# -------------------------------
# A recursive function calls itself and must include a base case.
# def countdown(n):
#     if n <= 0:
#         print("Countdown finished!")
#     else:
#         print(n)
#         countdown(n - 1)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# The call stack tracks active function calls. A call is pushed onto the
# stack, and its information is popped when the function returns.

# Fibonacci series.
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_series = [0, 1]
#         for i in range(2, n):
#             next_number = fib_series[i - 1] + fib_series[i - 2]
#             fib_series.append(next_number)
#         return fib_series


# 5. GENERATORS AND YIELD
# -----------------------
# yield pauses a function, returns one value, and resumes from the same
# position on the next next() call.

# ============================================================
# Generator demonstration.
# ============================================================

def numbers():
    for i in range(1, 6):
        yield i


# Using a generator with a for loop
for num in numbers():
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# Calling next() on a new generator starts at the first value each time.
# ============================================================

print(next(numbers()))
# This will print 1, as it is the first value yielded
# by the generator.

print(next(numbers()))
# This will print 1 again, because a new generator is
# created each time numbers() is called.


# ============================================================
# Storing a generator preserves its state between calls.
# ============================================================

gen = numbers()

print(next(gen))
# This will print 1

print(next(gen))
# This will print 2


# The same generator object (gen) remembers its position.
# Therefore, the next call continues from where it stopped.


# ============================================================
# A generator can yield individual values explicitly.
# ============================================================

def num():
    yield 1
    yield 2
    yield 3


print(next(num()))
# This will print 1

print(next(num()))
# This will print 1 again, because a new generator is
# created each time num() is called.


# ============================================================
# Maintaining generator state.
# ============================================================

gen = num()

print(next(gen))
# This will print 1

print(next(gen))
# This will print 2

print(next(gen))
# This will print 3


# This happens because each time you call num(), a new
# generator object is created.
#
# To maintain the state of the generator, you need to
# store it in a variable (like gen) and use that variable
# to call next().


# ============================================================
# 6. CLASSES, OBJECTS, AND ATTRIBUTES
# -----------------------------------
# A class defines the structure and behavior of objects created from it.
# ============================================================

class student:
    pass


s1 = student()
# s1 is an object of the student class.

print(type(s1))
# Output:
# <class '__main__.student'>

print(s1)
# Output will look something like:
# <__main__.student object at 0x...>


# ============================================================
# Defining __init__ and instance attributes.
# ============================================================

class student:

    def __init__(self, name, age):
        # __init__ is a special method in Python classes.
        # It is automatically called when a new object
        # of the class is created.
        #
        # Its purpose is to initialize the attributes
        # of the object with the values provided during
        # object creation.
        #
        # self refers to the current object.

        self.name = name
        self.age = age


    def display(self):
        # This is called a method.
        # A method is a function defined inside a class.
        #
        # It can access the attributes of the object
        # using self.

        print(f"Name: {self.name}, Age: {self.age}")


# ============================================================
# Creating objects from the class.
# ============================================================

s1 = student("John", 20)
# s1 is an object of the student class.
# s1.name = "John"
# s1.age = 20


s2 = student("Alice", 22)
# s2 is another object of the student class.
# s2.name = "Alice"
# s2.age = 22


# ============================================================
# Calling an instance method.
# ============================================================

s2.display()
# Output:
# Name: Alice, Age: 22


# ============================================================
# Accessing object attributes.
# ============================================================

print(s1.name)
# Output:
# John

print(s2.age)
# Output:
# 22


# ============================================================
# __dict__ contains an object's instance attributes.
# ============================================================

print(s1.__dict__)
# Output:
# {'name': 'John', 'age': 20}

# __dict__ shows the attributes and their values
# stored inside the object.


# ============================================================
# Accessing multiple attributes.
# ============================================================

print(s1.name, s1.age)
# Output:
# John 20


# ============================================================
# CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES
# ============================================================


# ------------------------------------------------------------
# 1. CLASS ATTRIBUTE
# ------------------------------------------------------------

class Student:

    school_name = "ABC School"
    # school_name is a CLASS ATTRIBUTE.
    #
    # It belongs to the class, not to any one particular object.
    # All objects can access the same class attribute.


    # --------------------------------------------------------
    # 2. INSTANCE ATTRIBUTES
    # --------------------------------------------------------

    def __init__(self, name, age):

        self.name = name
        # name is an INSTANCE ATTRIBUTE.
        #
        # Each object gets its own name.

        self.age = age
        # age is also an INSTANCE ATTRIBUTE.
        #
        # Each object gets its own age.


# ------------------------------------------------------------
# 3. CREATING OBJECTS
# ------------------------------------------------------------

s1 = Student("John", 20)

s2 = Student("Alice", 22)


# ------------------------------------------------------------
# 4. ACCESSING INSTANCE ATTRIBUTES
# ------------------------------------------------------------

print(s1.name)
# Output: John

print(s2.name)
# Output: Alice

# s1 and s2 have different name values.
#
# s1.name  → "John"
# s2.name  → "Alice"


# ------------------------------------------------------------
# 5. ACCESSING CLASS ATTRIBUTE
# ------------------------------------------------------------

print(s1.school_name)
# Output: ABC School

print(s2.school_name)
# Output: ABC School

# Both objects can access the same class attribute.
#
# s1.school_name → "ABC School"
# s2.school_name → "ABC School"


# We can also access the class attribute directly
# through the class:

print(Student.school_name)
# Output: ABC School


# ------------------------------------------------------------
# 6. CHANGING CLASS ATTRIBUTE THROUGH AN OBJECT
# ------------------------------------------------------------

s1.school_name = "XYZ School"

# IMPORTANT:
# This does NOT change the class attribute.
#
# Instead, Python creates a NEW INSTANCE ATTRIBUTE
# called school_name specifically for s1.


# ------------------------------------------------------------
# 7. CHECKING THE VALUES
# ------------------------------------------------------------

print(s1.school_name)
# Output: XYZ School

print(s2.school_name)
# Output: ABC School

print(Student.school_name)
# Output: ABC School


# ------------------------------------------------------------
# 8. WHY?
# ------------------------------------------------------------

# Initially:

# Student.school_name
#       ↓
# "ABC School"
#
# s1.school_name → looks at class → "ABC School"
# s2.school_name → looks at class → "ABC School"


# After:

s1.school_name = "XYZ School"

# Now:

# s1 has its own school_name:
#
# s1
# ├── name = "John"
# ├── age = 20
# └── school_name = "XYZ School"
#
#
# s2 does NOT have its own school_name:
#
# s2
# ├── name = "Alice"
# └── age = 22
#
# Therefore s2 uses the class attribute:
#
# Student.school_name → "ABC School"


# ============================================================
# CLASS ATTRIBUTE vs INSTANCE ATTRIBUTE
# ============================================================

# CLASS ATTRIBUTE
# ----------------
# Created inside the class but outside methods.
#
# Example:
#
# class Student:
#     school_name = "ABC School"
#
# Shared by all objects unless an object has its own
# attribute with the same name.


# INSTANCE ATTRIBUTE
# ------------------
# Created using self inside a method, usually __init__.
#
# Example:
#
# self.name = name
# self.age = age
#
# Each object has its own values.


# ============================================================
# SIMPLE DIFFERENCE
# ============================================================

# Class attribute:
#     Student.school_name = "ABC School"
#
# Shared by objects.


# Instance attribute:
#     s1.name = "John"
#     s2.name = "Alice"
#
# Different for each object.


# ============================================================
# IMPORTANT RULE
# ============================================================

# When we write:

s1.school_name

# Python first checks:
#
# 1. Does s1 have its own school_name?
#       ↓
#    YES → use s1's value
#       ↓
#    NO → check the class
#       ↓
#    Student.school_name
#
#
# Therefore:

# Before changing s1.school_name:
#
# s1.school_name → ABC School
#
# After:
#
# s1.school_name → XYZ School
# s2.school_name → ABC School
# Student.school_name → ABC School


# ============================================================
# CLASS METHOD
# ============================================================

class Student:

    # --------------------------------------------------------
    # CLASS ATTRIBUTE
    # --------------------------------------------------------

    school_name = "ABC School"


    # --------------------------------------------------------
    # CLASS METHOD
    # --------------------------------------------------------

    @classmethod   
    def get_school_name(cls):
        #@classmethod is a decorator that indicates that this method is a class method. 
        # and is used to define a method that is bound to the class and not the instance of the class. 
        # It can access class attributes and other class methods, but it cannot access instance attributes or methods.


        # cls refers to the CLASS itself.
        #
        # Here:
        # cls = Student
        #
        # Therefore:
        # cls.school_name
        #
        # is the same as:
        # Student.school_name

        return cls.school_name


# ------------------------------------------------------------
# CALLING THE CLASS METHOD
# ------------------------------------------------------------

print(Student.get_school_name())

# Output:
# ABC School

#----------------------------------------------------------------
#example 1 :
#----------------------------------------------------------------

class student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    s1 = student("John", 20)

    print(s1.introduce())  
    # Output: Hello, my name is John and I am 20 years old.

    print(student.get_school_name())  
    # Output: ABC School

#----------------------------------------------------------------
#example 2 :
#----------------------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, student_string):
        name, age = student_string.split(',')
        return cls(name, int(age))

s1= Student.from_string("John,20")

#explanation of the above code is given below:
    # ============================================================
    # 2. CLASS METHOD: from_string()
    # ============================================================

    @classmethod
    def from_string(cls, student_string):

        # @classmethod makes this a class method.
        #
        # A class method receives the class itself as the first
        # argument.
        #
        # cls refers to the Student class.
        #
        # So here:
        #
        # cls → Student


        # --------------------------------------------------------
        # SPLITTING THE STRING
        # --------------------------------------------------------

        name, age = student_string.split(',')

        # Suppose we call:
        #
        # Student.from_string("John,20")
        #
        # Then:
        #
        # student_string = "John,20"
        #
        # split(',') splits the string wherever there is a comma.
        #
        # "John,20".split(',')
        #
        # gives:
        #
        # ["John", "20"]
        #
        # Therefore:
        #
        # name = "John"
        # age  = "20"
        #
        # Notice that age is still a STRING.


        # --------------------------------------------------------
        # CREATING THE STUDENT OBJECT
        # --------------------------------------------------------

        return cls(name, int(age))

        # int(age) converts:
        #
        # "20" → 20
        #
        # cls refers to Student.
        #
        # Therefore:
        #
        # cls(name, int(age))
        #
        # becomes:
        #
        # Student("John", 20)
        #
        # This creates a new Student object.
        #
        # When Student("John", 20) is executed,
        # __init__() is automatically called.
        #
        # __init__() receives:
        #
        # name = "John"
        # age  = 20
        #
        # and stores:
        #
        # self.name = "John"
        # self.age = 20
        #
        # Finally, return sends this newly created Student
        # object back to where from_string() was called.


    # ============================================================
    # 3. CREATING AN OBJECT USING THE CLASS METHOD
    # ============================================================

    s1 = Student.from_string("John,20")

    # Step 1:
    #
    # Student.from_string("John,20")
    #
    # calls the class method.
    #
    #
    # Step 2:
    #
    # student_string = "John,20"
    #
    #
    # Step 3:
    #
    # "John,20".split(',')
    #
    # gives:
    #
    # ["John", "20"]
    #
    #
    # Step 4:
    #
    # name = "John"
    # age = "20"
    #
    #
    # Step 5:
    #
    # int(age)
    #
    # converts:
    #
    # "20" → 20
    #
    #
    # Step 6:
    #
    # cls(name, int(age))
    #
    # becomes:
    #
    # Student("John", 20)
    #
    #
    # Step 7:
    #
    # A Student object is created.
    #
    # __init__() runs:
    #
    # self.name = "John"
    # self.age = 20
    #
    #
    # Step 8:
    #
    # return sends the Student object back.
    #
    #
    # Step 9:
    #
    # The returned object is stored in s1.
    #
    #
    # So finally:
    #
    # s1
    # ├── name = "John"
    # └── age = 20


print(s1.name)  
# Output: John

print(s1.age)   
# Output: 20


class bank_account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")

account = bank_account(10000)
account.deposit(100)
account.withdraw(50)

print(account.balance) 


#-------------------------------------------------------------
#example 3:
#--------------------------------------------------------------------

class Product:
    category = "electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        return self.price - (self.price * percentage / 100)

    @classmethod
    def get_category(cls):
        return cls.category



# ============================================================
# CLASS CUSTOMIZATION / SPECIAL METHODS
# ============================================================

# Special methods are also called DUNDER methods.
#
# "DUNDER" = Double UNDERscore
#
# Example:
#
# __init__
# __str__
# __len__
# __eq__
# __add__
#
# These methods allow us to customize how Python's built-in
# operations behave with our objects.


# ============================================================
# 1. __init__()
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("John", 20)

print(s1.name)
# Output:
# John

print(s1.age)
# Output:
# 20


# __init__() is automatically called when an object is created.
#
# Student("John", 20)
#       ↓
# __init__(self, name, age)
#       ↓
# self.name = "John"
# self.age = 20
#
# So:
#
# s1.name = "John"
# s1.age = 20


# ============================================================
# 2. __str__()
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"


s1 = Student("John", 20)

print(s1)

# Output:
# Student: John, Age: 20


# __str__() controls what is displayed when we use:
#
# print(object)
#
# When Python sees:
#
# print(s1)
#
# it calls:
#
# s1.__str__()
#
# The returned string is then printed.


# FLOW:
#
# print(s1)
#     ↓
# s1.__str__()
#     ↓
# "Student: John, Age: 20"
#     ↓
# print the string


# ============================================================
# 3. __repr__()
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"


s1 = Student("John", 20)

print(repr(s1))

# Output:
# Student('John', 20)


# __repr__() is mainly used to provide an unambiguous,
# developer-friendly representation of an object.
#
# repr(s1)
#     ↓
# s1.__repr__()
#     ↓
# "Student('John', 20)"


# NOTE:
#
# __str__() → user-friendly representation
#
# __repr__() → developer/debugging representation


# ============================================================
# 4. __len__()
# ============================================================

class Team:

    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team1 = Team(["John", "Alice", "Bob"])

print(len(team1))

# Output:
# 3


# Without __len__(), Python would not know what
# len(team1) should mean.
#
# Because we defined __len__(), Python does:
#
# len(team1)
#     ↓
# team1.__len__()
#     ↓
# len(team1.players)
#     ↓
# 3


# Another example:
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __len__(self):
#         return len(self.name)
#
#
# s1 = Student("John")
#
# print(len(s1))
#
# Output:
# 4
#
# Because:
#
# "John" has 4 characters.


# ============================================================
# 5. __eq__()
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


s1 = Student("John", 20)
s2 = Student("Alice", 22)
s3 = Student("John", 20)

print(s1 == s2)
# Output:
# False

print(s1 == s3)
# Output:
# True


# __eq__() controls what happens when we use:
#
# object1 == object2
#
# When Python sees:
#
# s1 == s3
#
# it calls:
#
# s1.__eq__(s3)
#
# Then it compares:
#
# s1.name == s3.name
# AND
# s1.age == s3.age
#
# "John" == "John" → True
# 20 == 20         → True
#
# Therefore:
#
# True AND True → True


# FLOW:
#
# s1 == s3
#    ↓
# s1.__eq__(s3)
#    ↓
# compare name
#    ↓
# compare age
#    ↓
# True


# ============================================================
# 6. __add__()
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age


s1 = Student("John", 20)
s2 = Student("Alice", 22)

print(s1 + s2)

# Output:
# 42


# __add__() controls what happens when we use:
#
# object1 + object2
#
# When Python sees:
#
# s1 + s2
#
# it calls:
#
# s1.__add__(s2)
#
# Inside __add__():
#
# self.age  → 20
# other.age → 22
#
# Therefore:
#
# 20 + 22
#    ↓
# 42


# FLOW:
#
# s1 + s2
#    ↓
# s1.__add__(s2)
#    ↓
# self.age + other.age
#    ↓
# 20 + 22
#    ↓
# 42


# ============================================================
# 7. __del__()
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Deleting student: {self.name}")


s1 = Student("John")

del s1

# Output:
# Deleting student: John


# __del__() is called when an object is being destroyed.
#
# When we write:
#
# del s1
#
# Python removes the reference to the object.
#
# If the object is no longer referenced, Python can destroy it
# and __del__() may run.
#
# IMPORTANT:
# Do not depend on __del__() for important cleanup because
# Python does not guarantee exactly when it will execute.

