import numpy as np


# ============================================================
# Task 4: Logistic Regression with L1 and L2 Regularization
# ============================================================


def generate_dataset(theta, n, m, rng):
    """Generate a synthetic binary classification dataset."""

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
    X = rng.normal(0, 1, (n, m))

    # Add intercept column
    X_aug = np.hstack((np.ones((n, 1)), X))

    # Generate true coefficients
    beta = rng.normal(0, 1, m + 1)

    # Generate probabilities and labels
    z = X_aug @ beta
    probability = 1 / (1 + np.exp(-z))
    Y = (probability > 0.5).astype(int)

    # Add label noise
    flip = rng.binomial(1, theta, n)
    Y = np.where(flip == 1, 1 - Y, Y)

    return X, Y.reshape(n, 1), beta


def logistic_regression_regularized(
    X, Y, k, tau, lam, reg_type="none", reg_lambda=0.0, rng=None
):
    """
    Learn logistic regression coefficients using Gradient Descent
    with optional L1 or L2 regularization.

    The intercept is not regularized.

    reg_type:
        "none" -> no regularization
        "l1"   -> L1 regularization
        "l2"   -> L2 regularization
    """

    # ---------------- Input validation ----------------

    if not isinstance(X, np.ndarray):
        raise TypeError("X must be a numpy array.")

    if not isinstance(Y, np.ndarray):
        raise TypeError("Y must be a numpy array.")

    if X.ndim != 2:
        raise ValueError("X must be a 2-dimensional array.")

    if X.shape[0] != Y.shape[0]:
        raise ValueError("X and Y must have the same number of samples.")

    if not np.all(np.isin(Y, [0, 1])):
        raise ValueError("Y must contain only 0 and 1.")

    if not isinstance(k, (int, np.integer)):
        raise TypeError("k must be an integer.")
    if k <= 0:
        raise ValueError("k must be greater than 0.")

    if not isinstance(tau, (int, float, np.integer, np.floating)):
        raise TypeError("tau must be a number.")
    if tau < 0:
        raise ValueError("tau must be greater than or equal to 0.")

    if not isinstance(lam, (int, float, np.integer, np.floating)):
        raise TypeError("learning rate must be a number.")
    if lam <= 0:
        raise ValueError("learning rate must be greater than 0.")

    if reg_type not in ("none", "l1", "l2"):
        raise ValueError("reg_type must be 'none', 'l1', or 'l2'.")

    if not isinstance(reg_lambda, (int, float, np.integer, np.floating)):
        raise TypeError("regularization constant must be a number.")
    if reg_lambda < 0:
        raise ValueError("regularization constant must be >= 0.")

    if rng is None:
        rng = np.random.default_rng()

    Y = Y.flatten()
    n, m = X.shape

    # Add intercept column
    X_aug = np.hstack((np.ones((n, 1)), X))

    # Randomly initialise beta
    beta = rng.normal(0, 0.01, m + 1)

    epsilon = 1e-10

    # Initial cost
    p = 1 / (1 + np.exp(-(X_aug @ beta)))
    p = np.clip(p, epsilon, 1 - epsilon)

    cost = -(1 / n) * np.sum(
        Y * np.log(p) + (1 - Y) * np.log(1 - p)
    )

    # Add regularization penalty
    if reg_type == "l2":
        cost += (reg_lambda / (2 * n)) * np.sum(beta[1:] ** 2)
    elif reg_type == "l1":
        cost += (reg_lambda / n) * np.sum(np.abs(beta[1:]))

    # ---------------- Gradient Descent ----------------

    for i in range(k):

        # Calculate probabilities
        p = 1 / (1 + np.exp(-(X_aug @ beta)))

        # Gradient of the unregularized cost
        gradient = (1 / n) * (X_aug.T @ (p - Y))

        if reg_type == "l2":
            # Do not regularize the intercept beta[0]
            gradient[1:] += (reg_lambda / n) * beta[1:]

            beta = beta - lam * gradient

        elif reg_type == "l1":
            # Proximal Gradient / soft-thresholding for L1
            z = beta - lam * gradient

            threshold = lam * reg_lambda / n

            beta[0] = z[0]
            beta[1:] = (
                np.sign(z[1:])
                * np.maximum(np.abs(z[1:]) - threshold, 0)
            )

        else:
            beta = beta - lam * gradient

        # Calculate new cost
        p = 1 / (1 + np.exp(-(X_aug @ beta)))
        p = np.clip(p, epsilon, 1 - epsilon)

        new_cost = -(1 / n) * np.sum(
            Y * np.log(p) + (1 - Y) * np.log(1 - p)
        )

        if reg_type == "l2":
            new_cost += (reg_lambda / (2 * n)) * np.sum(beta[1:] ** 2)

        elif reg_type == "l1":
            new_cost += (reg_lambda / n) * np.sum(np.abs(beta[1:]))

        # Stop when the change in cost is below tau
        if abs(cost - new_cost) < tau:
            cost = new_cost
            break

        cost = new_cost

    return beta, cost


# ============================================================
# Experiment: Effect of Regularization Type and Strength
# ============================================================

if __name__ == "__main__":

    try:
        rng = np.random.default_rng(42)

        # Dataset settings
        n = 500
        m = 3
        theta = 0.10

        # Gradient Descent settings
        k = 3000
        tau = 1e-9
        learning_rate = 0.3

        # Values of the regularization constant
        lambda_values = [0, 1, 10, 50, 100, 200]

        # Generate one dataset so that all models are compared
        # using the same true beta and same training data.
        X, Y, beta_true = generate_dataset(theta, n, m, rng)

        print("Task 4: L1 and L2 Regularization")
        print("-" * 90)
        print("True beta:")
        print(np.round(beta_true, 4))
        print()

        print(
            f"{'Type':<8}"
            f"{'Lambda':>10}"
            f"{'Beta error':>15}"
            f"{'||beta[1:]||':>15}"
            f"{'Zero coeffs':>15}"
            f"{'Cost':>12}"
        )
        print("-" * 90)

        for reg_type in ["none", "l1", "l2"]:

            for reg_lambda in lambda_values:

                if reg_type == "none" and reg_lambda != 0:
                    continue

                beta_learned, final_cost = logistic_regression_regularized(
                    X,
                    Y,
                    k,
                    tau,
                    learning_rate,
                    reg_type=reg_type,
                    reg_lambda=reg_lambda,
                    rng=rng
                )

                # Compare learned beta with true beta
                beta_error = np.linalg.norm(beta_learned - beta_true)

                # Size of feature coefficients (intercept excluded)
                beta_norm = np.linalg.norm(beta_learned[1:])

                # Count coefficients that are effectively zero
                zero_coeffs = np.sum(np.abs(beta_learned[1:]) < 1e-6)

                print(
                    f"{reg_type:<8}"
                    f"{reg_lambda:>10.2f}"
                    f"{beta_error:>15.4f}"
                    f"{beta_norm:>15.4f}"
                    f"{zero_coeffs:>15}"
                    f"{final_cost:>12.4f}"
                )

        print("\nTrue beta:")
        print(np.round(beta_true, 4))

        print(
            "\nObservation: Increasing the regularization constant "
            "shrinks the feature coefficients."
        )
        print(
            "L1 regularization can make some coefficients exactly zero, "
            "while L2 generally shrinks coefficients smoothly toward zero."
        )

    except (TypeError, ValueError) as error:
        print("Error:", error)


# ============================================================
# Report
# ============================================================

"""

L1 and L2 regularization were added to the logistic regression cost function
to control the size of the learned coefficients. The intercept coefficient
was not regularized.

For L2 regularization, the cost function becomes:

J_L2(beta) = J(beta) + (lambda/(2n)) * sum(beta_j^2)

For L1 regularization:

J_L1(beta) = J(beta) + (lambda/n) * sum(|beta_j|)

where the sums exclude the intercept coefficient.

L2 adds (lambda/n) * beta_j to the gradient of each feature coefficient.
L1 uses a soft-thresholding step because the absolute-value function is not
differentiable at zero.

The experiment compares different values of the regularization constant
lambda. Increasing lambda increases the penalty and therefore shrinks the
learned beta coefficients toward zero.

L2 shrinks the coefficients smoothly and usually keeps them non-zero.
L1 can shrink some coefficients exactly to zero, producing a sparse model
and performing implicit feature selection.

Therefore, a small regularization constant has a relatively small effect on
the learned beta vector, while a large regularization constant produces
stronger shrinkage. Very large values can cause underfitting because the
feature coefficients become too small.

Overall, regularization reduces the magnitude of the learned coefficients
and can help prevent the model from fitting noise. L1 is useful when a
sparse model is desired, while L2 is useful when the features are expected
to contribute more continuously to the model.
"""
