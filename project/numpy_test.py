import numpy as np

x1 = np.add(1, 2)
print(x1)

x2 = np.add([1], [2])
print(x2)

x3 = np.add([[1]], [[2]])
print(x3)

x4 = np.add([[1, 2]], [[3], [4]])
print(x4)

x5 = np.array([[1, 2]]) + np.array([[3], [4]])
print(x5)

x6 = np.zeros(4)
print(x6)

x7 = np.ones((1, 4), dtype=np.int32)
print(x7)

x8 = np.arange(1, 9, dtype="int64").reshape((2, 4))
print(x8)

print(x8[0])
print(x8[0][0])
print(x8[0][1:3])
print(np.sum(x8))
print(np.mean(x8))
print(np.var(x8))
print(np.max(x8))
print(np.argmax(x8))