import numpy as np


# Using matrix form
data_list=[1,2,3,4,5,6]

data_matrix=[data_list[i:i + 3] for i in range(0, len(data_list), 3)]
print("Reshaped list (2x3):")
print(data_matrix)
transposed_matrix=[[data_matrix[j][i] for j in range(len(data_matrix))] for i in range(len(data_matrix[0]))]
print("Transposed matrix (3x2):")
print(transposed_matrix)

# Using NumPy   
data_array=np.array([1,2,3,4,5,6])

reshaped_array=data_array.reshape((2,3))
print("Reshaped array (2x3):")
print(reshaped_array)

transposed_array=reshaped_array.T
print("Transposed array (3x2):")
print(transposed_array)