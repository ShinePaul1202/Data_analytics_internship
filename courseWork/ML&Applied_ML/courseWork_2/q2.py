# task 2:
# Implement logistic regression using Gradient Descent.
import numpy as np


def logistic_regression_gd(X, Y, k, tau, lam):
    """
    Learn logistic regression coefficients using Gradient Descent.

    Parameters:
        X   : n x m numpy array of independent variables
        Y   : n x 1 binary numpy array of output values
        k   : maximum number of iterations
        tau : threshold for change in cost
        lam : learning rate

    Returns:
        beta : m+1 dimensional coefficient vector
        cost : final cost function value
    """

    # ---------------- Input validation ----------------

    if not isinstance(X, np.ndarray):
        raise TypeError("X must be a numpy array.")

    if not isinstance(Y, np.ndarray):
        raise TypeError("Y must be a numpy array.")

    if X.ndim != 2:
        raise ValueError("X must be a 2-dimensional array.")

    if Y.ndim not in (1, 2):
        raise ValueError("Y must be a 1-dimensional or 2-dimensional array.")

    if X.shape[0] != Y.shape[0]:
        raise ValueError("X and Y must have the same number of samples.")

    if not np.all(np.isin(Y, [0, 1])):
        raise ValueError("Y must contain only 0 and 1.")

    if not isinstance(k, (int, np.integer)):
        raise TypeError("k must be an integer.")

    if not isinstance(tau, (int, float, np.integer, np.floating)):
        raise TypeError("tau must be a number.")

    if not isinstance(lam, (int, float, np.integer, np.floating)):
        raise TypeError("lambda must be a number.")

    if k <= 0:
        raise ValueError("k must be greater than 0.")

    if tau < 0:
        raise ValueError("tau must be greater than or equal to 0.")

    if lam <= 0:
        raise ValueError("lambda must be greater than 0.")

    # Make Y a 1-dimensional array
    Y = Y.flatten()

    n, m = X.shape

    # ---------------- Add intercept column ----------------

    X = np.hstack((np.ones((n, 1)), X))

    # ---------------- Initialize beta randomly ----------------

    beta = np.random.randn(m + 1)

    # Calculate initial cost
    z = X @ beta
    p = 1 / (1 + np.exp(-z))

    epsilon = 1e-10
    p = np.clip(p, epsilon, 1 - epsilon)

    cost = -(1 / n) * np.sum(
        Y * np.log(p) + (1 - Y) * np.log(1 - p)
    )

    # ---------------- Gradient Descent ----------------

    for i in range(k):

        # Calculate predicted probabilities
        z = X @ beta
        p = 1 / (1 + np.exp(-z))

        # Calculate gradient
        gradient = (1 / n) * (X.T @ (p - Y))

        # Update beta
        beta = beta - lam * gradient

        # Calculate new cost
        z = X @ beta
        p = 1 / (1 + np.exp(-z))

        p = np.clip(p, epsilon, 1 - epsilon)

        new_cost = -(1 / n) * np.sum(
            Y * np.log(p) + (1 - Y) * np.log(1 - p)
        )

        # Stop if change in cost is below tau
        if abs(cost - new_cost) < tau:
            cost = new_cost
            break

        cost = new_cost

    return beta, cost