import numpy as np

arr = np.array([[0,0,0],[0,0,0],[0,0,0]])

print(arr)

for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        if x == y:
            arr[x,y] = 1

print(arr)