## Numpy array and basics

import numpy as np

#creating array from list 
arr_1d = np.array([1,2,3,4,5])
print("1D array:",arr_1d)

arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D array:",arr_2d)  

### Lists vs numpy array

py_list = [1,2,3]
print("python list multiplication ", py_list * 2)

np_array = np.array([1,2,3]) #element wise multiplication #
print("python list multiplication ", np_array * 2)

import time
start = time.time()
py_list = [1*2 for i in range(1000000) ]
print(time)