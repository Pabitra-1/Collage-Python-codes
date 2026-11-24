import numpy as np
arr1 = np.array([5,42,30,2,1])
print("Original Array : ",arr1)
print("Sorted Array (Ascending) : ",np.sort(arr1))
print("Sorted Array (Descending) : ",np.sort(arr1)[::-1])
print("Sorted Indices (Ascending) : ",np.argsort(arr1))
print("Sorted Indices (Descending) : ",np.argsort(arr1)[::-1])