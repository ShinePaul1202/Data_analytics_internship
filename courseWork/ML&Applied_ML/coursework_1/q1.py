# Write a function to generate an m+1 dimensional data set, of size n, consisting of m continuous independent variables (X) and one dependent variable (y) defined as
# yi = xi β + e
# where,
# • e is a Gaussian distribution with mean 0 and standard deviation (σ), representing the unexplained variation in y
# • β is a random vector of dimensionality m + 1, representing the coefficients of the linear relationship between X and y, and
# • ∀ i ∈ [1, n], xi0 = 1
# The function should take the following parameters:
# • σ: The spread of noise in the output variable
# • n: The size of the data set
# • m: The number of independent variables
# Output from the function should be:
# • X: An n × m numpy array of independent variable values (with a 1 in the first column)
# • y : The n × 1 numpy array of output values
# • β: The random coefficients used to generate y from X


import numpy as np

def generate_data(sigma,n,m):
  X=np.random.randn(n,m)
  X=np.column_stack((np.ones(n),X))

  beta=np.random.randn(m+1,1)
  e=np.random.normal(0,sigma,(n,1))

  y=X@beta+e

  return X, y, beta
  


