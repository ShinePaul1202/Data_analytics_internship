# # ch="hello"
# # m=""
# # for i in ch:
# #     m=i+m
# # print(m)

# # #copying a list
# # l1=[1,2,3,4,5]
# # a=l1.copy()
# # print(a)

# # import copy
# # l2=[1,2,3,4,5]
# # b=copy.deepcopy(l2) #deepcopy() creates a new object and recursively adds copies of nested objects found in the original.

# # # or

# # b=copy.copy(l2) #copy() creates a new object but does not create copies of nested objects, instead it references them.
# # print(b)

# # #try and except
# # try:
# #     print(10/0)
# # except ZeroDivisionError:
# #     print("Error: Division by zero is not allowed.")

# # #or

# try:
#     print(10/0)
# except Exception as e:   # This will catch any exception. e is a variable that holds the exception object, which can be used to get more information about the error. expection object is an instance of the Exception class or one of its subclasses.
#     print("An error occurred:", e)
# finally:  #finally block is used to execute code that must run regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
#     print("This block will always execute, regardless of whether an exception occurred or not.")


# from functools import reduce
# prices = [300,600, 800,450,1000,250]
# # total_price =reduce(lambda x, y: x + y, map(lambda x: x*0.9, filter(lambda x: x > 500, prices)))
# # print(total_price)  

# filtered = filter(lambda x: x > 500, prices)
# discounted = map(lambda x: x * 0.9, filtered)
# total = reduce(lambda a, b: a + b, discounted)
# print(total)

# # ============================================================
# # 1. CALCULATOR
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
# # 2. PATCHING THE CALCULATOR USING try-except
# # ============================================================

# def patch_calculater(a, b, operation):
#     try:
#         v = calculater(a, b, operation)
#         return v
#     except Exception as e:
#         print("An error occurred:", e)


# print(patch_calculater(10, 0, "div"))


# # ============================================================
# # 3. FUNCTION AS AN OBJECT
# # ============================================================

# def greet():
#     print("hello")


# my_greet = greet       # Don't use ()
# my_greet()             # Now call the function


# # ============================================================
# # 4. DECORATOR WITHOUT @
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
# # 5. DECORATOR USING @
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


# #recursion
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

#call stack -> it is a data structure that keeps track of function calls in a program. When a function is called, its information (such as local variables and return address) is pushed onto the stack. When the function returns, its information is popped off the stack.

#fibanocci series
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            next_number = fib_series[i - 1] + fib_series[i - 2]
            fib_series.append(next_number)
        return fib_series