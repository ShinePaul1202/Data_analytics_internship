# Q3: Investigate how different values of n and sigma impact the ability of the linear
# regression function (Q2) to recover the true coefficients beta used to generate y (Q1).

import numpy as np
import matplotlib.pyplot as plt

from q1 import generate_data
from q2 import learn_parameters

m = 3
n_values = [10, 50, 200, 1000]
sigma_values = [0, 1, 5, 10]

results = {}  # (n, sigma) -> relative error in beta

for n in n_values:
    for sigma in sigma_values:
        X, y, beta_true = generate_data(sigma, n, m)
        beta_hat, cost = learn_parameters(X[:, 1:], y, k=2000, tau=1e-8, lam=0.05)
        error = np.linalg.norm(beta_true - beta_hat) / np.linalg.norm(beta_true)
        results[(n, sigma)] = error
        print(f"n={n:<5} sigma={sigma:<3} -> relative beta error = {error:.4f}")

# Plot: error vs n, one line per sigma
plt.figure(figsize=(7, 5))
for sigma in sigma_values:
    errors = [results[(n, sigma)] for n in n_values]
    plt.plot(n_values, errors, marker="o", label=f"sigma={sigma}")
plt.xlabel("n (sample size)")
plt.ylabel("Relative error in beta")
plt.title("Effect of n and sigma on coefficient recovery")
plt.legend()
plt.savefig("error_vs_n.png")
plt.show()


# =============================================================================
# REPORT
# =============================================================================
"""
As n increases, the learned coefficients get closer to the true beta, for every
noise level — more data lets Gradient Descent average out the random noise (e) and
converge to a better estimate. As sigma increases, the error goes up for a fixed n,
since noisier y values carry less information about the true relationship. The two
effects trade off: a larger n can compensate for a higher sigma, but a small,
noisy dataset (low n, high sigma) gives the least reliable estimate of beta.
"""