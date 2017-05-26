import numpy as np

arr = np.arange(5)
np.save ('myarray', arr)

np.load('myarray.npy')
# npy is the file extension

np.savez('ziparray.npz', x=arr1, y=arr2)
# zip file extensions with multiple arrays

archive_array = np.load('ziparray.npz')
archive_array['x']

np.savetxt('mytextarray.txt', arr, delimiter=',')

arr = np.loadtxt('mytextarray.txt', delimiter=',')
