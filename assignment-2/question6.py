import pandas as pd

def read_csv():
    file_path = 'Credit.csv'
    df = pd.read_csv(file_path)

    print(df)


def main():
    read_csv()

if __name__ == "__main__":
    main()