# Write a program to display only those numbers from a list that satisfy the following conditions:

# The number must be divisible by 5
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop


n=input("enter a list of numbers separated by commas: ")

lst = [int(x) for x in n.split(",")]

if len(lst) == 0:
    print("The list is empty.")

elif len(lst) >= 1:
    result = []

    for num in lst:

        if num > 500:
            break
        if num > 150:
            continue
        if num % 5 == 0:
            result.append(num)

    print(result)
