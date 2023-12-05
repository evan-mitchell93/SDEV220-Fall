import numpy as np

"""#Working with Numpy

#our first array
arr = np.array([3,2,1,0,-1,-2,-3,-4,-5])

#print(arr.ndim)

#first 2-d array
arr_2d = np.array([[1,6,0],[0,1,0],[0,0,1]])
#print(arr_2d.ndim)

#access to 1d
print(arr[0])

#access to 2d
print(arr_2d[0,1])
#or
print(arr_2d[0][1])

#3d array

arr_3d = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])

#3d access
print(arr_3d[1,1,2])
#negative indexing works
print(arr_3d[1,1,-1])

#Slicing
#1d [start:stop:step]
print(arr[1::2])

#2d
#[(slice),(slice)]
print(arr_2d[1:, 1:])

test = np.array([1,2,"Hello"])
print(test.dtype)
print(arr_2d.dtype)

forced = np.array([1,2,3,'4'], dtype='i4')

data types in numpy
    i - integer
    b - boolean
    u - unsigned int
    f - float
    c - complex
    m - timedelta
    M - datetime
    O - object
    S - String
    U - unicode string
    V - void/other type fixed chunk memor

arr[0] = 10
print(arr)"""

"""looping_arr = np.array([[0,0],[0,0]])
for x in range(2):
    for y in range(2):
        looping_arr[x,y] = int(input("Enter a number: "))

print(looping_arr)"""
"""
option_two = np.empty([2,2],dtype="i4")
for x in range(2):
    for y in range(2):
        #validate that the data is a number here before
        #assigning it to the array.
        option_two[x,y] = int(input("enter more numbers"))"""
#print(option_two)

#copy original stays the same
"""x = option_two.copy()
x[0,0] = 100
print(option_two)
print(x)"""

#view changes show in both the original and view
"""v = x.view()
v[0,0] = 77
print(option_two)
print(x)
print(v)"""

#Joining arrays

arr1 = np.array([1,100,1000])
arr2 = np.array([2,200,2000])

conc = np.concatenate([arr1,arr2])
#print(conc)

#joining 2d
arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[7,8,9],[10,11,12]])

conc2 = np.concatenate((arr3,arr4),axis=1)


#split arrays
split_arr = np.array_split(conc,5)

#split 2d
split2 = np.array_split(conc2,2,axis=1)


#searching
searchable = np.array([2,1,0,7,5,10,11,-13])
indcs = np.where(searchable%2 == 0)
print(indcs)

#search sorted to insert
sorted = np.array([1,2,6,8,11])
x = np.searchsorted(sorted,5)
print(sorted)
print(x)

#sorting
print(np.sort(searchable))
print(searchable)

#filtering
#use a boolean index list
filt_arr = np.array([1,2,3,4])
bl = [True,False,False,True]
newarr = filt_arr[bl]
print(newarr)

bl = []
for element in filt_arr:
    if element % 2 == 1:
        bl.append(True)
    else:
        bl.append(False)
newarr = filt_arr[bl]
print(newarr)

newfilter = filt_arr %2 == 0

newarr = filt_arr[newfilter]
print(newfilter)
print(newarr)