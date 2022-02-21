"""
Look at the numpy docs to explore all the ways which you can use numpy to generate tensors/matrices/arrays of random numbers
Create a matrix of random numbers with 4 rows and 6 columns
Index the element on the 3rd row, 2nd col
Index all of the even rows
Index all of the elements on even rows and odd columns
Index the elements along the diagonal
"""

from sqlite3 import Row
from tkinter.tix import ROW
import numpy as np

ran_matx = np.random.randint(0,1000,(4,6))
print(ran_matx)
print(ran_matx[2][1]) 
ran_matx.compress(Row%2==0,axis=0)
