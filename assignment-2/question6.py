import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def find_lowest_median(df):
    numeric_cols = df.select_dtypes(include=['number'])
    medians = numeric_cols.median()
    
    min_median_column = medians.idxmin()
    min_median_value = medians.min()
    
    return min_median_column, min_median_value

def find_greatest_range(df):
    numeric_cols = df.select_dtypes(include=['number'])
    
    ranges = numeric_cols.max() - numeric_cols.min()
    
    max_range_column = ranges.idxmax()
    max_range_value = ranges.max()
    
    return max_range_column, max_range_value

def calculate_variance_limit(df):
    # Check if the 'Limit' column exists in the DataFrame
    if 'Limit' in df.columns:
        # Calculate the variance of the 'Limit' column
        variance = df['Limit'].var()
        return variance
    else:
        return "Column 'Limit' not found in the DataFrame"

def calculate_std_income_balance(df):
    # Calculate standard deviation for 'Income' and 'Balance'
    if 'Income' in df.columns and 'Balance' in df.columns:
        std_income = df['Income'].std()
        std_balance = df['Balance'].std()
        return std_income, std_balance
    else:
        return "Column 'Income' or 'Balance' not found in the DataFrame"

def compare_cv_income_balance(df):
    # Check if 'Income' and 'Balance' exist
    if 'Income' in df.columns and 'Balance' in df.columns:
        # Calculate coefficient of variation (CV = std / mean)
        cv_income = df['Income'].std() / df['Income'].mean()
        cv_balance = df['Balance'].std() / df['Balance'].mean()
        
        # Determine which has the greater CV
        if cv_income > cv_balance:
            greater_cv = 'Income'
        else:
            greater_cv = 'Balance'
        
        return greater_cv, cv_income, cv_balance
    else:
        return "Column 'Income' or 'Balance' not found in the DataFrame"

def plot_histogram_limit(df):
    # Check if the 'Limit' column exists in the DataFrame
    if 'Limit' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.hist(df['Limit'], bins=30, color='skyblue', edgecolor='black')
        plt.title('Histogram of Credit Limits')
        plt.xlabel('Credit Limit')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        plt.show()
    else:
        print("Column 'Limit' not found in the DataFrame")

def plot_boxplot_balance(df):
    # Check if the required columns exist in the DataFrame
    if 'Balance' in df.columns and 'Student' in df.columns:
        plt.figure(figsize=(10, 6))
        
        # Create the boxplot
        sns.boxplot(x='Student', y='Balance', data=df, palette={'Yes': 'skyblue', 'No': 'salmon'})
        
        # Set title and labels
        plt.title('Boxplot of Balance by Student Status')
        plt.xlabel('Student Status')
        plt.ylabel('Balance')
        plt.grid(axis='y', alpha=0.75)
        plt.show()
    else:
        print("Required columns 'Balance' or 'Student' not found in the DataFrame")

def read_csv():
    file_path = 'Credit.csv'
    df = pd.read_csv(file_path)
    return df

def main():
    df = read_csv()

    # a. Finding variable with the lowest median
    min_var, min_value = find_lowest_median(df)
    print(f'Var with lowest median value: {min_var}, value: {min_value}')

    # b. Finding variable with the greatest range
    max_range_var, max_value = find_greatest_range(df)
    print(f'Var with greatest range: {max_range_var}, value: {max_value}')

    # c. Calculating variance of 'Limit'
    variance = calculate_variance_limit(df)
    print(f"Limit's variance: {variance}")

    # d. Calculating standard deviation for 'Income' and 'Balance'
    std_income, std_balance = calculate_std_income_balance(df)
    print(f"Standard deviation of Income: {std_income}")
    print(f"Standard deviation of Balance: {std_balance}")

    # e. Comparing coefficient of variation (CV) between 'Income' and 'Balance'
    greater_cv, cv_income, cv_balance = compare_cv_income_balance(df)
    print(f"Greater CV between Income and Balance: {greater_cv}")
    print(f"Income CV: {cv_income}, Balance CV: {cv_balance}")

    # f. What does this coefficient tell us about the variables?

    # g. Histogram of Limit
    plot_histogram_limit(df)
    # WHAT CAN WE SAY ABOUT THIS VARIABLE?

    # h. Boxplot
    plot_boxplot_balance(df)
if __name__ == "__main__":
    main()