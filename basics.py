# print("hello world")
# age=27
# s="hdgKJHDKJVALKSAS"
# print(s.split("V"))
# print(s[-len(s)])
# # %whos is used to get all the details about the variables in the current file. it is only available in jupyter notebook. it will not work in here.


# #BODMAS
# # b - BRACKETS          => () paranethesis, [] square brackets, {} curly brackets
# # o - ORDERS            => ** Exponents
# # d - DIVISION          => / DIVISION, // FLOOR DIVISION, % MODULUS
# # m - MULTIPLICATION    => * MULTIPLICATION
# # a - ADDITION          => + ADDITION
# # s - SUBTRACTION       => - SUBTRACTION


# #RELATIONAL OPERATORS
# # == : EQUAL TO
# # != : NOT EQUAL TO
# # >  : GREATER THAN
# # <  : LESS THAN
# # >= : GREATER THAN OR EQUAL TO
# # <= : LESS THAN OR EQUAL TO

# print(10==10.0)


# #BOOLEAN OPERATORS
# # and : Returns True if both statements are true
# # or : Returns True if one of the statements is true
# # not : Returns True if the statement is false

# #AND operator
# print(10>5 and 10<20) #True

# #OR operator
# print(10>5 or 10<20) #True

# #NOT operator
# print(not(10>5 and 10<20)) #False

#Short circuit

# name = "John"
# if len(name) > 0 and name[0] == "n":
#     print("Name is long and has 'n' at index 5")

#Membership Operators
# in : Returns True if a sequence with the specified value is present in the object
# not in : Returns True if a sequence with the specified value is not present in the object

#identity Operators
# is : Returns True if both variables are the same object
# is not : Returns True if both variables are not the same object


#Lists and Set
#1. Lists are ordered, mutable, and allow duplicate elements. 
# They are defined using square brackets [] or the list() function.
#2. Sets are unordered, mutable, and do not allow duplicate elements. 
# They are defined using curly braces {} or the set() function.     

#list functions =>extend,delete,pop,remove,insert,append,sort,reverse
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



#Example of set functions
# my_set = {1, 2, 3}
# my_set.add(4)  # Adds 4 to the set
# my_set.remove(2)  # Removes 2 from the set
# print(my_set)  # Output: {1, 3, 4}


#set operations
# union() : Returns a set containing all unique elements from both sets
# intersection() : Returns a set containing only the elements that are common to both sets
# difference() : Returns a set containing elements that are in the first set but not in the second set  

#example of set operations
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
# print(set1.intersection(set2))  # Output: {3}
# print(set1.difference(set2))  # Output: {1, 2}

#using operators for set operations
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 | set2)  # Output: {1, 2, 3, 4, 5}
# print(set1 & set2)  # Output: {3}
# print(set1 - set2)  # Output: {1, 2}  



#binary number system
#Binary number system is a base-2 number system that uses only two digits: 0 and 1. 
# Each digit in a binary number is called a bit. The rightmost bit represents 2^0, the next bit to the left represents 2^1, then 2^2, and so on.  

#binary to decimal conversion
#To convert a binary number to decimal, we multiply each bit by its corresponding power of 2 and sum the results. 
# For example, the binary number 1011 can be converted to decimal as follows:
# 1011 in binary is equal to 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 8 + 0 + 2 + 1 = 11 in decimal.

#decimal to binary conversion
#To convert a decimal number to binary, we repeatedly divide the number by 2 and record
#the remainders. The binary representation is obtained by reading the remainders in reverse order.
# For example, to convert the decimal number 13 to binary:


#f-string
# print(f"Hello, my name is {name} and I am {age} years old.")

# number = 100000
# print(f"The number is {number:,}")  # Output: The number is 100,000

# n=i am a title
# print(f"{n.title()}")  # Output: I Am A Title
# print(f"{n.upper()}")  # Output: I AM A TITLE
# print(f"{n.lower()}")  # Output: i am a title
# print(f"{n.capitalize()}")  # Output: I am a title
# print(f"{n.swapcase()}")  # Output: I AM A TITLE


#startswith
# s = "I am a title"
# print(f"{s.startswith('I')}")  # Output: True

#endswith
# print(f"{s.endswith('title')}")  # Output: True

#rstrip and lstrip
# s = "   I am a title   "
# print(f"{s.rstrip()}")  # Output: "   I am a title"
# print(f"{s.lstrip()}")  # Output: "I am a title   "

