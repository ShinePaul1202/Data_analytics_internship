import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve
)


# ---------------------------------------------------------
# Task 6: Logistic Regression
# ---------------------------------------------------------
try:
    # Load the dataset
    df = pd.read_csv("USvideos.csv")


    # 1. Create Required Features
    # ---------------------------------------------------------

    # Title length
    df["title_length"] = df["title"].str.len()


    # Convert dates
    df["trending_date"] = pd.to_datetime(
        df["trending_date"],
        format="%y.%d.%m"
    )

    df["publish_time"] = pd.to_datetime(
        df["publish_time"],
        utc=True
    )


    # Days since publication
    df["days_since_publish"] = (
        df["trending_date"].dt.tz_localize("UTC")
        - df["publish_time"].dt.normalize()
    ).dt.days


    # 2. Create Viral Target
    # ---------------------------------------------------------

    top_25_quantile = df["views"].quantile(0.75)

    df["viral"] = (
        df["views"] > top_25_quantile
    ).astype(int)


    # 3. Select Features
    # ---------------------------------------------------------

    numeric_features = [
        "likes",
        "dislikes",
        "comment_count",
        "title_length",
        "days_since_publish"
    ]

    categorical_features = [
        "channel_title",
        "category_id"
    ]

    feature_columns = numeric_features + categorical_features

    X = df[feature_columns]

    # Classification target
    y = df["viral"]


    # 4. Train-Test Split
    # ---------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )


    # 5. Preprocessing
    # ---------------------------------------------------------

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                StandardScaler(),
                numeric_features
            ),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            )
        ]
    )


    # Fit on training data
    X_train_processed = preprocessor.fit_transform(X_train)

    # Transform test data
    X_test_processed = preprocessor.transform(X_test)


    # 6. Train Logistic Regression Model
    # ---------------------------------------------------------

    model = LogisticRegression(
        max_iter=1000
    )

    model.fit(
        X_train_processed,
        y_train
    )


    # 7. Make Predictions
    # ---------------------------------------------------------

    y_pred = model.predict(X_test_processed)

    # Probability of viral = 1
    y_probability = model.predict_proba(
        X_test_processed
    )[:, 1]


    # 8. Calculate Evaluation Metrics
    # ---------------------------------------------------------

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred
    )

    recall = recall_score(
        y_test,
        y_pred
    )

    f1 = f1_score(
        y_test,
        y_pred
    )

    roc_auc = roc_auc_score(
        y_test,
        y_probability
    )


    # 9. Print Evaluation Metrics
    # ---------------------------------------------------------

    print("Logistic Regression Results")
    print("-" * 40)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-score : {f1:.4f}")
    print(f"ROC-AUC  : {roc_auc:.4f}")


    # 10. Confusion Matrix
    # ---------------------------------------------------------

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    print("\nConfusion Matrix:")
    print(cm)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Non-Viral", "Viral"]
    )

    disp.plot()

    plt.title("Confusion Matrix - Logistic Regression")
    plt.tight_layout()
    plt.show()


    # 11. ROC Curve
    # ---------------------------------------------------------

    fpr, tpr, thresholds = roc_curve(
        y_test,
        y_probability
    )

    plt.figure(figsize=(8, 6))

    plt.plot(
        fpr,
        tpr,
        label=f"ROC-AUC = {roc_auc:.4f}"
    )

    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        label="Random Classifier"
    )

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    plt.title("ROC Curve - Logistic Regression")

    plt.legend()

    plt.tight_layout()
    plt.show()


    # 12. Feature Coefficients
    # ---------------------------------------------------------

    feature_names = preprocessor.get_feature_names_out()

    coefficients = model.coef_[0]

    coefficient_df = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": coefficients
    })

    coefficient_df["Absolute_Coefficient"] = (
        coefficient_df["Coefficient"].abs()
    )

    coefficient_df = coefficient_df.sort_values(
        "Absolute_Coefficient",
        ascending=False
    )


    # 13. Display Top 15 Features
    # ---------------------------------------------------------

    print("\nTop 15 Features Influencing Virality:")
    print(
        coefficient_df[
            ["Feature", "Coefficient"]
        ].head(15).to_string(index=False)
    )


    # 14. Plot Feature Importance
    # ---------------------------------------------------------

    top_features = coefficient_df.head(15).sort_values(
        "Absolute_Coefficient"
    )

    plt.figure(figsize=(10, 7))

    plt.barh(
        top_features["Feature"],
        top_features["Coefficient"]
    )

    plt.title("Top 15 Logistic Regression Coefficients")

    plt.xlabel("Coefficient")

    plt.ylabel("Feature")

    plt.tight_layout()

    plt.show()


    # 15. Interpretation
    # ---------------------------------------------------------

    print("\nInterpretation:")

    print(
        "The Logistic Regression model performed well, with an accuracy "
        "of 93.95% and a ROC-AUC score of 0.9824. This shows that the "
        "model is able to distinguish between viral and non-viral videos "
        "quite effectively."
    )

    print(
        "From the coefficient plot, likes have the strongest influence "
        "on whether a video is predicted as viral. Some channel-related "
        "features also have a noticeable influence on the prediction."
    )

    print(
        "Positive coefficients indicate that a feature increases the "
        "likelihood of a video being classified as viral, while negative "
        "coefficients indicate a lower likelihood."
    )

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")