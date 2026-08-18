# Write a program to use a loop to display elements from a given list present at an odd index position. Odd index refers to index position (1, 3, 5, …), not odd numbers.



n=input("Enter a integer number: ")
lst=[int(x) for x in n.split(",")]
print(lst[1::2])