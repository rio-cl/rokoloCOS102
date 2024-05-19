import numpy as np

classNum = int(input("How many students are in the CSC 102 class?"))

class_arr = np.array(classNum)

if (class_arr == 1):
    print("There is only ", class_arr, "student in CSC 102 class" )
else:
    print("There are", class_arr, "students in CSC 102 class" )