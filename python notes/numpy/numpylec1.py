#Creatig Numpy Arrays#
"""np.array"""
import numpy as np
a = np.array([1,2,3])
print(a)
print(type(a))

#2D and 3D
b = np.array([[1,2,3],[4,5,6]])
print(b)
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

#dtype(datatype as per as our requirement)

x=np.array([1,2,3],dtype=float)
y=np.array([1,2,3],dtype=bool)
k=np.array([1,2,3],dtype=complex)
print(x)
print(y)
print(k)


## np.range
