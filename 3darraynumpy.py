import numpy as np

arr = np.array([[[1,2,3],
               [4,5,6]],

               [[7,8,9],
                [10,11,12]]])


print("3D Array:\n",arr)

for matrix in arr:
 print("\n2D matrix:\n",matrix)