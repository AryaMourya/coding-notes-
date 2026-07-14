import numpy as np

b = np.random.randint(1,100,24).reshape(6,4)
print(np.sort(b))
print(np.sort(b, axis=0)) ## axis = 0 (Coloumn-wise)
print(np.sort(b,axis=1)) ## axis = 1 (Row-wise)

""" np.append """
a = np.random.randint(1,100,12)
print(np.append(a,200))
print(np.append(b,np.ones((b.shape[0],1)),axis=1))
print(np.append(b,np.random.random((b.shape[0],1)),axis=1))

""" np.concatinate """