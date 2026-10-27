import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# Task 2: Explore Distributions and Relationships
# ---------------------------------------------------------
try:
    # Load dataset
    df = pd.read_csv("USvideos.csv")


    # 1. Create title_length
    # ---------------------------------------------------------

    df["title_length"] = df["title"].str.len()


    # 2. Create days_since_publish
    # ---------------------------------------------------------

    df["trending_date"] = pd.to_datetime(
        df["trending_date"],
        format="%y.%d.%m"
    )

    df["publish_time"] = pd.to_datetime(
        df["publish_time"],
        utc=True
    )

    df["days_since_publish"] = (
        df["trending_date"].dt.tz_localize("UTC")
        - df["publish_time"].dt.normalize()
    ).dt.days


    # 3. Histogram of Views
    # ---------------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.hist(df["views"], bins=50)

    plt.title("Distribution of YouTube Video Views")
    plt.xlabel("Views")
    plt.ylabel("Number of Videos")

    plt.show()


    # 4. Scatterplot: Likes vs Views
    # ---------------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["likes"],
        df["views"],
        alpha=0.5
    )

    plt.title("Likes vs Views")
    plt.xlabel("Likes")
    plt.ylabel("Views")

    plt.show()


    # 5. Correlation Matrix
    # ---------------------------------------------------------

    correlation_features = [
        "views",
        "likes",
        "dislikes",
        "comment_count",
        "title_length",
        "days_since_publish"
    ]

    correlation_matrix = df[correlation_features].corr()

    print("\nCorrelation Matrix:")
    print(correlation_matrix)


    # 6. Display Correlation Heatmap
    # ---------------------------------------------------------

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")

    plt.show()


    # 7. Observations
    # ---------------------------------------------------------

    print("\nObservations:")

    print(
        "1. Likes have a strong positive relationship with views "
        "(correlation = 0.83). This suggests that videos receiving "
        "more likes generally tend to get more views."
    )

    print(
        "2. Comment count has a moderate positive relationship with views "
        "(correlation = 0.56). This indicates that videos with more "
        "comments generally tend to have higher views."
    )

    print(
        "3. Dislikes have a moderate positive relationship with views "
        "(correlation = 0.44). Although the relationship is positive, "
        "it is weaker than the relationship between likes and views."
    )

    print(
        "4. Title length has a very weak negative relationship with views "
        "(correlation = -0.06), so the length of the title does not appear "
        "to have much of a linear relationship with views."
    )

    print(
        "5. Days since publication has almost no relationship with views "
        "(correlation = -0.02) in this dataset."
    )

    print(
        "6. The histogram shows that most videos have relatively low views, "
        "while a small number of videos have extremely high views. "
        "Therefore, the distribution of views is strongly right-skewed."
    )

except FileNotFoundError:
    print("Error: USvideos.csv was not found.")

except KeyError as e:
    print(f"Error: Required column {e} is missing.")

except ValueError as e:
    print(f"Error: Invalid value or data format: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
# ---------------------------------------------------------
# Note about duration
# ---------------------------------------------------------
"""
The  USvideos.csv dataset i downloded from the kaggle dataset does not contain a duration column, 
so duration is not included in the correlation matrix.
"""
