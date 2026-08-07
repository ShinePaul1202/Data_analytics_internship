# Write a Python program to find the median of three values. Median means the middle value after sorting the three numbers.



x=int(input("enter the 1st number: "))
y=int(input("enter the 2nd number: "))
z=int(input("enter the 3rd number: "))

lst=[x,y,z]
lst.sort()

print(lst[1])