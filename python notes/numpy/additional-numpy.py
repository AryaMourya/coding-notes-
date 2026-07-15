import numpy as np

b = np.random.randint(1,100,24).reshape(6,4)

""" np.sort() """
print(np.sort(b))
print(np.sort(b, axis=0)) ## axis = 0 (Coloumn-wise)
print(np.sort(b,axis=1)) ## axis = 1 (Row-wise)

""" np.append() """
a = np.random.randint(1,100,12)
print(np.append(a,200))
print(np.append(b,np.ones((b.shape[0],1)),axis=1))
print(np.append(b,np.random.random((b.shape[0],1)),axis=1))

""" np.concatinate() """
c= np.arange(6).reshape(2,3)
d =np.arange(6,12).reshape(2,3)
print(np.concatenate((c,d),axis=0))

"""np.unique()"""
e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
f= np.array([[1,2,3,1],[1,2,3,2]])
print(e)
print(f)
print(np.unique(e))
print(np.unique(f))

"""np.expand_dims()"""
print(np.expand_dims(a,axis=0))
print(np.expand_dims(a,axis=1))

"""np.where()"""
## find all indices with value greater than 50
print(np.where(a>50))

## Replace all values > 50 with 0
"""np.where(condition,true,false)"""
print(np.where(a>50,0,a))

## Replace all value divded by 2 with 0
print(np.where(a%2==0,0,a))

"""np.argmax"""
print(np.argmax(e))
print(np.argmax(b,axis=0)) # for columns
print(np.argmax(b,axis=1)) # for rows

"""np.argmin"""
print(np.argmin(e))
print(np.argmin(b,axis=0))
print(np.argmin(b,axis=1))

"""np.cumsum"""
i= np.arange(7,14)
print(i)
print(np.cumsum(i))
print(np.cumsum(c,axis=0))
print(np.cumsum(c,axis=1))

"""np.cumprod"""
print(np.cumprod(i))
print(np.cumprod(c,axis=0))
print(np.cumprod(c,axis=1))

"""np.percentile"""
print(a)
print(np.percentile(a,100)) # max number in array for 100 percentile
print(np.percentile(a,0)) # min number in array for 0 percentile
print(np.percentile(a,50))

"""np.histogram"""
print(np.histogram(a,bins=[0,50,100]))

""" np.corrcoef """
salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])

print(np.corrcoef(salary,experience))

""" np.isin """
items =[10,20,30,40,50,60,70,80,90,100]
print(np.isin(a,items))
print(a[np.isin(a,items)])

""" np.flip """
print(np.flip(a))
print(np.flip(c,axis=0)) # row flip
print(np.flip(c,axis=1)) # col flip

""" np.put """
np.put(a,[0,1],[110,530])
print(a)

""" np.delete """
print(np.delete(a,0)) 

""" SET FUCTIONS """
## np.union1d ##

g = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

print(np.union1d(g,n))

## np.intersect1d ##
print(np.intersect1d(g,n))

## np.setdiff1d ## (not common func)
print(np.setdiff1d(g,n))

## np.setxor1d ## remove the common term of two array and create new array
print(np.setxor1d(g,n))

