#numpy is a library used for working with arrays, linear algebra, and others.
#arrays may be faster than lists because they are stored in contiguous memory locations (easier to find the next element)
#It was also optimized for newer CPU architectures.

import numpy as np

arr = np.array([[0,0,0],[0,0,0],[0,0,0]])
print(arr)

for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        if x == y:
            arr[x,y] = 1

print(arr)
