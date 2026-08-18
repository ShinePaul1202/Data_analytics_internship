# Write a program to calculate the sum of series up to n term.
# For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. This series is formed by appending the digit 2 in each term.


n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    c="2"*i
    num=int(c)
    sum+=num
print(sum)

