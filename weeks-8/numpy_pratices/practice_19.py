# Iterate on the elements of the following 3-D array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x[0][1])
    print(x[1][0])