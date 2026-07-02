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