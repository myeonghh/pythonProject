import  keras
from keras import layers

model = keras.Sequential([
    layers.Dense(units=16, input_shape=(16,), activation="relu"), # 파라미터 개수: 16 * 16 + 16(편향) = 272
    layers.Dense(units=128, activation="relu"), # 파라미터 개수: 16 * 128 + 128 = 2172
    layers.Dense(units=512, activation="relu"), # 파라미터 개수: 128 * 512 + 512 = 66048
    layers.Dense(units=10, activation="softmax") # 파라미터 개수: 512 * 10 + 10 = 5130
])

model.summary()