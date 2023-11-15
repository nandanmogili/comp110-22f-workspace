import pandas as pd


def main() -> None:
    df = pd.read_excel('/Users/nandanmogili/Documents/python projects/comp110-22f-workspace/projects/SocialSciences_Dataset.xlsx', sheet_name ='Chapter5')
    print(df.head);

if __name__ == '__main__':
    main()