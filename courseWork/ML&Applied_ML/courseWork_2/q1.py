# task 1:
# Generate a synthetic binary classification dataset.

import numpy as np


def generate_dataset(theta, n, m):
    """
    Generate a synthetic binary classification dataset.

    Parameters:
        theta : probability of flipping a label
        n     : number of samples
        m     : number of independent variables

    Returns:
        X     : n x (m+1) numpy array
        Y     : n x 1 binary numpy array
        beta  : random coefficient vector of size m+1
    """

    # Input validation
    if not isinstance(n, (int, np.integer)):
        raise TypeError("n must be an integer.")

    if not isinstance(m, (int, np.integer)):
        raise TypeError("m must be an integer.")

    if not isinstance(theta, (int, float, np.integer, np.floating)):
        raise TypeError("theta must be a number.")

    if n <= 0:
        raise ValueError("n must be greater than 0.")

    if m <= 0:
        raise ValueError("m must be greater than 0.")

    if theta < 0 or theta > 1:
        raise ValueError("theta must be between 0 and 1.")

    # Generate m continuous independent variables
    X_features = np.random.randn(n, m)

    # Add a column of 1s (x_i0 = 1)
    X = np.hstack((np.ones((n, 1)), X_features))

    # Generate random coefficients
    beta = np.random.randn(m + 1)

    # Calculate x · beta
    z = X @ beta

    # Logistic probability
    probability = 1 / (1 + np.exp(-z))

    # Generate binary labels
    Y = (probability > 0.5).astype(int)

    # Add label noise using Bernoulli(theta)
    flip = np.random.binomial(1, theta, n)

    # Flip labels where flip = 1
    Y = np.where(flip == 1, 1 - Y, Y)

    # Convert Y to an n x 1 array
    Y = Y.reshape(n, 1)

    return X, Y, beta

