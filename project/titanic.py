import pandas as pd
import matplotlib.pyplot as plt

data_path = "../../../../titanic.csv"
df:pd.DataFrame = pd.read_csv(data_path, encoding="utf8")
print(df.describe())

print(df.columns * 10)