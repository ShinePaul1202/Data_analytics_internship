# ============================================================
# Q5: Merge Linear Regression and Logistic Regression
# using Object-Oriented Programming
# ============================================================

import numpy as np


# ============================================================
# 1. BASE DATA GENERATOR
# ============================================================

class DataGenerator:
    """
    Common class for generating X and beta.
    """

    def __init__(self, seed=None):
        self.rng = np.random.default_rng(seed)

    def generate_X_beta(self, n, m):
        if n <= 0:
            raise ValueError("n must be greater than 0.")

        if m <= 0:
            raise ValueError("m must be greater than 0.")

        # Generate m continuous independent variables
        X_features = self.rng.normal(0, 1, (n, m))

        # Add intercept column
        X = np.hstack((np.ones((n, 1)), X_features))

        # Generate beta
        beta = self.rng.normal(0, 1, (m + 1, 1))

        return X, beta


# ============================================================
# 2. LINEAR DATA GENERATOR
# ============================================================

class LinearDataGenerator(DataGenerator):
    """
    Generates data for linear regression:

        y = X beta + noise
    """

    def __init__(self, sigma, seed=None):
        super().__init__(seed)

        if sigma < 0:
            raise ValueError("sigma must be >= 0.")

        self.sigma = sigma

    def generate(self, n, m):

        X, beta = self.generate_X_beta(n, m)

        # Generate Gaussian noise
        noise = self.rng.normal(
            0,
            self.sigma,
            (n, 1)
        )

        # Generate y
        y = X @ beta + noise

        return X, y, beta


# ============================================================
# 3. LOGISTIC DATA GENERATOR
# ============================================================

class LogisticDataGenerator(DataGenerator):
    """
    Generates data for logistic regression.
    """

    def __init__(self, theta, seed=None):
        super().__init__(seed)

        if theta < 0 or theta > 1:
            raise ValueError("theta must be between 0 and 1.")

        self.theta = theta

    def generate(self, n, m):

        X, beta = self.generate_X_beta(n, m)

        # Calculate sigmoid probability
        z = X @ beta
        probability = 1 / (1 + np.exp(-z))

        # Generate binary labels
        y = (probability > 0.5).astype(int)

        # Flip labels with probability theta
        flip = self.rng.binomial(
            1,
            self.theta,
            n
        ).reshape(n, 1)

        y = np.where(
            flip == 1,
            1 - y,
            y
        )

        return X, y, beta


# ============================================================
# 4. BASE REGRESSION CLASS
# ============================================================

class Regression:
    """
    Common class for Linear and Logistic Regression.

    Contains the common Gradient Descent and
    regularization code.
    """

    def __init__(
        self,
        k=1000,
        tau=1e-8,
        learning_rate=0.01,
        reg_type="none",
        reg_lambda=0,
        seed=None
    ):

        if k <= 0:
            raise ValueError("k must be greater than 0.")

        if tau < 0:
            raise ValueError("tau must be >= 0.")

        if learning_rate <= 0:
            raise ValueError("learning_rate must be greater than 0.")

        if reg_type not in ["none", "l1", "l2"]:
            raise ValueError(
                "reg_type must be 'none', 'l1' or 'l2'."
            )

        if reg_lambda < 0:
            raise ValueError(
                "reg_lambda must be >= 0."
            )

        self.k = k
        self.tau = tau
        self.learning_rate = learning_rate
        self.reg_type = reg_type
        self.reg_lambda = reg_lambda
        self.seed = seed

        self.beta = None
        self.cost = None

    # --------------------------------------------------------
    # These functions will be different for each regression
    # algorithm.
    # --------------------------------------------------------

    def activation(self, z):
        raise NotImplementedError

    def calculate_cost(self, y, prediction):
        raise NotImplementedError

    # --------------------------------------------------------
    # Regularization
    # --------------------------------------------------------

    def regularization_cost(self, beta, n):

        # Do not regularize the intercept beta[0]
        coefficients = beta[1:]

        if self.reg_type == "l2":

            return (
                self.reg_lambda / (2 * n)
            ) * np.sum(coefficients ** 2)

        elif self.reg_type == "l1":

            return (
                self.reg_lambda / n
            ) * np.sum(np.abs(coefficients))

        return 0

    # --------------------------------------------------------
    # Gradient Descent
    # --------------------------------------------------------

    def fit(self, X, y):

        n, m = X.shape

        y = y.reshape(-1, 1)

        # Random beta initialization
        rng = np.random.default_rng(self.seed)

        beta = rng.normal(
            0,
            0.01,
            (m, 1)
        )

        # Initial cost
        prediction = self.activation(X @ beta)

        previous_cost = (
            self.calculate_cost(y, prediction)
            + self.regularization_cost(beta, n)
        )

        current_cost = previous_cost

        # Gradient Descent
        for i in range(self.k):

            # Calculate prediction
            prediction = self.activation(X @ beta)

            # Gradient
            gradient = (
                1 / n
            ) * X.T @ (prediction - y)

            # -------------------------
            # L2 regularization
            # -------------------------

            if self.reg_type == "l2":

                gradient[1:] += (
                    self.reg_lambda / n
                ) * beta[1:]

                beta = (
                    beta
                    - self.learning_rate * gradient
                )

            # -------------------------
            # L1 regularization
            # -------------------------

            elif self.reg_type == "l1":

                beta_step = (
                    beta
                    - self.learning_rate * gradient
                )

                threshold = (
                    self.learning_rate
                    * self.reg_lambda
                    / n
                )

                beta[1:] = (
                    np.sign(beta_step[1:])
                    * np.maximum(
                        np.abs(beta_step[1:])
                        - threshold,
                        0
                    )
                )

                # Intercept is not regularized
                beta[0] = beta_step[0]

            # -------------------------
            # No regularization
            # -------------------------

            else:

                beta = (
                    beta
                    - self.learning_rate * gradient
                )

            # Calculate new cost
            prediction = self.activation(X @ beta)

            current_cost = (
                self.calculate_cost(y, prediction)
                + self.regularization_cost(beta, n)
            )

            # Stopping condition
            if abs(current_cost - previous_cost) < self.tau:
                break

            previous_cost = current_cost

        self.beta = beta
        self.cost = current_cost

        return self


# ============================================================
# 5. LINEAR REGRESSION
# ============================================================

class LinearRegression(Regression):
    """
    Linear Regression inherits the common Gradient Descent
    code from Regression.
    """

    def activation(self, z):

        # Linear prediction
        return z

    def calculate_cost(self, y, prediction):

        n = y.shape[0]

        return (
            1 / (2 * n)
        ) * np.sum(
            (prediction - y) ** 2
        )


# ============================================================
# 6. LOGISTIC REGRESSION
# ============================================================

class LogisticRegression(Regression):
    """
    Logistic Regression inherits the common Gradient Descent
    and regularization code from Regression.
    """

    def activation(self, z):

        # Sigmoid function
        return 1 / (1 + np.exp(-z))

    def calculate_cost(self, y, prediction):

        n = y.shape[0]

        # Prevent log(0)
        epsilon = 1e-10

        prediction = np.clip(
            prediction,
            epsilon,
            1 - epsilon
        )

        return -(1 / n) * np.sum(
            y * np.log(prediction)
            + (1 - y) * np.log(1 - prediction)
        )

    def predict(self, X):

        probability = self.activation(
            X @ self.beta
        )

        return (probability > 0.5).astype(int)


# ============================================================
# 7. TEST LINEAR REGRESSION
# ============================================================

print("=" * 60)
print("LINEAR REGRESSION")
print("=" * 60)

m = 3

linear_generator = LinearDataGenerator(
    sigma=2,
    seed=42
)

X_linear, y_linear, beta_true_linear = (
    linear_generator.generate(500, m)
)

linear_model = LinearRegression(
    k=2000,
    tau=1e-8,
    learning_rate=0.05,
    seed=10
)

linear_model.fit(
    X_linear,
    y_linear
)

linear_error = (
    np.linalg.norm(
        beta_true_linear
        - linear_model.beta
    )
    / np.linalg.norm(beta_true_linear)
)

print("True beta:")
print(beta_true_linear)

print("\nLearned beta:")
print(linear_model.beta)

print(
    "\nRelative beta error:",
    round(linear_error, 4)
)

print(
    "Final cost:",
    round(linear_model.cost, 4)
)


# ============================================================
# 8. TEST LOGISTIC REGRESSION
# ============================================================

print("\n" + "=" * 60)
print("LOGISTIC REGRESSION")
print("=" * 60)

logistic_generator = LogisticDataGenerator(
    theta=0.10,
    seed=42
)

X_logistic, y_logistic, beta_true_logistic = (
    logistic_generator.generate(500, m)
)

logistic_model = LogisticRegression(
    k=2000,
    tau=1e-9,
    learning_rate=0.5,
    seed=10
)

logistic_model.fit(
    X_logistic,
    y_logistic
)

predictions = logistic_model.predict(
    X_logistic
)

accuracy = np.mean(
    predictions == y_logistic
)

print("True beta:")
print(beta_true_logistic)

print("\nLearned beta:")
print(logistic_model.beta)

print(
    "\nTraining accuracy:",
    round(accuracy, 4)
)

print(
    "Final cost:",
    round(logistic_model.cost, 4)
)


# ============================================================
# 9. SHOW CODE REUSE WITH L1 AND L2
# ============================================================

print("\n" + "=" * 60)
print("L1 AND L2 REGULARIZATION")
print("=" * 60)


# Linear Regression + L1
linear_l1 = LinearRegression(
    k=2000,
    tau=1e-8,
    learning_rate=0.05,
    reg_type="l1",
    reg_lambda=10,
    seed=10
)

linear_l1.fit(
    X_linear,
    y_linear
)

print("\nLinear Regression - L1:")
print(linear_l1.beta)


# Linear Regression + L2
linear_l2 = LinearRegression(
    k=2000,
    tau=1e-8,
    learning_rate=0.05,
    reg_type="l2",
    reg_lambda=10,
    seed=10
)

linear_l2.fit(
    X_linear,
    y_linear
)

print("\nLinear Regression - L2:")
print(linear_l2.beta)


# Logistic Regression + L1
logistic_l1 = LogisticRegression(
    k=2000,
    tau=1e-9,
    learning_rate=0.5,
    reg_type="l1",
    reg_lambda=10,
    seed=10
)

logistic_l1.fit(
    X_logistic,
    y_logistic
)

print("\nLogistic Regression - L1:")
print(logistic_l1.beta)


# Logistic Regression + L2
logistic_l2 = LogisticRegression(
    k=2000,
    tau=1e-9,
    learning_rate=0.5,
    reg_type="l2",
    reg_lambda=10,
    seed=10
)

logistic_l2.fit(
    X_logistic,
    y_logistic
)

print("\nLogistic Regression - L2:")
print(logistic_l2.beta)