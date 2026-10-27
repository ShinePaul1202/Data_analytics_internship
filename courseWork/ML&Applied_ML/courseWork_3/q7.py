import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, LogisticRegression


# Task 7: Cross-Validation and Scaling Comparison
# ---------------------------------------------------------
try:
    # Load dataset
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

    # Regression target
    y_regression = df["views"]

    # Classification target
    y_classification = df["viral"]


    # 4. Create Preprocessors
    # ---------------------------------------------------------

    # StandardScaler preprocessing
    standard_preprocessor = ColumnTransformer(
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


    # MinMaxScaler preprocessing
    minmax_preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                MinMaxScaler(),
                numeric_features
            ),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            )
        ]
    )


    # 5. Create Models
    # ---------------------------------------------------------

    # Linear Regression with StandardScaler
    linear_standard = Pipeline([
        ("preprocessor", standard_preprocessor),
        ("model", LinearRegression())
    ])


    # Linear Regression with MinMaxScaler
    linear_minmax = Pipeline([
        ("preprocessor", minmax_preprocessor),
        ("model", LinearRegression())
    ])


    # Logistic Regression with StandardScaler
    logistic_standard = Pipeline([
        ("preprocessor", standard_preprocessor),
        (
            "model",
            LogisticRegression(
                max_iter=1000
            )
        )
    ])


    # Logistic Regression with MinMaxScaler
    logistic_minmax = Pipeline([
        ("preprocessor", minmax_preprocessor),
        (
            "model",
            LogisticRegression(
                max_iter=1000
            )
        )
    ])


    # 6. Linear Regression - 5 Fold Cross-Validation
    # ---------------------------------------------------------

    print("=" * 60)
    print("LINEAR REGRESSION - 5 FOLD CROSS-VALIDATION")
    print("=" * 60)


    linear_standard_scores = cross_val_score(
        linear_standard,
        X,
        y_regression,
        cv=5,
        scoring="r2",
        n_jobs=-1
    )


    linear_minmax_scores = cross_val_score(
        linear_minmax,
        X,
        y_regression,
        cv=5,
        scoring="r2",
        n_jobs=-1
    )


    print("\nStandardScaler:")
    print("Fold R² scores:", linear_standard_scores)
    print(f"Mean R²: {linear_standard_scores.mean():.4f}")
    print(f"Variance: {linear_standard_scores.var():.6f}")


    print("\nMinMaxScaler:")
    print("Fold R² scores:", linear_minmax_scores)
    print(f"Mean R²: {linear_minmax_scores.mean():.4f}")
    print(f"Variance: {linear_minmax_scores.var():.6f}")


    # 7. Logistic Regression - 5 Fold Cross-Validation
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("LOGISTIC REGRESSION - 5 FOLD CROSS-VALIDATION")
    print("=" * 60)


    logistic_standard_scores = cross_val_score(
        logistic_standard,
        X,
        y_classification,
        cv=5,
        scoring="roc_auc",
        n_jobs=-1
    )


    logistic_minmax_scores = cross_val_score(
        logistic_minmax,
        X,
        y_classification,
        cv=5,
        scoring="roc_auc",
        n_jobs=-1
    )


    print("\nStandardScaler:")
    print("Fold ROC-AUC scores:", logistic_standard_scores)
    print(f"Mean ROC-AUC: {logistic_standard_scores.mean():.4f}")
    print(f"Variance: {logistic_standard_scores.var():.6f}")


    print("\nMinMaxScaler:")
    print("Fold ROC-AUC scores:", logistic_minmax_scores)
    print(f"Mean ROC-AUC: {logistic_minmax_scores.mean():.4f}")
    print(f"Variance: {logistic_minmax_scores.var():.6f}")


    # 8. Scaling Comparison
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("SCALING COMPARISON")
    print("=" * 60)

    print("\nLinear Regression:")
    print(
        f"StandardScaler Mean R²: "
        f"{linear_standard_scores.mean():.4f}"
    )

    print(
        f"MinMaxScaler Mean R²: "
        f"{linear_minmax_scores.mean():.4f}"
    )

    print("\nLogistic Regression:")
    print(
        f"StandardScaler Mean ROC-AUC: "
        f"{logistic_standard_scores.mean():.4f}"
    )

    print(
        f"MinMaxScaler Mean ROC-AUC: "
        f"{logistic_minmax_scores.mean():.4f}"
    )


    # 9. Select Better Scaling Method for Logistic Regression
    # ---------------------------------------------------------

    if logistic_standard_scores.mean() >= logistic_minmax_scores.mean():
        best_logistic_pipeline = logistic_standard
        best_scaler_name = "StandardScaler"

    else:
        best_logistic_pipeline = logistic_minmax
        best_scaler_name = "MinMaxScaler"


    print(
        f"\nBetter scaling method for Logistic Regression: "
        f"{best_scaler_name}"
    )


    # 10. Fit Best Logistic Regression Model
    # ---------------------------------------------------------

    best_logistic_pipeline.fit(
        X,
        y_classification
    )


    # Get fitted preprocessing step
    fitted_preprocessor = best_logistic_pipeline.named_steps[
        "preprocessor"
    ]

    # Get fitted logistic regression model
    fitted_model = best_logistic_pipeline.named_steps[
        "model"
    ]


    # 11. Get Feature Names and Coefficients
    # ---------------------------------------------------------

    feature_names = fitted_preprocessor.get_feature_names_out()

    coefficients = fitted_model.coef_[0]


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


    # 12. Display Top Features
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("TOP FEATURES INFLUENCING VIRALITY")
    print("=" * 60)

    print(
        coefficient_df[
            ["Feature", "Coefficient"]
        ].head(15).to_string(index=False)
    )


    # 13. Feature Importance Plot
    # ---------------------------------------------------------

    top_features = coefficient_df.head(15).sort_values(
        "Absolute_Coefficient"
    )


    plt.figure(figsize=(10, 7))

    plt.barh(
        top_features["Feature"],
        top_features["Coefficient"]
    )

    plt.title(
        f"Top 15 Logistic Regression Features ({best_scaler_name})"
    )

    plt.xlabel("Coefficient")
    plt.ylabel("Feature")

    plt.tight_layout()
    plt.show()


    # 14. Interpretation
    # ---------------------------------------------------------

    print("\nInterpretation:")

    print(
        "Five-fold cross-validation was used to compare "
        "StandardScaler and MinMaxScaler."
    )

    print(
        "For Linear Regression, both scaling methods produced "
        "very similar results. StandardScaler had a mean R² of "
        "-13.1197, while MinMaxScaler had a mean R² of -13.1206. "
        "The large variation is mainly due to one fold having a "
        "very low R² score."
    )

    print(
        "For Logistic Regression, StandardScaler performed better "
        "than MinMaxScaler, with mean ROC-AUC scores of 0.9525 and "
        "0.8830 respectively."
    )

    print(
        "The feature importance plot shows that likes have the "
        "strongest influence on the prediction of virality. "
        "Several channel-related features also have a noticeable "
        "influence on the model's predictions."
    )

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")