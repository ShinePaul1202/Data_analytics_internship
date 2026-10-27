import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


# ---------------------------------------------------------
# Task 4: Preprocess Features
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


    # 2. Create Classification Target
    # ---------------------------------------------------------

    top_25_quantile = df["views"].quantile(0.75)

    df["viral"] = (
        df["views"] > top_25_quantile
    ).astype(int)


    # 3. Select Input Features
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


    # 4. Split Dataset into Training and Testing Sets
    # ---------------------------------------------------------

    X_train, X_test, y_reg_train, y_reg_test, y_cls_train, y_cls_test = train_test_split(
        X,
        y_regression,
        y_classification,
        test_size=0.20,
        random_state=42
    )


    # 5. Create Preprocessing Pipeline
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


    # 6. Fit Preprocessor on Training Data
    # ---------------------------------------------------------

    X_train_processed = preprocessor.fit_transform(X_train)

    X_test_processed = preprocessor.transform(X_test)


    # 7. Display Results
    # ---------------------------------------------------------

    print("Original Dataset Shape:")
    print(df.shape)

    print("\nTraining Data Shape:")
    print(X_train.shape)

    print("\nTesting Data Shape:")
    print(X_test.shape)

    print("\nProcessed Training Data Shape:")
    print(X_train_processed.shape)

    print("\nProcessed Testing Data Shape:")
    print(X_test_processed.shape)


    # 8. Display Target Shapes
    # ---------------------------------------------------------

    print("\nRegression Training Target Shape:")
    print(y_reg_train.shape)

    print("\nRegression Testing Target Shape:")
    print(y_reg_test.shape)

    print("\nClassification Training Target Shape:")
    print(y_cls_train.shape)

    print("\nClassification Testing Target Shape:")
    print(y_cls_test.shape)


    # 9. Check StandardScaler Results
    # ---------------------------------------------------------

    # Convert the first five numeric columns of the processed
    # training data to a DataFrame for inspection.

    scaled_numeric = X_train_processed[:, :len(numeric_features)].toarray()

    scaled_numeric_df = pd.DataFrame(
        scaled_numeric,
        columns=numeric_features
    )

    print("\nScaled Numeric Features - First 5 Rows:")
    print(scaled_numeric_df.head())

    print("\nScaled Numeric Feature Means:")
    print(scaled_numeric_df.mean())

    print("\nScaled Numeric Feature Standard Deviations:")
    print(scaled_numeric_df.std())


    # 10. Display Classification Target Distribution
    # ---------------------------------------------------------

    print("\nClassification Target Distribution - Training:")
    print(y_cls_train.value_counts())


    print("\nTask 4 preprocessing completed successfully.")

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")