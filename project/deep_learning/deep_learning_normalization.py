import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import  numpy as np
import  keras
from keras import layers

keras.utils.set_random_seed(0)

load_data = load_diabetes()
x = load_data.data
y = load_data.target
norm = layers.Normalization()
norm.adapt(y)
denorm = layers.Normalization(invert=True)
denorm.adapt(y)
y_ = norm(y)
size = x.shape

model = keras.Sequential([
    layers.Dense(units=10, input_shape=(size[1],), activation="relu"),
    layers.Dense(units=256, activation="relu"),
    layers.Dense(units=1),
])

model.compile(optimizer="adam", loss="mae")

history = model.fit(x, y_, epochs=100)

result = model.predict(x)
result_ = denorm(result.reshape(-1))
print(result_)
x_ = np.arange(1, 11)
plt.plot(x_, y[:10], x_, result_[:10])
plt.show()