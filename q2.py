import numpy as np

#how to find the size of any array



# null_vector=np.zeros([5,5], dtype='int8')

# null_vectors=np.zeros([5,5], dtype='int8')

# print("The size :", null_vector.__sizeof__())
# print(null_vector)

null_arr=np.zeros([2])

# print(null_arr.dtype)
# print(null_arr.itemsize)
print(null_arr)
print(f"Total elements size : {null_arr.nbytes}")   #because it is 64 bits-
print(f"Item size of each element : {null_arr.itemsize}")
print(f"Total size : {null_arr.size * null_arr.itemsize}")
