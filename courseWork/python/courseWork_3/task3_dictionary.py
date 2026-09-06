# Write a single Python program named: task3_dictionary.py that performs the following dictionary operations.

# Part A: Sorting a Dictionary by Value
# Given a dictionary with numeric values: Sort the dictionary in ascending order and descending order by value. Display both results clearly.

# Part B: Iterating Through a Dictionary
# Demonstrate how to iterate through a dictionary using for loops:
# Iterate over keys only.
# Iterate over values only.
# Iterate over key-value pairs. Display the results clearly.

# Part C: Merging Dictionaries
# Merge two dictionaries into a single dictionary.

# Requirements:
# 1. If duplicate keys exist, the value from the second dictionary should overwrite the first.
# 2. The program must not crash if one or both dictionaries are empty.

# Part D: Aggregation Operations
# Calculate the sum of all numeric values in a dictionary.
# Calculate the product (multiplication) of all numeric values in a dictionary.

# Requirements:
# 1. Assume values are numeric.
# 2. Handle the case of an empty dictionary appropriately.

# Part E: Sorting by Key
# Sort a dictionary in ascending order by key. Display the sorted result clearly.

# Part F: Removing Duplicates
# Remove duplicate values from a dictionary.
# Clarification:
# Since dictionary keys must be unique, “duplicate” refers to duplicate values.
# If multiple keys share the same value, keep only the first occurrence and remove the others.
# Example:
# Input: {'a': 10, 'b': 20, 'c': 10}
# Output: {'a': 10, 'b': 20}


# Part A: Sorting a Dictionary by Value
def sort_dict_by_value(d):
    sorted_asc = dict(sorted(d.items(), key=lambda item: item[1]))
    sorted_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    return sorted_asc, sorted_desc

# Part B: Iterating Through a Dictionary
def iterate_dict(d):
    keys = []
    values = []
    pairs = []

    for key in d:
        keys.append(key)

    for value in d.values():
        values.append(value)

    for key, value in d.items():
        pairs.append((key, value))

    return keys, values, pairs

# Part C: Merging Dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict 

# Part D: Aggregation Operations
def calculate_sum(d):
    if not d:
        return 0

    return sum(d.values())

def calculate_product(d):
    if not d:
        return 0

    product = 1

    for value in d.values():
        product *= value

    return product

# Part E: Sorting by Key
def sort_dict_by_key(d):
    sorted_dict = dict(sorted(d.items()))
    return sorted_dict

# Part F: Removing Duplicates
def remove_duplicate_values(d):
    unique_dict = {}
    seen_values = set()

    for key, value in d.items():
        if value not in seen_values:
            unique_dict[key] = value
            seen_values.add(value)

    return unique_dict


if __name__ == "__main__":
    # Iterating Through a Dictionary
    input_d=input("Enter dictionary items in the format key1:value1,key2:value2,... : ")
    input_d={k.strip(): float(v.strip()) for k, v in (item.split(':') for item in input_d.split(','))}
    sorted_asc, sorted_desc = sort_dict_by_value(input_d)

    print("Sorted Ascending:", sorted_asc)
    print("Sorted Descending:", sorted_desc)

    # Iterating Through a Dictionary
    input_d1=input("Enter dictionary items in the format key1:value1,key2:value2,... : ")
    input_d1={k.strip(): v.strip() for k, v in (item.split(':') for item in input_d1.split(','))}

    keys, values, pairs = iterate_dict(input_d1)

    print("Keys:", keys)
    print("Values:", values)
    print("Key-Value Pairs:", pairs)

    # Merging Dictionaries
    input_1 = input("Enter the first dictionary in the format key1:value1,key2:value2,... : ")

    if input_1.strip() == "":
        input_1 = {}
    else:
        input_1 = {k.strip(): float(v.strip()) for k, v in (item.split(':') for item in input_1.split(','))}


    input_2 = input("Enter the second dictionary in the format key1:value1,key2:value2,... : ")

    if input_2.strip() == "":
        input_2 = {}
    else:
        input_2 = {k.strip(): float(v.strip()) for k, v in (item.split(':') for item in input_2.split(','))}


    merged_dict = merge_dictionaries(input_1, input_2)

    print("Merged Dictionary:", merged_dict)

    # Aggregation Operations

    input_d4 = input("Enter dictionary items in the format key1:value1,key2:value2,... : ")

    if input_d4.strip() == "":
        input_d4 = {}
    else:
        input_d4 = {k.strip(): float(v.strip()) for k, v in (item.split(':') for item in input_d4.split(','))}

    total = calculate_sum(input_d4)
    product = calculate_product(input_d4)

    print("Sum of values:", total)
    print("Product of values:", product)


    # Sorting by Key
    input_d5 = input("Enter dictionary items in the format key1:value1,key2:value2,... : ")

    if input_d5.strip() == "":
        input_d5 = {}
    else:
        input_d5 = {k.strip(): float(v.strip()) for k, v in (item.split(':') for item in input_d5.split(','))}

    sorted_by_key = sort_dict_by_key(input_d5)

    print("Dictionary Sorted by Key:", sorted_by_key)


    # Removing Duplicates

    input_d6 = input("Enter dictionary items in the format key1:value1,key2:value2,... : ")

    if input_d6.strip() == "":
        input_d6 = {}
    else:
        input_d6 = {k.strip(): float(v.strip()) for k, v in (item.split(':') for item in input_d6.split(','))}

    unique_dict = remove_duplicate_values(input_d6)

    print("Dictionary after removing duplicate values:", unique_dict)


