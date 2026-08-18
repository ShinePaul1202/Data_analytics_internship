# ch="hello"
# m=""
# for i in ch:
#     m=i+m
# print(m)

# #copying a list
# l1=[1,2,3,4,5]
# a=l1.copy()
# print(a)

# import copy
# l2=[1,2,3,4,5]
# b=copy.deepcopy(l2) #deepcopy() creates a new object and recursively adds copies of nested objects found in the original.

# # or

# b=copy.copy(l2) #copy() creates a new object but does not create copies of nested objects, instead it references them.
# print(b)

# #try and except
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# #or

# try:
#     print(10/0)
# except Exception as e:   # This will catch any exception. e is a variable that holds the exception object, which can be used to get more information about the error. expection object is an instance of the Exception class or one of its subclasses.
#     print("An error occurred:", e)
finally:  #finally block is used to execute code that must run regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
    print("This block will always execute, regardless of whether an exception occurred or not.")