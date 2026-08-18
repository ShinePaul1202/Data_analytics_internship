# Write a function that learns the parameters of a linear regression line given inputs
# • X : An n × m numpy array of independent variable values
# • y : The n × 1 numpy array of output values
# • k : the number of iterations (epochs)
# • τ : the threshold on change in Cost function value from the previous to current iteration
# • λ : the learning rate for Gradient Descent
# The function should implement the Gradient Descent algorithm as discussed in class that
# initialises β with random values and then updates these values in each iteration by moving into
# the direction defined by the partial derivative of the cost function with respect to each of the
# coefficients. The function should use only one loop that ends after a number of iterations (k) or a
# threshold on the change in cost function value (τ ).
# The output should be an m + 1 dimensional vector of coefficients and the final cost function
# value.

import numpy as np

def learn_parameters(X, y, k, tau, lam):
    n, m = X.shape

    X_new=np.hstack((np.ones((n, 1)), X))
    y=y.reshape(-1, 1)
    
    beta=np.random.rand(m + 1, 1)
    predictions = X_new @ beta
    errors = predictions - y
    prev_cost = (1/(2*n)) * np.sum(errors ** 2)

    cur_cost = prev_cost #fall back , if the loop doesn't run at all.

    for i in range(k):
        predictions = X_new @ beta
        errors = predictions - y
        
        gradient = (1/n) * (X_new.T @ errors)
        beta-=lam*gradient
        predictions = X_new @ beta
        errors = predictions - y
        cur_cost = (1/(2*n)) * np.sum(errors ** 2)

        if abs(cur_cost - prev_cost) < tau:
            break
        
        prev_cost = cur_cost

    return beta, cur_cost


    
    