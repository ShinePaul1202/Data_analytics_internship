import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# ---------------------------------------------------------
# Task 5: Linear Regression
# ---------------------------------------------------------
try:
    # Load the dataset
    df = pd.read_csv("USvideos.csv")


    # 1. Create Required Features
    # ---------------------------------------------------------

    # Calculate title length
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

    # Calculate days since publication
    df["days_since_publish"] = (
        df["trending_date"].dt.tz_localize("UTC")
        - df["publish_time"].dt.normalize()
    ).dt.days


    # 2. Select Features and Target
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
    y = df["views"]


    # 3. Split Data into Training and Testing Sets
    # ---------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )


    # 4. Preprocess Features
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

    # Fit preprocessing on training data
    X_train_processed = preprocessor.fit_transform(X_train)

    # Transform testing data
    X_test_processed = preprocessor.transform(X_test)


    # 5. Train Linear Regression Model
    # ---------------------------------------------------------

    model = LinearRegression()

    model.fit(
        X_train_processed,
        y_train
    )


    # 6. Predict Views on Test Data
    # ---------------------------------------------------------

    y_pred = model.predict(X_test_processed)


    # 7. Evaluate the Model
    # ---------------------------------------------------------

    mse = mean_squared_error(y_test, y_pred)

    rmse = np.sqrt(mse)

    mae = mean_absolute_error(y_test, y_pred)

    r2 = r2_score(y_test, y_pred)


    # 8. Print Regression Metrics
    # ---------------------------------------------------------

    print("Linear Regression Results")
    print("-" * 40)

    print(f"MSE  : {mse:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"MAE  : {mae:.2f}")
    print(f"R²   : {r2:.4f}")


    # 9. Get Feature Names and Coefficients
    # ---------------------------------------------------------

    feature_names = preprocessor.get_feature_names_out()

    coefficients = model.coef_

    coefficient_df = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": coefficients
    })

    # Calculate absolute coefficient values
    coefficient_df["Absolute_Coefficient"] = (
        coefficient_df["Coefficient"].abs()
    )

    # Sort by absolute coefficient
    coefficient_df = coefficient_df.sort_values(
        "Absolute_Coefficient",
        ascending=False
    )

    # 10. Display Top 15 Features
    # ---------------------------------------------------------

    print("\nTop 15 Features Influencing Views:")

    print(
        coefficient_df[
            ["Feature", "Coefficient"]
        ].head(15).to_string(index=False)
    )




    # 11. Plot Feature Coefficients
    # ---------------------------------------------------------

    top_features = coefficient_df.head(15).sort_values(
        "Absolute_Coefficient"
    )

    plt.figure(figsize=(10, 7))

    plt.barh(
        top_features["Feature"],
        top_features["Coefficient"]
    )

    plt.title("Top 15 Linear Regression Coefficients")
    plt.xlabel("Coefficient")
    plt.ylabel("Feature")

    plt.tight_layout()
    plt.show()


    # 12. Brief Comment
    # ---------------------------------------------------------

    print("\nBrief Comment:")

    print(
        "The coefficient plot shows that channel-related features "
        "have the largest coefficients, suggesting that the channel "
        "associated with a video has a strong influence on predicted views."
    )

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
