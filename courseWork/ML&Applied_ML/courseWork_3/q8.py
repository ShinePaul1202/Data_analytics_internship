import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# Task 8: Report & Insights
# =========================================================
try:
    print("=" * 70)
    print("YOUTUBE ANALYTICS - FINAL REPORT")
    print("=" * 70)


    # 1. Regression Model Performance
    # ---------------------------------------------------------

    regression_results = pd.DataFrame({
        "Metric": ["MSE", "RMSE", "MAE", "R²"],
        "Value": [
            3443346750623.50,
            1855625.70,
            605411.15,
            0.9029
        ]
    })

    print("\n1. REGRESSION MODEL PERFORMANCE")
    print("-" * 70)

    print(regression_results.to_string(index=False))

    print(
        "\nThe Linear Regression model performed well on the test data, "
        "with an R² score of 0.9029. This means that the model explains "
        "about 90.29% of the variation in video views."
    )

    print(
        "The RMSE was approximately 1.86 million views, while the MAE "
        "was approximately 605,411 views."
    )


    # 2. Key Predictors of Views
    # ---------------------------------------------------------

    print("\n2. KEY PREDICTORS OF VIEWS")
    print("-" * 70)

    print(
        "The Linear Regression coefficient analysis showed that "
        "channel-related features had some of the largest coefficients "
        "in the model."
    )

    print(
        "The correlation analysis also showed a strong positive "
        "relationship between likes and views, with a correlation "
        "of approximately 0.83."
    )

    print(
        "Comment count also had a positive relationship with views, "
        "with a correlation of approximately 0.56. Dislikes had a "
        "moderate positive correlation of approximately 0.44."
    )

    print(
        "Title length had only a very weak relationship with views."
    )


    # 3. Classification Model Performance
    # ---------------------------------------------------------

    classification_results = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1-score",
            "ROC-AUC"
        ],
        "Value": [
            0.9395,
            0.9256,
            0.8240,
            0.8719,
            0.9824
        ]
    })

    print("\n3. CLASSIFICATION MODEL PERFORMANCE")
    print("-" * 70)

    print(classification_results.to_string(index=False))

    print(
        "\nThe Logistic Regression model performed well in predicting "
        "whether a video was viral or non-viral."
    )

    print(
        "The model achieved an accuracy of 93.95%, meaning that most "
        "of the test videos were classified correctly."
    )

    print(
        "The ROC-AUC score was 0.9824, showing that the model was "
        "very effective at distinguishing between viral and "
        "non-viral videos."
    )

    print(
        "The recall was 82.40%, meaning that the model correctly "
        "identified a large proportion of the actual viral videos."
    )


    # 4. Key Predictors of Viral Videos
    # ---------------------------------------------------------

    print("\n4. KEY PREDICTORS OF VIRAL VIDEOS")
    print("-" * 70)

    print(
        "Likes were the strongest feature influencing the Logistic "
        "Regression prediction of virality."
    )

    print(
        "Several channel-related features also had relatively large "
        "positive or negative coefficients. This suggests that the "
        "channel associated with a video is also useful for predicting "
        "whether the video will be classified as viral."
    )

    print(
        "Overall, the results suggest that viewer engagement is an "
        "important factor when identifying potentially viral videos."
    )


    # 5. Hypothesis Testing
    # ---------------------------------------------------------

    hypothesis_results = pd.DataFrame({
        "Feature": [
            "Likes",
            "Dislikes",
            "Comment Count"
        ],
        "t-statistic": [
            49.6269,
            50.8031,
            48.1664
        ],
        "p-value": [
            "< 0.05",
            "< 0.05",
            "< 0.05"
        ],
        "Decision": [
            "Reject H0",
            "Reject H0",
            "Reject H0"
        ]
    })

    print("\n5. HYPOTHESIS TESTING INSIGHTS")
    print("-" * 70)

    print(hypothesis_results.to_string(index=False))

    print(
        "\nThe p-values for likes, dislikes, and comment count were "
        "all below 0.05. Therefore, the null hypothesis was rejected "
        "for all three features."
    )

    print(
        "This means that there is statistically significant evidence "
        "of a difference in views between the high and low engagement "
        "groups for likes, dislikes, and comment count."
    )

    print(
        "The correlation analysis also showed positive relationships "
        "between these engagement measures and views, especially for "
        "likes. Together, these results suggest that engagement is "
        "closely associated with video views."
    )

    # 6. Cross-Validation and Scaling Comparison
    # ---------------------------------------------------------

    scaling_results = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Linear Regression",
            "Logistic Regression",
            "Logistic Regression"
        ],
        "Scaling": [
            "StandardScaler",
            "MinMaxScaler",
            "StandardScaler",
            "MinMaxScaler"
        ],
        "Mean CV Score": [
            -13.1197,
            -13.1206,
            0.9525,
            0.8830
        ],
        "Variance": [
            762.655830,
            762.757941,
            0.000046,
            0.000380
        ]
    })

    print("\n6. CROSS-VALIDATION AND SCALING COMPARISON")
    print("-" * 70)

    print(scaling_results.to_string(index=False))

    print(
        "\nFor Linear Regression, StandardScaler and MinMaxScaler "
        "produced almost identical results. The mean R² values were "
        "-13.1197 and -13.1206 respectively."
    )

    print(
        "The negative Linear Regression cross-validation score was "
        "mainly affected by one fold that produced a very low R² score."
    )

    print(
        "For Logistic Regression, StandardScaler performed clearly "
        "better than MinMaxScaler. The mean ROC-AUC was 0.9525 with "
        "StandardScaler compared with 0.8830 with MinMaxScaler."
    )

    print(
        "Therefore, StandardScaler was the better scaling method "
        "for the Logistic Regression model in this experiment."
    )


    # 7. Business Recommendations
    # ---------------------------------------------------------

    print("\n7. BUSINESS RECOMMENDATIONS")
    print("-" * 70)

    print(
        "1. Encourage viewer engagement."
    )

    print(
        "Likes and comments showed positive relationships with views. "
        "Content creators can therefore encourage viewers to interact "
        "with videos through questions, calls to action, and engaging "
        "content."
    )

    print(
        "2. Focus on channel strategy."
    )

    print(
        "Channel-related features appeared among the strongest "
        "predictors in the regression and classification models. "
        "Creators can study which types of channels and content "
        "perform better and use those insights when planning future "
        "videos."
    )

    print(
        "3. Use engagement information to identify potentially viral "
        "videos."
    )

    print(
        "The Logistic Regression model achieved a ROC-AUC of 0.9824 "
        "on the test set. This suggests that engagement-related "
        "information can be useful for identifying videos that are "
        "more likely to be classified as viral."
    )

    print(
        "4. Be careful when making recommendations about video length."
    )

    print(
        "The dataset used in this project does not contain a video "
        "duration column, so an exact optimal video length cannot be "
        "determined from this analysis. Title length had only a weak "
        "relationship with views."
    )

    print(
        "5. Use StandardScaler for the Logistic Regression model."
    )

    print(
        "Based on the five-fold cross-validation results, StandardScaler "
        "gave a better mean ROC-AUC than MinMaxScaler."
    )


    # 8. Overall Conclusion
    # ---------------------------------------------------------

    print("\n8. OVERALL CONCLUSION")
    print("-" * 70)

    print(
        "Overall, the analysis shows that viewer engagement and "
        "channel characteristics are important factors related to "
        "YouTube video performance."
    )

    print(
        "The Linear Regression model achieved an R² of 0.9029 on "
        "the test data, while the Logistic Regression model achieved "
        "93.95% accuracy and a ROC-AUC of 0.9824."
    )

    print(
        "The hypothesis tests also showed statistically significant "
        "differences in views between high and low engagement groups "
        "for likes, dislikes, and comment count."
    )

    print(
        "Among the features used for classification, likes had the "
        "strongest influence on the prediction of virality."
    )

    print(
        "Overall, improving viewer engagement and understanding "
        "channel-level performance appear to be useful strategies "
        "for improving YouTube video performance."
    )


    # =========================================================
    # PLOTS
    # =========================================================


    # Plot 1: Classification Model Performance
    # ---------------------------------------------------------

    metrics = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1-score",
        "ROC-AUC"
    ]

    values = [
        0.9395,
        0.9256,
        0.8240,
        0.8719,
        0.9824
    ]

    plt.figure(figsize=(9, 6))

    plt.bar(metrics, values)

    plt.ylim(0, 1)

    plt.title("Logistic Regression Performance")

    plt.xlabel("Metric")
    plt.ylabel("Score")

    plt.tight_layout()

    plt.show()


    # Plot 2: Scaling Comparison
    # ---------------------------------------------------------

    models = [
        "Linear\nStandard",
        "Linear\nMinMax",
        "Logistic\nStandard",
        "Logistic\nMinMax"
    ]

    scores = [
        -13.1197,
        -13.1206,
        0.9525,
        0.8830
    ]

    plt.figure(figsize=(9, 6))

    plt.bar(models, scores)

    plt.title("Cross-Validation Scaling Comparison")

    plt.xlabel("Model and Scaling Method")

    plt.ylabel("Mean CV Score")

    plt.tight_layout()

    plt.show()


    print("\nReport completed successfully.")

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")