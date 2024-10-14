import pandas as pd

def find_lowest_median(df):
    numeric_cols = df.select_dtypes(include=['number'])
    medians = numeric_cols.median()
    
    min_median_column = medians.idxmin()
    min_median_value = medians.min()
    
    return min_median_column, min_median_value

def read_csv():
    file_path = 'Credit.csv'
    df = pd.read_csv(file_path)
    return df


def main():
    df = read_csv()
    min_var, min_value = find_lowest_median(df)
    print(f'var with lowest median value: {min_var}, value: {min_value}')

if __name__ == "__main__":
    main()