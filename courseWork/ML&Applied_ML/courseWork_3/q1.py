import pandas as pd


# ---------------------------------------------------------
# Task 1: Load Dataset and Define Targets
# ---------------------------------------------------------
try:
    # Load the dataset
    df = pd.read_csv("USvideos.csv")


    # 1. Display Dataset Shape
    # ---------------------------------------------------------

    print("Dataset Shape:")
    print(df.shape)


    # 2. Display First 5 Rows
    # ---------------------------------------------------------

    print("\nFirst 5 Rows:")
    print(df.head())



    # 3. Display Dataset Information
    # ---------------------------------------------------------

    print("\nDataset Information:")
    df.info()


    # 4. Display Statistical Summary
    # ---------------------------------------------------------

    print("\nStatistical Summary:")
    print(df.describe())

    # 5. Define Regression Target
    # ---------------------------------------------------------

    regression_target = "views"

    print("\nRegression Target:")
    print(regression_target)


    # 6. Calculate Top 25% Quantile of Views
    # ---------------------------------------------------------

    top_25_quantile = df["views"].quantile(0.75)

    print("\nTop 25% Views Quantile:")
    print(top_25_quantile)


    # 7. Create Viral Classification Target
    # ---------------------------------------------------------

    # Viral = 1 if views are greater than the top 25% quantile
    # Viral = 0 otherwise

    df["viral"] = (df["views"] > top_25_quantile).astype(int)


    # 8. Display Viral Column
    # ---------------------------------------------------------

    print("\nFirst 5 Rows with Viral Column:")
    print(df[["views", "viral"]].head())


    # 9. Display Viral Class Counts
    # ---------------------------------------------------------

    print("\nViral Class Counts:")
    print(df["viral"].value_counts())


    # 10. Display Final Dataset Shape
    # ---------------------------------------------------------

    print("\nFinal Dataset Shape:")
    print(df.shape)

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")