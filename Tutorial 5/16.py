import numpy as np

a = np.random.randint(0, 21, size=(3, 3))
b = np.random.randint(0, 21, size=(3, 3))

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)

add = a + b
print("\nMatrix Addition (A + B):\n", add)

product = np.dot(a, b)
print("\nMatrix Multiplication (A x B):\n", product)

# Transpose of the Product Matrix
transpose = product.T
print("\nTranspose of Product Matrix:\n", transpose)
