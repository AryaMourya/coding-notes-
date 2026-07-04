import numpy as np

#### Working with mathmathical formula ####
"""sum"""
a = np.arange(10)
print(np.sum(a))  # sum will add all the number in the array 
print(np.sin(a)) # sin of all the value of array

"""Sigmoid"""
def sigmoid(array):
    return 1/(1 + np.exp(array))

b = np.arange(10)
sigmoid(b)
