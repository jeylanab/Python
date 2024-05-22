import numpy as np 
# nd array created from list
arr1 = np.array([1, 2, 3, 4, 5])

# nd array created from list
arr2 = np.array([2,5,3,6,7])

print (arr1 + arr2)
print('this is my second file')
course = 'python'
print(len(course))

# some built in functions of the numpy array

arr3 = np.zeros((2,6))
arr4 = np.ones((4,2))
arr5 = np.full((2,2), 5)
arange = np.arange(0, 10, 2)     # Array with values 0 to 8 with step 2
print(arr3)
print(arr4)
print(arr5)
print(arange)

