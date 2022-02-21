"""
Write a NumPy program to add a border of zeros to the outside elements of an array of size (20, 20).
Can you do it with an 3D array of dimension (20, 20, 20)?
Try the same with an array of dimension (20, 40, 10)
"""

import numpy as np

ran_matx = np.random.randint(0,10,(5,5,5))
print(ran_matx)
print(ran_matx.ndim)
print(ran_matx.shape)
zero_matr = np.zeros(shape=(ran_matx.shape[0]+2, ran_matx.shape[1]+2, ran_matx.shape[2]+2),dtype=np.int16)
print(np.add(ran_matx, zero_matr))
# print(zero_matr)