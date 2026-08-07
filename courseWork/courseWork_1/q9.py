# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


def fact1(a):
    if a<0:
        print("enter a non-negative no. : ")

    elif a == 0:
        print(1)

    else:
        fact=1
        for i in range(1,a+1):
            fact*=i
        print(fact)

n=int(input("enter the factorial: "))

fact1(n)
