import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Task 1: Load Dataset and Display First 5 Rows
# ============================================================

def load_dataset(file_path):
    """Load the CSV dataset into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def display_first_five_rows(df):
    """Return the first five rows of the dataset."""
    return df.head()


# Task 2: Clean Dataset
# ============================================================

def clean_dataset(df):
    """
    Clean the dataset by:
    1. Removing duplicate rows.
    2. Converting numeric columns to numeric data types.
    3. Removing rows containing missing values.
    """

    cleaned_df = df.copy()

    # Remove duplicate rows
    cleaned_df = cleaned_df.drop_duplicates()

    # Columns that should contain numeric data
    numeric_columns = [
        "Year",
        "Engine Size (L)",
        "Horsepower",
        "Torque (lb-ft)",
        "0-60 MPH Time (seconds)",
        "Price (in USD)"
    ]

    # Convert numeric columns
    for column in numeric_columns:

        # Convert values to strings first
        cleaned_df[column] = (
            cleaned_df[column]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
            .str.strip()
        )

        # Convert to numeric
        cleaned_df[column] = pd.to_numeric(
            cleaned_df[column],
            errors="coerce"
        )

    # Remove rows containing missing values
    cleaned_df = cleaned_df.dropna()

    return cleaned_df




# Task 3: Summary Statistics
# ============================================================

def calculate_summary_statistics(df):
    """
    Calculate mean, median, mode, standard deviation,
    and range for numeric columns.
    """

    numeric_df = df.select_dtypes(include=np.number)

    summary = pd.DataFrame(index=numeric_df.columns)

    summary["Mean"] = numeric_df.mean()
    summary["Median"] = numeric_df.median()
    summary["Mode"] = numeric_df.mode().iloc[0]
    summary["Standard Deviation"] = numeric_df.std()
    summary["Range"] = numeric_df.max() - numeric_df.min()

    return summary


# Task 4: Average Price by Car Make
# ============================================================

def calculate_average_price_by_make(df):
    """Calculate the average price for each car make."""

    average_price = (
        df.groupby("Car Make")["Price (in USD)"]
        .mean()
        .sort_values(ascending=False)
    )

    return average_price


# Task 5: Average Horsepower by Year
# ============================================================

def calculate_average_horsepower_by_year(df):
    """Calculate the average horsepower for each year."""

    average_horsepower = (
        df.groupby("Year")["Horsepower"]
        .mean()
        .sort_index()
    )

    return average_horsepower


# Task 6: Scatter Plot and Linear Regression
# ============================================================

def create_price_horsepower_plot(df):
    """
    Create a scatter plot of price versus horsepower
    and add a linear regression line using NumPy polyfit().
    """

    x = df["Horsepower"].to_numpy()
    y = df["Price (in USD)"].to_numpy()

    # Calculate the slope and intercept using polyfit()
    slope, intercept = np.polyfit(x, y, 1)

    # Calculate predicted price values
    regression_line = slope * x + intercept

    # Sort values so the regression line is displayed correctly
    sort_index = np.argsort(x)

    plt.figure(figsize=(10, 6))

    plt.scatter(
        x,
        y,
        alpha=0.7,
        label="Sports Cars"
    )

    plt.plot(
        x[sort_index],
        regression_line[sort_index],
        linewidth=2,
        label="Linear Regression Line"
    )

    plt.xlabel("Horsepower")
    plt.ylabel("Price (USD)")
    plt.title("Price vs Horsepower")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()

    return slope, intercept


# Task 7: Histogram of 0-60 MPH Times
# ============================================================

def create_mph_histogram(df):
    """
    Create a histogram of 0-60 MPH times
    with bins of size 0.5 seconds.
    """

    times = df["0-60 MPH Time (seconds)"]

    # Determine the minimum and maximum values
    minimum = np.floor(times.min() * 2) / 2
    maximum = np.ceil(times.max() * 2) / 2

    # Create bins with a width of 0.5 seconds
    bins = np.arange(
        minimum,
        maximum + 0.5,
        0.5
    )

    plt.figure(figsize=(10, 6))

    plt.hist(
        times,
        bins=bins,
        edgecolor="black"
    )

    plt.xlabel("0-60 MPH Time (seconds)")
    plt.ylabel("Number of Cars")
    plt.title("Distribution of 0-60 MPH Times")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    plt.show()

    return bins


# Task 8: Filter and Sort Cars
# ============================================================

def filter_and_sort_expensive_cars(df):
    """
    Filter cars with price greater than $500,000
    and sort them by horsepower in descending order.
    """

    expensive_cars = df[
        df["Price (in USD)"] > 500000
    ].sort_values(
        by="Horsepower",
        ascending=False
    )

    return expensive_cars


# Task 9: Export Cleaned Dataset
# ============================================================

def export_cleaned_dataset(df, output_file):
    """Export the cleaned dataset to a new CSV file."""

    df.to_csv(
        output_file,
        index=False
    )

    return output_file


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    # Name of the downloaded Kaggle CSV file
    input_file = r"C:\sabudh_internship\python_class\courseWork\python\courseWork_4\Sport car price.csv"

    # Name of the output CSV file
    output_file = "cleaned_sport_car_prices.csv"

    try:

        # 1. Load Dataset
        # ----------------------------------------------------

        df = load_dataset(input_file)

        print("=" * 70)
        print("TASK 1: FIRST 5 ROWS OF THE DATASET")
        print("=" * 70)

        print(display_first_five_rows(df))


        # 2. Clean Dataset
        # ----------------------------------------------------

        cleaned_df = clean_dataset(df)

        print("\n" + "=" * 70)
        print("TASK 2: CLEANED DATASET")
        print("=" * 70)

        print("Original number of rows:", len(df))
        print("Number of rows after cleaning:", len(cleaned_df))

        print("\nCleaned dataset:")
        print(cleaned_df.head())


        # 3. Summary Statistics
        # ----------------------------------------------------

        summary_statistics = calculate_summary_statistics(
            cleaned_df
        )

        print("\n" + "=" * 70)
        print("TASK 3: SUMMARY STATISTICS")
        print("=" * 70)

        print(summary_statistics)


        # 4. Average Price by Car Make
        # ----------------------------------------------------

        average_price = calculate_average_price_by_make(
            cleaned_df
        )

        print("\n" + "=" * 70)
        print("TASK 4: AVERAGE PRICE BY CAR MAKE")
        print("=" * 70)

        print(average_price)


        # 5. Average Horsepower by Year
        # ----------------------------------------------------

        average_horsepower = calculate_average_horsepower_by_year(
            cleaned_df
        )

        print("\n" + "=" * 70)
        print("TASK 5: AVERAGE HORSEPOWER BY YEAR")
        print("=" * 70)

        print(average_horsepower)


        # 6. Scatter Plot and Regression Line
        # ----------------------------------------------------

        print("\n" + "=" * 70)
        print("TASK 6: PRICE VS HORSEPOWER")
        print("=" * 70)

        slope, intercept = create_price_horsepower_plot(
            cleaned_df
        )

        print("Regression slope:", slope)
        print("Regression intercept:", intercept)


        # 7. Histogram
        # ----------------------------------------------------

        print("\n" + "=" * 70)
        print("TASK 7: 0-60 MPH HISTOGRAM")
        print("=" * 70)

        create_mph_histogram(cleaned_df)

        print("Histogram created successfully.")


        # 8. Filter and Sort
        # ----------------------------------------------------

        expensive_cars = filter_and_sort_expensive_cars(
            cleaned_df
        )

        print("\n" + "=" * 70)
        print("TASK 8: CARS ABOVE $500,000")
        print("=" * 70)

        print(expensive_cars)


        # 9. Export Dataset
        # ----------------------------------------------------

        exported_file = export_cleaned_dataset(
            cleaned_df,
            output_file
        )

        print("\n" + "=" * 70)
        print("TASK 9: DATASET EXPORT")
        print("=" * 70)

        print(
            "Cleaned dataset successfully exported to:",
            exported_file
        )


    # --------------------------------------------------------
    # Error Handling
    # --------------------------------------------------------

    except FileNotFoundError:
        print(
            "Error: Dataset file was not found."
        )
        print(
            "Make sure the CSV file is in the same folder "
            "as this Python program."
        )

    except KeyError as error:
        print(
            "Error: A required column was not found:",
            error
        )

    except pd.errors.EmptyDataError:
        print(
            "Error: The CSV file is empty."
        )

    except pd.errors.ParserError:
        print(
            "Error: The CSV file could not be parsed correctly."
        )

    except ValueError as error:
        print(
            "ValueError:",
            error
        )

    except Exception as error:
        print(
            "An unexpected error occurred:",
            error
        )
