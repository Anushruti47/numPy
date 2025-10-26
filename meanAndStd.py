import math
import random
import numpy as np

#1 Using python lists
data_list=[random.random() for i in range(1000)]

mean_list=sum(data_list)/len(data_list)
var_list=sum((x - mean_list) ** 2 for x in data_list) / len(data_list)
std_list=math.sqrt(var_list)
print("Mean (list):",mean_list)
print("Standard Deviation (list):",std_list)

#2 Using NumPy
data_array=np.random.random(1000)

mean_array=np.mean(data_array)
std_array=np.std(data_array)
print("Mean (NumPy):",mean_array)
print("Standard Deviation (NumPy):",std_array)