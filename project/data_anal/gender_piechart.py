import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_csv(name:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(name, encoding="cp949")
        print(f"'{os.path.basename(name)}'이 로드되었습니다.")
        return df
    except FileNotFoundError as e:
        print("해당 파일이 존재하지 않습니다.")
        return pd.DataFrame("[[]]")


def gender_analysis() -> None:
    df = load_csv("../../data/gender.csv")

    size = []
    name = input("지역을 입력하세요 : ")

    # pandas에서 문자열이 특정 열의 값에 포함되어 있는지를 확인하려면 == 대신 str.contains() 메서드를 사용해야 한다.
    # in은 파이썬의 기본 연산자로 사용되지만, pandas에서는 str.contains()가 문자열 비교에 더 적합하다.
    location_index = df[df['행정구역'].str.contains(name, na=False)].index[0]

    male_df = df.iloc[location_index, 1]
    female_df = df.iloc[location_index, -103]

    size.append(male_df)
    size.append(female_df)

    print(male_df)
    print(female_df)
    print(size)

    color = ['crimson', 'darkcyan']
    plt.axis('equal')

    plt.pie(size, labels=['Male', 'Female'], autopct='%.1f%%', colors=color, startangle=90)
    plt.title('Gender Ratio')
    plt.show()


def main() -> None:
    gender_analysis()


if __name__ == "__main__":
    main()