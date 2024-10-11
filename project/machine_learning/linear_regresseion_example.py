from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


a = 0.2
u = 10 * np.random.normal(size=(500, ))

x = np.arange(1, 501)
y = a * x + u

plt.scatter(x, y)
plt.show()


x = x.reshape(-1, 1) # 차원을 하나 늘려 줌, y와 1대1로 데이터가 대응되게끔.
# 학습용 데이터, 평가용 데이터를 나눔, 랜덤으로 뽑기 위해서 "suffle=ture"
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

plt.scatter(x_train, y_train)
plt.scatter(x_test, y_test)
plt.show()

model = LinearRegression()
model = model.fit(x_train, y_train)

print(model.coef_)
print(model.score(x_test, y_test))



