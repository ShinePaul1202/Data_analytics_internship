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