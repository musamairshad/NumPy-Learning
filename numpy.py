"""
NumPy => Numeric python.
Alternative to python list => NumPy Array.
Calculations over entire array's.
Easy and Fast.
NumPy Array's => Contains only one type.
"""

import numpy as np

# height = [1.73, 1.68, 1.71, 1.89, 1.79]
# np_height = np.array(height)
# weight = [65.4, 59.2, 63.6, 88.4, 68.7]
# np_weight = np.array(weight)
# bmi = np_weight / np_height ** 2 # This gives an error if you use regular python list's.
# print(bmi)
# # print(np_height, np_weight)

python_list = [1, 2, 3]
numpy_array1 = np.array([1, 2, 3])
numpy_array2 = np.array([1, 2, 3])
print(numpy_array1[numpy_array1 > 1])
# print(numpy_array1 > 1)
# print(numpy_array1 + numpy_array2)
# print(type(numpy_array))