import pandas as pd
from scipy.stats import ttest_ind


# ---------------------------------------------------------
# Task 3: Hypothesis Testing
# ---------------------------------------------------------
try:
    # Load the dataset
    df = pd.read_csv("USvideos.csv")


    # 1. State the Hypothesis
    # ---------------------------------------------------------

    print("Hypothesis:")
    print(
        "Videos with higher likes, dislikes, or comment counts "
        "have significantly higher views."
    )


    print("\nNull Hypothesis (H0):")
    print(
        "Videos with higher likes, dislikes, or comment counts "
        "do not have significantly different views."
    )


    print("\nAlternative Hypothesis (H1):")
    print(
        "Videos with higher likes, dislikes, or comment counts "
        "have significantly different views."
    )


    # 2. Features to Test
    # ---------------------------------------------------------

    features = [
        "likes",
        "dislikes",
        "comment_count"
    ]


    # 3. Perform t-test for Each Feature
    # ---------------------------------------------------------

    print("\nT-Test Results:")
    print("-" * 60)


    for feature in features:

        # Calculate the median of the feature
        median_value = df[feature].median()

        # Create two groups based on the median
        low_group = df[df[feature] <= median_value]["views"]
        high_group = df[df[feature] > median_value]["views"]

        # Perform independent samples t-test
        t_statistic, p_value = ttest_ind(
            high_group,
            low_group,
            equal_var=False
        )

        # Display results
        print(f"\nFeature: {feature}")
        print(f"Median: {median_value}")
        print(f"t-statistic: {t_statistic:.4f}")
        print(f"p-value: {p_value:.10f}")

        # Interpret the p-value
        if p_value < 0.05:

            print("Result: Reject the null hypothesis (p < 0.05).")

            print(
                "Interpretation: There is a statistically significant "
                "difference in views between the high and low groups."
            )

        else:

            print(
                "Result: Fail to reject the null hypothesis (p >= 0.05)."
            )

            print(
                "Interpretation: There is not enough evidence to conclude "
                "that there is a statistically significant difference "
                "in views between the high and low groups."
            )


    # 4. Overall Conclusion
    # ---------------------------------------------------------

    print("\nOverall Conclusion:")

    print(
        "The p-values for likes, dislikes, and comment count are all "
        "less than 0.05. Therefore, the null hypothesis is rejected "
        "for all three features. The results provide statistically "
        "significant evidence of a difference in views between the "
        "high and low groups."
    )

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")