import numpy as np
"""Advanced Indexing"""
#Normal indexing and slicing
a = np.arange(12).reshape(4,3)
print(a[1,2]) #indexing 
print(a[1:3,1:3]) #slicing

#Fancy indexing
print(a[[0,2,3]])
print(a[:,[0,2]])

"""how to genrate an np btw two no randomly"""
print(np.random.randint(1,100,24).reshape(6,4))

#Boolean Indexing
"""find all numbers greater than 50"""
a= np.random.randint(1,100,24).reshape(6,4)
print(a[a>50])
"""find out even numbers"""
print(a[a % 2==0])
"""find all numbers greater than 50 and are even """
print(a[(a > 50)&(a % 2==0)])
"""find all no not div by 7"""
print(a[a% 7!=0])

#Broadcasting
b = np.arange(6).reshape(2,3)
c = np.arange(6,12).reshape(2,3)
d = np.arange(3).reshape(1,3)
print(b)
print(c)
print(b +c)
print(b + d)

"""Broadcasting Examples"""
#example 1
a = np.arange(12).reshape(4,3)
b = np.arange(3)

print(a)
print(b)
print(a + b)

# Example 2
c = np.arange(3).reshape(1,3)
d = np.arange(3).reshape(3,1)

print(c)
print(d)
print(c + d)

#Example 3
e = np.array([1])
"""shape -> (1,1)"""
f = np.arange(4).reshape(2,2)
""" shape -> (2,2)"""

print(e)
print(f)
print(e + f)

g = np.arange(12).reshape(3,4)
h = np.arange(12).reshape(4,3)
#print(g + h) #[ this will show error because in both the case there is no 1 in one of thes
#  ]
