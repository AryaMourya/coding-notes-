## speed of excution 
a= [i for i in range(1000000)]
b = [i for i in range(1000000, 2000000)]

c =[]
import time

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time()-start)

import numpy as np
a = np.arange(1000000)
b = np.arange(1000000,2000000)

start = time.time()
c = a + b
print(time.time() - start)

# memory
a= [i for i in range(1000000)]
import sys

print(sys.getsizeof(a))

a = np.arange(1000000,dtype=np.int32)
print(sys.getsizeof(a))