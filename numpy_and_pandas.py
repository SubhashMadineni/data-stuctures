# -*- coding: utf-8 -*-
"""numpy and pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s8YMJx22zDcNynm9AyKPzz6Zvbz5Lt2I
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

list1 = [1,2,3]

array = np.array(list1)
array

list1 = [1,2,3]
list2 = [4,5,6]

array = np.array([list1,list2])
array

list1 = [1,2,3]
list2 = [4,5,6]

array = np.hstack([list1,list2])
array

list1 = [1,2,3]
list2 = [4,5,6]

array = np.vstack([list1,list2]).reshape(3,2)
array

list1 = [[1,2],[3,4],[5,6]]
list2 = [[7,8],[9,10],[11,12]]

array = np.hstack([list1,list2])
array

list1 = [[1,2],[3,4],[5,6]]
list2 = [[7,8],[9,10],[11,12]]

array = np.vstack([list1,list2]).reshape(4,3)
array

list1 = [[1,2],[3,4],[5,6]]
list2 = [[7,8],[9,10],[11,12]]

array2 = np.hstack([list1,list2]).reshape(4,3)
array2

np.zeros(3)

list1 = [[1,2],[3,4],[5,6]]
list2 = [[7,8],[9,10],[11,12]]

array = np.hstack([list1,list2])
array

array = np.random.randint(40,100,10)
array.max()

vector = np.array(range(10))
my_slice = vector[3:7]
my_slice[:] = 20
print(vector)

matrix

matrix = np.array(range(1,10)).reshape((3,3))
#matrix[0,0]
#matrix[0][0] 
#matrix[2,2]  
# matrix[2][2] 

output = np.array([1,2,3]).reshape(3,1)
output

matrix[2:3,:3]



