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

#itemsize
print(a2.itemsize)

#dtype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

#astype
print(a3.astype(np.int32))

### SCALAR OPERATIONS ###
""" Arthimetic operation"""
print(a1 + 2)
print(a2 * 3)

## relational

#
print(a2 + a2)

a4 = np.random.random((3,3))
a4 = np.round(a4 * 100)
print(a4)

"""max/min/sum/prod"""
print(np.max(a4))
print(np.min(a4))
print(np.sum(a4))
print(np.prod(a4,axis=0))

##Statical operation
"""mean/median/std/var"""
print(np.mean(a4))
print(np.median(a4))
print(np.std(a4))
print(np.var(a4))


##DOT Product##
a2= np.arange(12).reshape(3,4)
a3= np.arange(12,24).reshape(4,3)
print(np.dot(a2,a3))

#log and exponents
print(np.log(a4))
print(np.exp(a4))

# Round/floor/ceil
array5=np.round(np.random.random((2,3))*100)
print(array5)

#Indexing
a5 = np.arange(8).reshape(2,2,2)
print(a5)
print(a5[1,1,0])

#Slicing
"""slicing for 1D array"""
print(a1[2:5])
a6= np.arange(12).reshape(3,4)
"""slicing  for 2D array"""
print(a6)
print(a6[0,:])
print(a6[:,2])
print(a6[1:,1:3])
print(a6[::2,::3])
"""slicing for 3D array"""
print(a5[::2])
print(a5[::2,0,::2])

#Iteration
"""for 1D array"""
for i in a1:
    print(i)
"""for 2D array"""
for i in a6:
    print(i)
"""for 3D array"""
for i in a5:
    print(i)

for i in np.nditer(a5):
    print(i)


#Transpose
print(np.transpose(a6))
print(a6.T)

#Ravel
print(a6.ravel())

#Stacking
"""horizontal stacking"""
array1 = np.arange(12).reshape(3,4)
array2 = np.arange(12,24).reshape(3,4)
print(np.hstack((array1,array2)))
"""vertical stacking"""
print(np.vstack((array1,array2)))

#Spliting
"""horizontal spliting"""
print(np.hsplit(array1,2))
print(np.vsplit(array1,3))