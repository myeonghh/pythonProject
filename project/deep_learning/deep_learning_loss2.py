import matplotlib.pyplot as plt
import  numpy as np
from sklearn.datasets import load_iris
import  keras
from keras import layers

keras.utils.set_random_seed(0)

load_data = load_iris()
x = load_data.data
y = load_data.target
classes = len(np.unique(y))
size = x.shape

model = keras.Sequential([
    layers.Dense(units=4, input_shape=(size[1],), activation="relu"),
    layers.Dense(units=32, activation="relu"),
    layers.Dense(units=64, activation="relu"),
    layers.Dense(units=classes, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
history = model.fit(x, y, epochs=100)

history_ = history.history
plt.plot(history_["loss"])
plt.show()

plt.plot(history_["accuracy"])
plt.show()