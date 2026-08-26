# Q3: Investigate how different values of n and sigma impact the ability of the linear
# regression function (Q2) to recover the true coefficients beta used to generate y (Q1).

import numpy as np
import matplotlib.pyplot as plt

def generate_data(sigma,n,m):
  X=np.random.randn(n,m)
  X=np.column_stack((np.ones(n),X))

  beta=np.random.randn(m+1,1)
  e=np.random.normal(0,sigma,(n,1))

  y=X@beta+e

  return X, y, beta

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
    errors=[results[(n, sigma)] for n in n_values]
    plt.plot(n_values, errors, marker="o", label=f"sigma={sigma}")
plt.xlabel("n (sample size)")
plt.ylabel("Relative error in beta")
plt.title("Effect of n and sigma on coefficient recovery")
plt.legend()
plt.savefig("error_vs_n.png")
plt.show()


# =====================================
# REPORT
# =====================================
"""
As n increases, the relative error in the learned coefficients generally decreases, 
indicating that using more data helps the linear regression function recover the true beta more accurately. 
However, some small fluctuations occur because the data and noise are randomly generated. 
As sigma increases, the relative error generally increases for a fixed n, since greater noise in y makes it more 
difficult to identify the true relationship between X and y.The results also show that increasing n can reduce 
the effect of higher noise. Overall, a small dataset with high sigma gives the least reliable estimate of beta, 
while a larger dataset with low sigma gives the most accurate coefficient recovery.
"""



