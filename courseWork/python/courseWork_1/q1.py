# Read an integer N. For all non-negative integers i < N, print i^2 as a list.

n=int(input("Enter a non-negative integer number: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    squares = [i**2 for i in range(n)]
    print(squares)