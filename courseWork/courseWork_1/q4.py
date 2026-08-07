# Write a program to count the total number of digits in a number using a while loop.


n=int(input("enter a number: "))

count=0
while n>0:
    count+=1
    n//=10

print(count)

