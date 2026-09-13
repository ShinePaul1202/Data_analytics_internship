
import numpy as np


# --------------------------------------------------
# Task 1: Generate Dataset
# --------------------------------------------------

def generate_dataset(theta, n, m, rng):
    
    # Generate m continuous independent variables
    X_features = rng.normal(0, 1, (n, m))

    # Add intercept column
    X = np.hstack((np.ones((n, 1)), X_features))

    # Generate true beta
    beta = rng.normal(0, 1, m + 1)

    # Calculate x . beta
    z = X @ beta

    # Logistic probability
    probability = 1 / (1 + np.exp(-z))

    # Generate clean labels
    Y = (probability > 0.5).astype(int)

    # Add noise
    flip = rng.binomial(1, theta, n)
    Y = np.where(flip == 1, 1 - Y, Y)

    return X, Y.reshape(n, 1), beta


# --------------------------------------------------
# Task 2: Logistic Regression using Gradient Descent
# --------------------------------------------------

def logistic_regression_gd(X, Y, k, tau, lam, rng):

    Y = Y.flatten()

    n, m_plus_one = X.shape

    # Randomly initialise beta
    beta = rng.normal(0, 0.01, m_plus_one)

    # Initial cost
    z = X @ beta
    p = 1 / (1 + np.exp(-z))

    p = np.clip(p, 1e-10, 1 - 1e-10)

    cost = -(1 / n) * np.sum(
        Y * np.log(p) + (1 - Y) * np.log(1 - p)
    )

    # Gradient Descent
    for i in range(k):

        # Calculate probabilities
        z = X @ beta
        p = 1 / (1 + np.exp(-z))

        # Calculate gradient
        gradient = (1 / n) * (X.T @ (p - Y))

        # Update beta
        beta = beta - lam * gradient

        # Calculate new cost
        z = X @ beta
        p = 1 / (1 + np.exp(-z))

        p = np.clip(p, 1e-10, 1 - 1e-10)

        new_cost = -(1 / n) * np.sum(
            Y * np.log(p) + (1 - Y) * np.log(1 - p)
        )

        # Check convergence
        if abs(cost - new_cost) < tau:
            cost = new_cost
            break

        cost = new_cost

    return beta, cost


# --------------------------------------------------
# Task 3: Experiment
# --------------------------------------------------

m = 3

n_values = [50, 100, 250, 500, 1000, 2500, 5000]

theta_values = [0.0, 0.05, 0.1, 0.2, 0.3, 0.45]

number_of_trials = 8

k = 1500
tau = 1e-9
lam = 0.5

rng = np.random.default_rng(42)


print("Task 3: Effect of n and theta")
print("-" * 80)


for theta in theta_values:

    for n in n_values:

        beta_errors = []
        final_costs = []

        for trial in range(number_of_trials):

            # Generate training data
            X, Y, beta_true = generate_dataset(
                theta, n, m, rng
            )

            # Learn beta
            beta_learned, final_cost = logistic_regression_gd(
                X, Y, k, tau, lam, rng
            )

            # Measure difference between true and learned beta
            beta_error = np.linalg.norm(
                beta_learned - beta_true
            )

            beta_errors.append(beta_error)
            final_costs.append(final_cost)

        # Calculate average results
        mean_error = np.mean(beta_errors)
        std_error = np.std(beta_errors)
        mean_cost = np.mean(final_costs)

        print(
            f"n = {n:5d}, "
            f"theta = {theta:.2f}, "
            f"Mean beta error = {mean_error:.4f}, "
            f"Std = {std_error:.4f}, "
            f"Mean cost = {mean_cost:.4f}"
        )


# ===================================== 
# REPORT
# ===================================== 

""" The results show that the sample size n and the label noise theta both affect the 
ability of logistic regression to recover the true coefficients beta. As n increases,
the coefficient error generally decreases for low and moderate values of theta.
For example, when theta = 0.10, the mean beta error decreases from 1.7814 
for n = 50 to 0.5324 for n = 2500. This indicates that having more training data 
generally helps the Gradient Descent algorithm estimate the coefficients more accurately.
As theta increases, more output labels are randomly flipped. This makes it more difficult
for the model to recover the original beta values. 

At theta = 0.45, the coefficient error remains relatively high even when n is large, because almost half of the labels 
contain noise. Some fluctuations can be seen in the results because the data, beta values, 
and label noise are randomly generated. Therefore, the error does not always decrease 
smoothly as n increases. An unusual result occurs when theta = 0. The coefficient error 
is very large, even though the final cost is very small. This happens because the labels 
are generated using a 0.5 threshold, which can produce linearly separable data. In this 
situation, logistic regression can increase the magnitude of its coefficients while 
continuing to reduce the cost. Overall, the experiment shows that larger datasets 
generally improve the stability and accuracy of coefficient estimation, while increasing 
label noise makes it more difficult to recover the true beta coefficients. """