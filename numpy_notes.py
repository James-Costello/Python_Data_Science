import numpy as np

arr = np.arange(5)
np.save ('myarray', arr)

np.load('myarray.npy')
# npy is the file extension

np.savez('ziparray.npz', x=arr1, y=arr2)
