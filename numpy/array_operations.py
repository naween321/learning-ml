import numpy as np

a = np.array([1, 2, 3])  # One dimensional array
print(a[2])

a = np.array([[1, 2], [3, 4]])  # two-dimensional array
print(a.ndim)  # gives the array dimension
print(a.size)
print(a.shape)

print(np.zeros((3, 4)))  # 3 rows 4 columns 0 matrix
print(np.ones((2, 2)))  # one matrix
print(np.arange(1, 5))  # similar to python range
print(a.ravel())  # similar to flat=true which gives a list

a.sum(axis=0)  # sums the column
a.sum(axis=1)  # sums the row

np.sqrt(a)  # sqrt is not array method. It's called by numpy
np.std(a)  # standard deviation

a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])
print(a + b)
print(a * b)
print(a / b)
print(a.dot(b))
