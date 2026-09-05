# Write a Python program named: task1_lists.py that performs the following operations on lists.

# Part A: Integer List Operations

# Given a list of integers, implement logic to:
# 1. Multiply all the items in the list.
# 2. Find the largest number in the list.
# 3. Find the smallest number in the list.
# 4. Remove duplicate elements while preserving the original order.
# 5. Check whether the list is empty.
# 6. Find the largest odd number in the list. If no odd numbers exist, print: "No odd numbers found"
# 7. Remove elements at index positions 0, 4, and 5 from the list. Remove only if the index exists. The program must not crash for short lists.

# Part B: Tuple List Sorting
# 8. Given a list of non-empty tuples, sort the list in increasing order based on the last element of each tuple.
# Example:
# Input: [(1, 3), (2, 1), (4, 2)]
# Output: [(2, 1), (4, 2), (1, 3)]

# Part C: Word List Analysis

# 9. Given a list of words, count the total number of lowercase letters across all words in the list.

# Part D: Consecutive Element Extraction

# 10. Given a list of integers and a positive integer k, extract elements that appear exactly k times consecutively. If an element appears more than or fewer than k times consecutively, do NOT include it.
# Example:
# Input : [1, 1, 3, 4, 4, 5, 6, 7]
# k = 2
# Output: [1, 4]



# Integer List Operations

from functools import reduce

def multiply_list(lst):
    if len(lst) == 0:
        return 0

    return reduce(lambda x, y: x * y, lst)
        

def find_largest(lst):
    if len(lst) == 0:
        return None
    return max(lst)

def find_smallest(lst):
    if len(lst) == 0:
        return None
    
    return min(lst)

def remove_duplicates(lst):

    lst_no_duplicates = []

    for item in lst:
        if item not in lst_no_duplicates:
            lst_no_duplicates.append(item)

    return lst_no_duplicates

def is_empty(lst):
    return len(lst) == 0

def find_largest_odd(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    if not odd_numbers:
        return "No odd numbers found"
    return max(odd_numbers)

def remove_elements_at_indices(lst):
    for i in [5,4,0]:
        if i<len(lst):
            lst.pop(i)

    return lst
         
# Tuple List Sorting
def sort_tuples_by_last_element(lst):
    return sorted(lst, key=lambda x: x[-1])

def count_lowercase_letters(words):
    count = 0
    for word in words:
        for char in word:
            if char.islower():
                count += 1
    return count

# Consecutive Element Extraction
def extract_consecutive_elements(lst, k):
    result=[]

    if not lst:
        return result
    
    count=1
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            count+=1

        else:
            if count==k:
                result.append(lst[i])

            count=1

    if count==k:
        result.append(lst[-1])

    return result

 
    
if __name__ == "__main__":

    user_input = input("Enter a list of integers separated by commas: ")

    if user_input.strip() == "":
        nums = []
    else:
        nums = list(map(int, user_input.split(',')))

    print("Product of all items in the list:", multiply_list(nums))

    print("Largest number in the list:", find_largest(nums))

    print("Smallest number in the list:", find_smallest(nums))

    print("List of integers with duplicates removed:", *remove_duplicates(nums))

    print("Is the list empty?", is_empty(nums))

    print("Largest odd number in the list:", find_largest_odd(nums))

    print("After removing elements at indices 0, 4, and 5:", remove_elements_at_indices(nums.copy())) 



# Tuple List Sorting
#-----------------------------------------------------------------------


    tuple_input = input("Enter tuples in the format (1,2),(3,4): ")
    tuples = [tuple(map(int, t.strip('()').split(','))) for t in tuple_input.split('),(')]

    print("Tuples sorted by last element:", sort_tuples_by_last_element(tuples)) 


# Word List Analysis
#------------------------------------------------------------------------

    words_input = input("Enter a list of words separated by commas: ")
    words = [word.strip() for word in words_input.split(',')]

    print("Number of lowercase letters in the list of words:", count_lowercase_letters(words))


# Consecutive Element Extraction
#-----------------------------------------------------------------------

    consecutive_input = input("Enter integers separated by commas for consecutive extraction: ")

    if consecutive_input.strip() == "":
            consecutive_list = []
    else:
        consecutive_list = list(map(int, consecutive_input.split(',')))

    k = int(input("Enter k: "))

    print("Elements appearing exactly k times consecutively:",extract_consecutive_elements(consecutive_list, k))