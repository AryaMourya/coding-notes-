import numpy as np

b = np.random.randint(1,100,24).reshape(6,4)

""" np.sort """
print(np.sort(b))
print(np.sort(b, axis=0)) ## axis = 0 (Coloumn-wise)
print(np.sort(b,axis=1)) ## axis = 1 (Row-wise)

""" np.append """
a = np.random.randint(1,100,12)
print(np.append(a,200))
print(np.append(b,np.ones((b.shape[0],1)),axis=1))
print(np.append(b,np.random.random((b.shape[0],1)),axis=1))

""" np.concatinate """
c= np.arange(6).reshape(2,3)
d =np.arange(6,12).reshape(2,3)
print(np.concatenate((c,d),axis=0))

"""np.unique"""
e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
f= np.array([[1,2,3,1],[1,2,3,2]])
print(e)
print(f)