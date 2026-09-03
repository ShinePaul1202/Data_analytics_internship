# PYTHON BASICS NOTES
# ==================
#
# Contents
# 1. Basic syntax, variables, and expressions
# 2. Operators and short-circuit evaluation
# 3. Lists, sets, and set operations
# 4. Binary and decimal number systems
# 5. String formatting and methods
# 6. Itertools and built-in iteration helpers
# 7. Evaluating expressions


# 1. BASIC SYNTAX, VARIABLES, AND EXPRESSIONS
# --------------------------------------------
# print("hello world")
# age=27
# s="hdgKJHDKJVALKSAS"
# print(s.split("V"))
# print(s[-len(s)])
# # %whos is used to get all the details about the variables in the current file. it is only available in jupyter notebook. it will not work in here.


# 2. OPERATORS AND SHORT-CIRCUIT EVALUATION
# -----------------------------------------
# BODMAS describes the order in which arithmetic expressions are evaluated.
# # b - BRACKETS          => () paranethesis, [] square brackets, {} curly brackets
# # o - ORDERS            => ** Exponents
# # d - DIVISION          => / DIVISION, // FLOOR DIVISION, % MODULUS
# # m - MULTIPLICATION    => * MULTIPLICATION
# # a - ADDITION          => + ADDITION
# # s - SUBTRACTION       => - SUBTRACTION


# Relational operators compare two values and return True or False.
# # == : EQUAL TO
# # != : NOT EQUAL TO
# # >  : GREATER THAN
# # <  : LESS THAN
# # >= : GREATER THAN OR EQUAL TO
# # <= : LESS THAN OR EQUAL TO

# print(10==10.0)


# Boolean operators combine or invert conditions.
# # and : Returns True if both statements are true
# # or : Returns True if one of the statements is true
# # not : Returns True if the statement is false

# #AND operator
# print(10>5 and 10<20) #True

# #OR operator
# print(10>5 or 10<20) #True

# #NOT operator
# print(not(10>5 and 10<20)) #False

# Short-circuit evaluation stops as soon as the final result is known.

# name = "John"
# if len(name) > 0 and name[0] == "n":
#     print("Name is long and has 'n' at index 5")

# Membership operators test whether a value exists in a sequence.
# in : Returns True if a sequence with the specified value is present in the object
# not in : Returns True if a sequence with the specified value is not present in the object

# Identity operators test whether two names refer to the same object.
# is : Returns True if both variables are the same object
# is not : Returns True if both variables are not the same object


# 3. LISTS, SETS, AND SET OPERATIONS
# ----------------------------------
# Lists are ordered and mutable; sets are unordered, mutable, and unique.
#1. Lists are ordered, mutable, and allow duplicate elements. 
# They are defined using square brackets [] or the list() function.
#2. Sets are unordered, mutable, and do not allow duplicate elements. 
# They are defined using curly braces {} or the set() function.     

# Common list operations: extend, delete, pop, remove, insert, append,
# sort, and reverse.
#Example of list functions
# my_list = [1, 2, 3]
# my_list.append(4)  # Adds 4 to the end of the list
#del my_list[0]  # Deletes the element at index 0
#del my_list[1:3]  # Deletes elements from index 1 to 2
#del my_list # Deletes the entire list
#my_list.extend([5, 6])  # Adds multiple elements to the end of the list
#extended_list = [7, 8]
# extended_list.extend(my_list[1:3])  # Adds elements from my_list to extended_list
#extended_list.extend(my_list)  # Adds all elements from my_list to extended_list
#my_list.pop(1)  # Removes the element at index 1
# my_list.insert(1, 1.5)  # Inserts 1.5 at index 1
# my_list.remove(2)  # Removes the first occurrence of 2
# my_list.pop()  # Removes and returns the last item
# my_list.sort()  # Sorts the list in ascending order
#my_list.sort(reverse=True)  # Sorts the list in descending order
# my_list.reverse()  # Reverses the list
# print(my_list)  # Output: [1, 1.5, 3, 4]



# Set methods example.
# my_set = {1, 2, 3}
# my_set.add(4)  # Adds 4 to the set
# my_set.remove(2)  # Removes 2 from the set
# print(my_set)  # Output: {1, 3, 4}


# Set operations: union, intersection, and difference.
# union() : Returns a set containing all unique elements from both sets
# intersection() : Returns a set containing only the elements that are common to both sets
# difference() : Returns a set containing elements that are in the first set but not in the second set  

# Set operations example.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
# print(set1.intersection(set2))  # Output: {3}
# print(set1.difference(set2))  # Output: {1, 2}

# Set operations can also use |, &, and - operators.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 | set2)  # Output: {1, 2, 3, 4, 5}
# print(set1 & set2)  # Output: {3}
# print(set1 - set2)  # Output: {1, 2}  



# 4. BINARY AND DECIMAL NUMBER SYSTEMS
# -------------------------------------
# Binary is base 2 and uses only the digits 0 and 1.
#Binary number system is a base-2 number system that uses only two digits: 0 and 1. 
# Each digit in a binary number is called a bit. The rightmost bit represents 2^0, the next bit to the left represents 2^1, then 2^2, and so on.  

# Binary to decimal conversion.
#To convert a binary number to decimal, we multiply each bit by its corresponding power of 2 and sum the results. 
# For example, the binary number 1011 can be converted to decimal as follows:
# 1011 in binary is equal to 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 8 + 0 + 2 + 1 = 11 in decimal.

# Decimal to binary conversion.
#To convert a decimal number to binary, we repeatedly divide the number by 2 and record
#the remainders. The binary representation is obtained by reading the remainders in reverse order.
# For example, to convert the decimal number 13 to binary:


# 5. STRING FORMATTING AND METHODS
# --------------------------------
# f-strings insert expressions directly into a string.
# print(f"Hello, my name is {name} and I am {age} years old.")

# number = 100000
# print(f"The number is {number:,}")  # Output: The number is 100,000

# n=i am a title
# print(f"{n.title()}")  # Output: I Am A Title
# print(f"{n.upper()}")  # Output: I AM A TITLE
# print(f"{n.lower()}")  # Output: i am a title
# print(f"{n.capitalize()}")  # Output: I am a title
# print(f"{n.swapcase()}")  # Output: I AM A TITLE


# startswith() checks the beginning of a string.
# s = "I am a title"
# print(f"{s.startswith('I')}")  # Output: True

# endswith() checks the end of a string.
# print(f"{s.endswith('title')}")  # Output: True

# rstrip() and lstrip() remove whitespace from one side of a string.
# s = "   I am a title   "
# print(f"{s.rstrip()}")  # Output: "   I am a title"
# print(f"{s.lstrip()}")  # Output: "I am a title   "



# Chaining methods applies multiple string operations in sequence.

# 6. ITERTOOLS AND BUILT-IN ITERATION HELPERS
# -------------------------------------------
# itertools provides efficient, lazy tools for working with iterables.
#a=(1,2,3,4,5)
# for i in a:
#     print(i)
# import itertools
# for pair in itertools.combinations(a, 2):
#     print(pair)  #output: (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)
# print(list(itertools.permutations(a, 2)))  #output: [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]    

# from itertools import product
# size=["small","medium","large"]
# flavours=["chocolate","vanilla","strawberry"]
# for i in product(size, flavours):
#     print(i)  #output: ('small', 'chocolate'), ('small', 'vanilla'), ('small', 'strawberry'), ('medium', 'chocolate'), ('medium', 'vanilla'), ('medium', 'strawberry'), ('large', 'chocolate'), ('large', 'vanilla'), ('large', 'strawberry')

# Product combinations summary:
# The code demonstrates the use of itertools.product to generate all possible combinations of size and flavour for a product catalog.and it understands

# from itertools import chain
# results=chain(size, flavours)
# for x in results:
#     print(x)  #output: small, medium, large, chocolate, vanilla, strawberry 

# from itertools import islice
# # Example of islice
# numbers=range(1000000)
# first_ten_numbers=islice(numbers, 10) # Get the first 10 numbers. numbers is an iterable that generates numbers from 0 to 999999. islice takes the first 10 numbers from this iterable and returns an iterator. We can convert this iterator to a list to see the first 10 numbers.
# print(list(first_ten_numbers))  #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# def batch(iterable, size):
#     """Batch data into tuples of a specified size."""
#     it = iter(iterable)
#     while batch := tuple(itertools.islice(it, size)):
#         yield batch

data = range(10)
# for batch_data in batch(data, 3):
#     print(batch_data)  #output: (0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)

# The walrus operator (:=) assigns a value as part of an expression.


# enumerate() returns index-value pairs for an iterable. The index starts at 0
# by default, or at a value supplied with start=.
 
# restaurant_menu = ["Pizza", "Burger", "Pasta", "Salad"]
# for i, restaurant_menu in enumerate(restaurant_menu, start=1): 
#     print(f"{i}. {restaurant_menu}")  #output: 1. Pizza, 2. Burger, 3. Pasta, 4. Salad


# zip() combines values at matching positions and stops at the shortest input.
# restaurant_menu = ["Pizza", "Burger", "Pasta", "Salad"]
# ratings = [4.5, 4.0, 4.2, 3.8]
# for item, rating in zip(restaurant_menu, ratings):
#     print(f"{item}: {rating}")  #output: Pizza: 4.5, Burger: 4.0, Pasta: 4.2, Salad: 3.8


# restaurant_menu = ["Pizza", "Burger", "Pasta", "Salad"]
# ratings = [4.5, 4.0, 4.2, 3.8]
# cities = ["New York", "Los Angeles", "Chicago"]
# for item, rating, city in zip(restaurant_menu, ratings, cities):
#     print(f"{item}: {rating} ({city})")  #output: Pizza: 4.5 (New York), Burger: 4.0 (Los Angeles), Pasta: 4.2 (Chicago)


# 7. EVALUATING EXPRESSIONS
# -------------------------
# eval() evaluates a string as a Python expression. Never use it with
# untrusted input because it can execute arbitrary code.
# exp="2 + 3 * 4"
# result = eval(exp)
# print(result)  #output: 14

eval("10 + 20")  #output: 30


