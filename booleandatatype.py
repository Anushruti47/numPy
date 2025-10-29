import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10],dtype=int)

even_mask=(arr%2==0)
print(even_mask)