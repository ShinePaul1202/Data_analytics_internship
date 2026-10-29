USE FinanceHub;

-- q1
SELECT
    CONCAT(first_name, ' ', last_name) AS customer_name,
    credit_score,
    annual_income,
    risk_profile
FROM Customers
WHERE credit_score > 700 AND annual_income > 80000
ORDER BY credit_score DESC;

-- q2
SELECT
    category,
    SUM(amount) AS total_amount
FROM Transactions
WHERE transaction_date >= '2024-01-01' AND transaction_date < '2025-01-01'
GROUP BY category HAVING SUM(amount) > 5000
ORDER BY total_amount DESC;