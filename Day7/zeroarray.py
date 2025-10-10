import numpy as np

print("-----------------for ones-------------------")

zeros = np.zeros((2,3))

print(zeros)

print("-----------------for ones-------------------")

import numpy as np
ones = np.zeros((3,3))

print(ones)


print("-----------------Arange-------------------")

arange_arr = np.arange(0,10,3)
print(arange_arr)


print("-----------------random numbers-------------------")

random_arr = np.random.rand(3,3)
print(random_arr)

print("-----------------Element wise addition-------------------")

a = np.array([1,2,3])
b = np.array([4,5,6])

c = a + b
# c = a * b
print(c)