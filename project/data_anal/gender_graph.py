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

    name = input("지역을 입력하세요 : ")
    location_index = df[df['행정구역'].str.contains(name, na=False)].index[0]

    male_df = df.iloc[location_index, 3:104]
    male_df = male_df * -1
    female_df = df.iloc[location_index, -101:]

    plt.barh(range(len(male_df)), male_df.values, label='Male', color='red')  # male_df.values로 변환
    plt.barh(range(len(female_df)), female_df.values, label='Female', color='blue')  # female_df.values로 변환

    plt.title('Comparison of Male and Female Data')
    plt.legend()

    plt.show()

def main() -> None:
    gender_analysis()


if __name__ == "__main__":
    main()