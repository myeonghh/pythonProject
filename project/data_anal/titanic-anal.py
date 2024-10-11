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
        return pd.DataFrame()


def survived_gender():
    df = load_csv("../../data/titanic.csv")

    print(df)
    print(df.describe())

    male_survive_cnt = len(df[(df['Survived'] == 1) & (df['Sex'] == 'male')])
    femail_survive_cnt = df[(df['Survived'] == 1) & (df['Sex'] == 'female')].shape[0] # shape = (행 개수, 열 개수) 여기서는 행 개수를 구하기 때문에 shpae[0]을 씀

    size = [male_survive_cnt, femail_survive_cnt]
    plt.axis('equal')
    plt.pie(size, labels=['Male', 'Female'], autopct='%.1f%%', colors=['lightblue', 'hotpink'], startangle=90)
    plt.legend()
    plt.title('Titanic Survived Ratio')
    plt.show()

def survived_probability():
    df=load_csv('../../data/titanic.csv')

    size = []

    print(len(df[df['Survived'] == 1]))
    print(len(df[df['Survived'] == 0]))

    live = len(df[df['Survived'] == 1])
    die = len(df[df['Survived'] == 0])

    size.append(live)
    size.append(die)

    color = ['crimson', 'yellow']
    plt.axis('equal')
    plt.pie(size, labels=['live', 'die'], autopct='%.1f%%', colors=color, startangle=90)
    plt.title("survive")
    plt.show()

def titanic_prob(target:str, live:bool=True, graph:str="pie"):
    df = load_csv('../../data/titanic.csv')
    if live: a, b = "Live", 1
    else: a, b = "Die", 0
    size = []

    unique_value:np.array = df[target].unique()
    unique_value = unique_value[~pd.isnull(unique_value)]
    for v in unique_value:
        v1 = len(df[(df['Survived'] == b) & (df[target] == v)])
        size.append(v1)

    if graph == "pie":
        plt.pie(size, labels=unique_value, autopct='%.1f%%', startangle=90)
        plt.title(f"{target} {a} Prob.")
        plt.show()
    elif graph == "bar":
        plt.bar(unique_value, size)
        plt.title(f"{target} {a} Prob.")
        plt.show()


def main() -> None:
    survived_probability()
    survived_gender()
    titanic_prob("Pclass", True, "pie")

if __name__ == "__main__":
    main()