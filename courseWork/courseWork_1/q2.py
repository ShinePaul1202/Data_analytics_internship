# You have been given a string. You need to remove all the duplicates from the string. The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can traverse the string only once.


n=input("enter a string: ")

result = ""
for i in n:

    if i not in result:
        result += i

print(result)
