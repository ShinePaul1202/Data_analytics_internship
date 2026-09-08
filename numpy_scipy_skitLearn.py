
#----------------------------------------
#numpy
# ----------------------------------------

# numpy is a powerful library for numerical computing in Python.
#  It provides support for large, multi-dimensional arrays and matrices,
#  along with a collection of mathematical functions to operate on these arrays efficiently.
# sucha as mean, median, standard deviation, and more. 

import numpy as np # importing the numpy library and giving it an alias 'np' for convenience.

print(np.__version__)  # Output: 1.21.0 (or the version you have installed)


num_lst=[1, 2, 3, 4, 5]  # A list of numbers.
num_array=np.array([1, 2, 3, 4, 5])  # Creating a NumPy array from the list.

print("lst:",num_lst) 
 # Output: lst: [1, 2, 3, 4, 5]
print("array:",num_array)  
# Output: array: [1 2 3 4 5]

print(num_array+10) # Adding 10 to each element in the array
# Output: [11 12 13 14 15]
print(num_array*2) # Multiplying each element in the array by 2
# Output: [ 2  4  6  8 10]

zero_1=np.zeros((2, 3))  # Creating a 2x3 array filled with zeros.
zero_2=np.zeros(5) # Creating a 1D array of length 5 filled with zeros.
ones=np.ones(5) # Creating a 1D array of length 5 filled with ones.
full=np.full((2, 3), 7) # Creating a 2x3 array filled with the value 7.
full2=np.full(5, 9) # Creating a 1D array of length 5 filled with the value 9.
sequnce=np.arange(0, 10, 2) # Creating an array with values from 0 to 10 (exclusive) with a step of 2.
evenly_spaced=np.linspace(0, 1, 5) # Creating an array of 5 evenly spaced values between 0 and 1.

print("zero1",zero_1)
# output: zero1 [[0. 0. 0.]
#                 [0. 0. 0.]]
print("zero2",zero_2)
#output: zero2 [0. 0. 0. 0. 0.]
print("ones",ones)
#output: ones [1. 1. 1. 1. 1.]
print("full",full)
# output: full [[7 7 7]
#              [7 7 7]]
print("full2",full2)
#output: full2 [9 9 9 9 9]
print("sequence",sequnce)
#output: sequence [0 2 4 6 8]
print("evenly_spaced",evenly_spaced)
#output: evenly_spaced [0.   0.25 0.5  0.75 1.  ]


# one dimensinal array and two dimensional array
#-------------------------------------------------------
# one dimensinal array and two dimensional array both are created using numpy.array() function. 
# one dimensional array is created by passing a list
# two dimensional array is created by passing a list of lists.
one_d_array=np.array([1, 2, 3, 4, 5]) # Creating a one-dimensional array.
matrix=np.array([[1, 2, 3], [4, 5, 6]]) # Creating a two-dimensional array.it is called matrix.

print("one_d_array:",one_d_array)
print("matrix:",matrix)

print("matrix shape:",matrix.shape)  
# Output: (2, 3)  # Shape of the matrix (2 rows, 3 columns)
print("no of elements:",matrix.size)
# Output: 6  # Total number of elements in the matrix
print("matrix data type:",matrix.dtype)
# Output: int64 (or the data type of the elements in the matrix)
print("matrix dimension:",matrix.ndim)
# Output: 2  # Number of dimensions of the matrix


#indexing and slicing
#----------------------------------------
print("first element of one_d_array:",one_d_array[0])
# Output: 1  # Accessing the first element of the one-dimensional array.

print("first row of matrix:",matrix[0])
# Output: [1 2 3]  # Accessing the first row of the two-dimensional array (matrix).
print("first element of first row of matrix:",matrix[0][0])
# Output: 1  # Accessing the first element of the first row of the matrix.


print("first two elements of one_d_array:",one_d_array[1:3])
# Output: [2 3]  # Accessing the first two elements of the one-dimensional array.
print("last two elements of one_d_array:",one_d_array[-2:])
# Output: [4 5]  # Accessing the last two elements of the one-dimensional array.
print("first two rows of one_d_array:",one_d_array[:2])
#output: [1 2]  # Accessing the first two elements of the one-dimensional array.
print("every second element of one_d_array:",one_d_array[::2])
# Output: [1 3 5]  # Accessing every second element of the one-dimensional array.

print("first two rows of matrix:",matrix[0:2])
# Output: [[1 2 3]
#          [4 5 6]]  # Accessing the first two rows of the two-dimensional array (matrix).

data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Creating a two-dimensional array (matrix).
print("first two rows and first two columns of data:",data[0:2,0:2])
# Output: [[1 2]
#          [4 5]]
print("every second row and every second column of data:",data[::2,::2])
# Output: [[1 3]
#          [7 9]]
print("last two rows and last two columns of data:",data[-2:,-2:])
# Output: [[5 6]
#          [8 9]]
print("first row and last two columns of data:",data[0,-2:])
# Output: [2 3]
print("first row",data[0,:])
print("first column",data[:,0])
print("second row",data[1,:])
print("second column",data[:,1])
print("last row",data[-1,:])
print("last column",data[:,-1])



#reshaping arrays
#----------------------------------------
arr=np.array([1, 2, 3, 4, 5, 6]) # Creating a one-dimensional array.
reshaped_arr=arr.reshape((2, 3)) # Reshaping the one-dimensional array into a two-dimensional array with 2 rows and 3 columns.
reshaped_arr2=arr.reshape((3, 2)) # Reshaping the one-dimensional array into a two-dimensional array with 3 rows and 2 columns.
print("original_arr:",arr)
print("reshaped_arr:",reshaped_arr)
print("reshaped_arr2:",reshaped_arr2)



#flattening and transposing 
#----------------------------------------
print("original matrix:",matrix)
print("transposed matrix:",matrix.T)  # Transposing the two-dimensional array (matrix)
# Output: [[1 4]
#          [2 5]]
print("flattened matrix:",matrix.flatten())  # Flattening the two-dimensional array (matrix) into a one-dimensional array.
#output: flattened matrix: [1 2 3 4 5 6]


#joining arrays
#------------------------------------------------
a_arr=np.array([1, 2, 3])
b_arr=np.array([4, 5, 6])

combined_array=np.concatenate((a_arr, b_arr))  # Concatenating two one-dimensional arrays.
print("combined_array:",combined_array)
# Output: combined_array: [1 2 3 4 5 6]

print("added_array:",np.add(a_arr, b_arr))  # Adding two one-dimensional arrays element-wise.
print(added_array :=np.add(a_arr, b_arr))  # Adding two one-dimensional arrays element-wise.
# Output:  [5 7 9]

# := is the walrus operator, which allows you to assign a value to a variable as part
#  of an expression. it can be used to simplify code and make it more readable by reducing
#  the number of lines needed for variable assignment. and can be used in situations
#  where you want to use a value immediately after assigning it, and can be used
#  afterwards in the code.



a_matrix=np.array([[1, 2], [3, 4]])
b_matrix=np.array([[5, 6], [7, 8]])

combined_matrix=np.concatenate((a_matrix, b_matrix), axis=0)  # Concatenating two two-dimensional arrays (matrices) along rows.
print("combined_matrix along rows:",combined_matrix)
# Output: combined_matrix along rows: [[1 2]
#                                      [3 4]
#                                      [5 6]
#                                      [7 8]]


combined_matrix_cols=np.concatenate((a_matrix, b_matrix), axis=1)  # Concatenating two two-dimensional arrays (matrices) along columns.
print("combined_matrix along columns:",combined_matrix_cols)
# Output: combined_matrix along columns: [[1 2 5 6]
#                                        [3 4 7 8]]

print("added_matrix:",np.add(a_matrix, b_matrix))  # Adding two two-dimensional arrays (matrices) element-wise.
# Output: added_matrix: [[ 6  8]
#                        [10 12]]
print("vertical_stack:",np.vstack((a_matrix, b_matrix)))  # Stacking two two-dimensional arrays (matrices) vertically.
# Output: vertical_stack: [[1 2]
#                          [3 4]
#                          [5 6]
#                          [7 8]]
print("horizontal_stack:",np.hstack((a_matrix, b_matrix)))  # Stacking two two-dimensional arrays (matrices) horizontally.
# Output: horizontal_stack: [[1 2 5 6]
#                            [3 4 7 8]]



#mathematical operations
#----------------------------------------
marks=np.array([80, 90, 70, 85, 95])  # Creating a one-dimensional array of marks.
print("mean:",np.mean(marks))  # Calculating the mean of the marks.
# Output: mean: 84.0
print("median:",np.median(marks))  # Calculating the median of the marks.
# Output: median: 85.0
print("standard deviation:",np.std(marks))  # Calculating the standard deviation of the marks.
# Output: standard deviation: 8.94427190999916
print("sum:",np.sum(marks))  # Calculating the sum of the marks.
# Output: sum: 420
print("maximum:",np.max(marks))  # Finding the maximum mark.
# Output: maximum: 95
print("minimum:",np.min(marks))  # Finding the minimum mark.
# Output: minimum: 70



#element-wise operations
#----------------------------------------
#element-wise operations are performed on each element of the array individually.
arr1=np.array([1, 2, 3])

arr2=np.array([4, 5, 6])

print("Element-wise multiplication:",np.multiply(arr1, arr2))  # Element-wise multiplication of two arrays.
# Output: Element-wise multiplication: [ 4 10 18]
print("Element-wise addition:",np.add(arr1, arr2))  # Element-wise addition of two arrays.
# Output: Element-wise addition: [5 7 9]
print("Element-wise subtraction:",np.subtract(arr1, arr2))  # Element-wise subtraction of two arrays.
# Output: Element-wise subtraction: [-3 -3 -3]
print("Element-wise division:",np.divide(arr1, arr2))  # Element-wise division of two arrays.
# Output: Element-wise division: [0.25 0.4 0.5]

print("Element-wise power:",np.power(arr1, arr2))  # Element-wise exponentiation of two arrays.
# Output: Element-wise power: [  1  32 729]
print("Element-wise square root:",np.sqrt(arr1))  # Element-wise square root of an array.
# Output: Element-wise square root: [1.         1.41421356 1.73205081]
print("Element-wise logarithm:",np.log(arr1))  # Element-wise natural logarithm of an array.
# Output: Element-wise logarithm: [0.         0.69314718 1.09861229]
print("squares of arr1:",np.power(arr1, 2))  # Element-wise squaring of an array.
# Output: squares of arr1: [1 4 9]
print("square of arr1:",np.square(arr1))  # Element-wise squaring of an array.
# Output: square of arr1: [1 4 9]



# Broadcasting
#----------------------------------------
# Broadcasting is a powerful feature in NumPy that allows for operations between 
# arrays of different shapes. this  means expansion of the smaller array to match 
# the shape of the larger array without making copies of data.

prices=np.array([100, 200, 300])  # Creating a one-dimensional array of prices.
discounts=20
final_prices=prices-discounts  # Broadcasting the scalar discount to each element of the prices array.
print("final_prices:",final_prices)
# Output: final_prices: [ 80 180 280]

#boolean indexing
#----------------------------------------
# Boolean indexing is a technique in NumPy that allows you to select elements from an array.

marks=np.array([20, 30, 40, 50, 60])  # Creating a one-dimensional array of marks.
passsed=marks>40  # Creating a boolean array where each element indicates whether the corresponding mark is greater than 40.
print("passsed:",passsed)
# Output: passsed: [False False False  True  True]

passed_marks=marks[passsed]  # Using boolean indexing to select marks that are greater than 40.
print("passed_marks:",passed_marks)
# Output: passed_marks: [50 60]

# OR

passed_marks2=marks[marks>40]  # Using boolean indexing directly to select marks that are greater than 40.
print("passed_marks2:",passed_marks2)
# Output: passed_marks2: [50 60]


print("Positions of marks greater than 40:",np.where(marks>40))  # Finding the indices of marks that are greater than 40.
# Output: Positions of marks greater than 40: (array([3, 4]),)
print("Positions of marks greater than 40:",np.argwhere(marks>40))  # Finding the indices of marks that are greater than 40.
# Output: Positions of marks greater than 40: [[3]
#         [4]]
print("Positions of maximum marks:",np.argmax(marks))  # Finding the index of the maximum mark.
# Output: Positions of maximum marks: 4
print("Positions of minimum marks:",np.argmin(marks))  # Finding the index of the minimum mark.
# Output: Positions of minimum marks: 0
print("unique elements in marks:",np.unique(marks))  # Finding the unique elements in the marks array.
# Output: unique elements in marks: [20 30 40 50 60]


#basic linear algebra operations with numpy
#----------------------------------------
# NumPy provides a set of functions for performing basic linear algebra operations
#  on arrays and matrices.

A=np.array([[1, 2], [3, 4]])  # Creating a two-dimensional array (matrix) A.
B=np.array([[5, 6], [7, 8]])  # Creating a two-dimensional array (matrix) B.
print("Matrix A:\n",A)
print("Matrix B:\n",B)

print("Matrix multiplication of A and B:\n",np.dot(A, B))  # Performing matrix multiplication of A and B.
# Output: Matrix multiplication of A and B: [[19 22]
#                                      [43 50]]
print("Matrix multiplication of A and B using @ operator:\n",A@B)  # Performing matrix multiplication of A and B using the @ operator.
# Output: Matrix multiplication of A and B using @ operator: [[19 22]
#                                                      [43 50]]
print("Determinant of A:",np.linalg.det(A))  # Calculating the determinant of matrix A.
# Output: Determinant of A: -2.0000000000000004
print("Inverse of A:\n",np.linalg.inv(A))  # Calculating the inverse of matrix A.
# Output: Inverse of A: [[-2.   1. ]
#                      [ 1.5 -0.5]]
print("Eigenvalues and Eigenvectors of A:\n",np.linalg.eig(A))  # Calculating the eigenvalues and eigenvectors of matrix A.
# Output: Eigenvalues and Eigenvectors of A: (array([-0.37228132,  5.37228132]), array([[-0.82456484, -0.41597356],
#        [ 0.56576746, -0.90937671]]))
print("transpose of A:\n",np.transpose(A))  # Calculating the transpose of matrix A.
# Output: transpose of A: [[1 3]
#                      [2 4]]
print("Transpose of A using .T:\n",A.T)  # Calculating the transpose of matrix A using the .T attribute.
# Output: Transpose of A using .T: [[1 3]
#                               [2 4]]




# HW problem
marks=np.array([55,72,91,43,88,67,95,38])
print("marks: ", marks)
print("average:",  np.mean(marks))
print("median:", np.median(marks))
print("highest marks:", np.max(marks))
print("lowest marks:", np.min(marks))
print("marks greater than 70:", marks[marks>70])
print("position of highest marks:", np.argmax(marks))



#------------------------------------------
#Scipy
# ----------------------------------------

# Scipy is a library for scientific and technical computing in Python.
#  It builds on NumPy and provides additional functionality for optimization, 
#  integration, interpolation, and other scientific computing tasks.
# it includes linear algebra, signal processing, image processing, temporal analysis, and more.

import scipy # importing the scipy library.

scipy.__version__  # Output: 1.7.0 (or the version you have installed)


#scientific constants
#----------------------------------------
from scipy import constants # importing the constants module from the scipy library.
print("Speed of light in vacuum (m/s):", constants.c)  # Speed of light in vacuum in meters per second.
# Output: Speed of light in vacuum (m/s): 299792458.0
print("Gravitational constant (m^3 kg^-1 s^-2):", constants.G)  # Gravitational constant in m^3 kg^-1 s^-2.
# Output: Gravitational constant (m^3 kg^-1 s^-2): 6.67430e-11
print("Planck's constant (J s):", constants.h)  # Planck's constant in joule-seconds.
# Output: Planck's constant (J s): 6.62607015e-34
print("pi:", constants.pi)  # Value of pi.
# Output: pi: 3.141592653589793

#units conversion
#----------------------------------------

from scipy.constants import convert_temperature # importing the convert_temperature function from the scipy.constants module.
temp_celsius = 25  # Temperature in Celsius.
print("Temperature in Celsius:", temp_celsius)

print("Temperature in Kelvin:", convert_temperature(temp_celsius, 'C', 'K'))  # Converting temperature from Celsius to Kelvin.
print("Temperature in Fahrenheit:", convert_temperature(temp_celsius, 'C', 'F'))  # Converting temperature from Celsius to Fahrenheit.
# Output: Temperature in Kelvin: 298.15
# Output: Temperature in Fahrenheit: 77.0

# OR

print("Temperature in Kelvin:", convert_temperature(temp_celsius, 'Celsius', 'Kelvin'))  # Converting temperature from Celsius to Kelvin using full names.
print("Temperature in Fahrenheit:", convert_temperature(temp_celsius, 'Celsius', 'Fahrenheit'))  # Converting temperature from Celsius to Fahrenheit using full names.
# Output: Temperature in Kelvin: 298.15
# Output: Temperature in Fahrenheit: 77.0


# integration
#----------------------------------------
# Integration is a mathematical operation that calculates the area under a curve or the accumulation of quantities over an interval.

from scipy.integrate import quad # importing the quad function from the scipy.integrate module.

def integrand(x):  # Defining a function to be integrated.
    return x**2  # The function returns the square of x.

result, error = quad(integrand, 0, 3)  # Integrating the function from 0 to 3.
print("Result of integration:", result)
print("Estimated error:", error)
# Output: Result of integration: 9.0
# Output: Estimated error: 9.992007221626409e-14

#Optimization
#----------------------------------------
# Optimization is the process of finding the best solution to a problem by minimizing or maximizing an objective function.
from scipy.optimize import minimize # importing the minimize function from the scipy.optimize module.

def objective_function(x):  # Defining an objective function to be minimized.
    return (x-3)**2 + 2   # The function returns a quadratic expression.

result = minimize(objective_function, x0=[0])  # Minimizing the objective function starting from x=0.
print("Minimum value:", result.fun)
print("Optimal x:", result.x)
# Output: Minimum value: 2.0
# Output: Optimal x: [3.]


# root finding
#----------------------------------------
# Root finding is a numerical method used to find the values of x for which a given function f(x) equals zero.
from scipy.optimize import root_scalar # importing the root_scalar function from the scipy.optimize module.

def f(x):  # Defining a function for which we want to find the root.
    return x**2 - 4  # The function returns x^2 - 4.

solution = root_scalar(f, bracket=[0, 3])  # Finding the root of the function in the interval [0, 3].
print("Root of the function:", solution.root)
# Output: Root of the function: 2.0


# interpolation
#----------------------------------------
# interpolation is a method of estimating values between known data points.
from scipy.interpolate import interp1d # importing the interp1d function from the scipy.interpolate module.

time=np.array([0, 1, 2, 3, 4])  # Creating an array of time points.
temp=np.array([0, 10, 20, 30, 40])  # Creating an array of temperature values corresponding to the time points.
model=interp1d(time, temp)  # Creating a linear interpolation function based on the time and temperature data.

print("Interpolated temperature at time 2.5:", model(2.5))  # Interpolating the temperature at time 2.5.
# Output: Interpolated temperature at time 2.5: 25.0


# statistics with scipy
#----------------------------------------


from scipy import stats # importing the stats module from the scipy library.
data=np.array([1, 2, 3, 4, 5])

summary=stats.describe(data)  # Getting a summary of statistics for the data array. it gives number of observations, min and max values, mean, variance, skewness, and kurtosis.
print("Summary of statistics:", summary)
# Output: Summary of statistics: DescribeResult(nobs=5, minmax=(1, 5), mean=3.0, variance=2.5, skewness=0.0, kurtosis=-1.3)


# correlation
#--------------------------------------------------

hours=np.array([1, 2, 3, 4, 5])  # Creating an array of hours studied.
scores=np.array([50, 60, 70, 80, 90])  # Creating an array of test scores.

correlation, p_value = stats.pearsonr(hours, scores)  # Calculating the Pearson correlation coefficient between hours studied and test scores.

print("Correlation coefficient:", correlation)
# Output: Correlation coefficient: 1.0
print("P-value:", p_value)
# Output: P-value: 0.0


# solving linear equations
#----------------------------------------
# solving linear equations is a fundamental task in linear algebra, where we find the values of variables that satisfy a set of linear equations.

from scipy.linalg import solve # importing the solve function from the scipy.linalg module.

A=np.array([[3, 2], [1, 2]])  # Creating a coefficient matrix A for the system of equations.
b=np.array([5, 5])  # Creating a constant vector b for the system of equations.

solution=solve(A, b)  # Solving the system of linear equations Ax = b and finds the values of x that satisfy the equations, which is unknowns values of x.
print("Solution of the linear equations:", solution)
# Output: Solution of the linear equations: [1. 2.]
