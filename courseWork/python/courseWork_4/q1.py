import numpy as np


# 1. NumPy Array Creation and Manipulation
# ============================================================

def create_array_a():
    """
    Create a 1D NumPy array of length 10
    containing random integers from 0 to 99.
    """
    return np.random.randint(0, 100, size=10)


def create_array_b():
    """
    Create a 2D NumPy array of shape (3, 4)
    containing random integers from -10 to 10.
    """
    return np.random.randint(-10, 11, size=(3, 4))


def flatten_array_b(b):
    """
    Flatten array b into a 1D array.
    """
    return b.flatten()


def create_array_a_copy(a):
    """
    Create a copy of a and set its first element to -1.
    """
    a_copy = a.copy()
    a_copy[0] = -1
    return a_copy


def create_array_c(a):
    """
    Create an array containing every second element of a,
    starting from index 0.
    """
    return a[::2]



# 2. NumPy Array Indexing and Slicing
# ============================================================

def get_third_element_a(a):
    """
    Return the third element of a.
    """
    return a[2]


def get_last_element_b(b):
    """
    Return the bottom-right (last) element of b.
    """
    return b[-1, -1]


def get_first_two_rows_last_two_columns(b):
    """
    Return the first two rows and last two columns of b.
    """
    return b[:2, -2:]


def get_second_row_b(b):
    """
    Return the second row of b.
    """
    return b[1]


def get_first_column_b(b):
    """
    Return the first column of b.
    """
    return b[:, 0]


# 3. NumPy Array Operations
# ============================================================

def create_array_d():
    """
    Create a 1D NumPy array containing integers from 1 to 10.
    """
    return np.arange(1, 11)


def add_arrays_a_and_d(a, d):
    """
    Add a and d element-wise.
    """
    return a + d


def double_array_b(b):
    """
    Multiply every element of b by 2.
    """
    return b * 2


def matrix_multiplication_b_and_transpose(b, b_double):
    """
    Calculate matrix multiplication of b and transpose of b_double.
    """
    return b @ b_double.T


def calculate_means(a, b, b_double):
    """
    Calculate the mean of a, b, and b_double separately
    and return them as a NumPy array.
    """
    return np.array([
        np.mean(a),
        np.mean(b),
        np.mean(b_double)
    ])



# 4. NumPy Array Aggregation
# ============================================================

def calculate_a_sum(a):
    """
    Calculate the sum of all elements in a.
    """
    return np.sum(a)


def calculate_b_minimum(b):
    """
    Find the minimum element in b.
    """
    return np.min(b)


def calculate_b_double_maximum(b_double):
    """
    Find the maximum element in b_double.
    """
    return np.max(b_double)


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    try:
        # ----------------------------------------------------
        # 1. NumPy Array Creation and Manipulation
        # ----------------------------------------------------

        a = create_array_a()
        print("1.1 Array a:")
        print(a)

        b = create_array_b()
        print("\n1.2 Array b:")
        print(b)

        b_flat = flatten_array_b(b)
        print("\n1.3 Flattened array b_flat:")
        print(b_flat)

        a_copy = create_array_a_copy(a)
        print("\n1.4 Copy of a (a_copy):")
        print(a_copy)

        c = create_array_c(a)
        print("\n1.5 Every second element of a (c):")
        print(c)

        # ----------------------------------------------------
        # 2. NumPy Array Indexing and Slicing
        # ----------------------------------------------------

        third_element = get_third_element_a(a)
        print("\n2.1 Third element of a:")
        print(third_element)

        last_element = get_last_element_b(b)
        print("\n2.2 Last element of b:")
        print(last_element)

        selected_part = get_first_two_rows_last_two_columns(b)
        print("\n2.3 First two rows and last two columns of b:")
        print(selected_part)

        b_row = get_second_row_b(b)
        print("\n2.4 Second row of b (b_row):")
        print(b_row)

        b_col = get_first_column_b(b)
        print("\n2.5 First column of b (b_col):")
        print(b_col)

        # ----------------------------------------------------
        # 3. NumPy Array Operations
        # ----------------------------------------------------

        d = create_array_d()
        print("\n3.1 Array d:")
        print(d)

        e = add_arrays_a_and_d(a, d)
        print("\n3.2 Element-wise addition of a and d (e):")
        print(e)

        b_double = double_array_b(b)
        print("\n3.3 b multiplied by 2 (b_double):")
        print(b_double)

        f = matrix_multiplication_b_and_transpose(b, b_double)
        print("\n3.4 Matrix multiplication of b and b_double.T (f):")
        print(f)

        g = calculate_means(a, b, b_double)
        print("\n3.5 Means of a, b, and b_double (g):")
        print(g)

        # ----------------------------------------------------
        # 4. NumPy Array Aggregation
        # ----------------------------------------------------

        a_sum = calculate_a_sum(a)
        print("\n4.1 Sum of all elements in a (a_sum):")
        print(a_sum)

        b_min = calculate_b_minimum(b)
        print("\n4.2 Minimum element of b (b_min):")
        print(b_min)

        b_double_max = calculate_b_double_maximum(b_double)
        print("\n4.3 Maximum element of b_double (b_double_max):")
        print(b_double_max)

    except ValueError as error:
        print("ValueError occurred:", error)

    except TypeError as error:
        print("TypeError occurred:", error)

    except IndexError as error:
        print("IndexError occurred:", error)

    except Exception as error:
        print("An unexpected error occurred:", error)