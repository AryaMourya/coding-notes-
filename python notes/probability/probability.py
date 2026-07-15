import random
import numpy as np

outcome = []
for i in range(10000):
    outcome.append(random.randint(1,6))

print(np.array(outcome).mean())