# Write a Python program named: task2_tuples.py that performs the following tuple operations.

# Part A: Tuple Creation and Access

# 1. Create a tuple containing elements of different data types (e.g., integer, float, string, boolean).
# 2. Create a tuple containing at least five numbers and Print one specific element (choose any valid index).
# 3. Retrieve the 4th element from the end of a given tuple. If the tuple contains fewer than 4 elements, display an appropriate message. The program must not crash.

# Part B: Tuple Modification

# 4. Add an item to an existing tuple. Since tuples are immutable, demonstrate the correct method to achieve this. Do not modify the original tuple directly.

# Part C: Tuple Conversion

# 5. Convert a tuple into a dictionary. If the tuple contains key-value pairs (e.g., ( ("a",1), ("b",2) )), convert directly. If the tuple is a simple sequence of values, convert it into a dictionary where: Keys are the index positions, Values are the tuple elements. The program must clearly handle one of the given approaches.

# Part D: Tuple Transformation in a List
# 6. Given a list of tuples: [(10, 20, 40), (40, 50, 60), (70, 80, 90)], Replace the last element of each tuple with 100.
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# Requirements:
# 1. Do not modify tuples directly (since they are immutable).
# 2. Create updated tuples properly.
# 3. The program must work for tuples of any length (greater than or equal to 1).



# Tuple Creation and Access
def create_mixed_tuple():
    while True:
        try:
            integer_value=int(input("Enter an integer: "))
            float_value=float(input("Enter a float: "))
            string_value=input("Enter a string: ")
            boolean_value=input("Enter a boolean (True/False): ").strip().capitalize()
            if boolean_value not in ['True', 'False']:
                raise ValueError("Invalid boolean value. Please enter True or False")
            else:
                boolean_value = True if boolean_value == 'True' else False
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    return (integer_value, float_value, string_value, boolean_value)

def create_number_tuple():
    while True:
        try:
            numbers = input("Enter at least five numbers separated by spaces: ")
            number_tuple = tuple(float(num) for num in numbers.split())
            if len(number_tuple) < 5:
                raise ValueError("Please enter at least five numbers.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    return number_tuple[0]

def get_fourth_from_end(tup):
    if len(tup)<4:
        return "The tuple must contain at least 4 elements."
    
    return "4th Element from the End: "+tup[-4]


# Tuple Modification
def add_item_to_tuple(tup, item):

    return tup + (item,)


# Tuple Conversion
def convert_tuple_to_dict(tup):
    dict_from_tuple ={key: value for key, value in enumerate(tup)}

    return dict_from_tuple


# Tuple Transformation in a List
def replace_last_element_in_tuples(tuple_list):
    new_lst=[]

    for tup in tuple_list:
        new_lst.append(tup[:-1]+(100,))

    return new_lst



if __name__ == "__main__":
    # Part A: Tuple Creation and Access
    mixed_tuple = create_mixed_tuple()
    print("Mixed Tuple:", mixed_tuple)

    number_tuple = create_number_tuple()
    print("Specific Element from Number Tuple:", number_tuple)

    input_tuple =input("Enter the tuple elements separated by spaces: ")
    input_tuple = tuple(input_tuple.split())
    fourth_from_end = get_fourth_from_end(input_tuple)

    print("Result:", fourth_from_end)

    # Part B: Tuple Modification
    tuple_input = input("Enter a tuple in comma-separated format: ")
    tuple_input = tuple(tuple_input.split(','))
    new_item = input("Enter an item to add to the tuple: ")
    updated_tuple = add_item_to_tuple(tuple_input, new_item)

    print("original Tuple:", tuple_input)
    print("Updated Tuple:", updated_tuple)

    # Part C: Tuple Conversion
    input2= input("Enter a tuple in comma-separated format: ")
    dict_from_tuple = convert_tuple_to_dict(tuple(input2.split(',')))

    print("Dictionary from Tuple:", dict_from_tuple)

    # Part D: Tuple Transformation in a List
    input_list = input("Enter a list of tuples in the format [(10,20,40),(40,50,60),(70,80,90)]: ").strip("[] ").replace(" ", "").split("),(")
    input_list=[tuple(map(int,tuple_item.strip("()").split(","))) for tuple_item in input_list]
    
    print("Updated List of Tuples after changing last ellement to 100:",replace_last_element_in_tuples(input_list))
