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


## np.arange
range = np.arange(1,11)
print(range)
R = np.arange(1,11,2)
print(R)

#with reshape
r = np.arange(1,11).reshape(5,2)
print(r)

#np.ones and np.zeroes
print(np.ones((3,4)))
print(np.zeros((2,3)))

#np.random
print(np.random.random((2,3)))

#np.linspace
print(np.linspace(-10,10,3))
print(np.linspace(-5,5,15))

#np.identity
print(np.identity(2))

### Array Attributes
a1 =np.arange(10)
a2 =np.arange(12,dtype=float).reshape(3,4)
a3 =np.arange(8).reshape(2,2,2)


#ndim( tell the dimension of array)
print(a2.ndim)
print(a3.ndim)

#shape
print(a1.shape)
print(a2.shape)
print(a3.shape)

#size
print(a1.size)
print(a2.size)
print(a3.size)