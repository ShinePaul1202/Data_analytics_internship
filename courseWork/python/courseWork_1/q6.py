# Write a program to reverse given numbers without slicing. Input will be a positive integer.


n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse)