import numpy as np

array_str=np.array(['a','bc','def'],dtype='S3')
print(array_str)

# Using S5 datatype
arr_exercise_str = np.array(['apple', 'banana', 'cherry'], dtype='S5')
print(arr_exercise_str)

# Use S6 to avoid truncation
arr_exercise_str = np.array(['apple', 'banana', 'cherry'], dtype='S6')
print(arr_exercise_str)

# Use str to auto detect the string length
arr_exercise_str = np.array(['apple', 'banana', 'cherry'], dtype='str')
print(arr_exercise_str)
