import random
import time
import numpy as np

data_list=[random.random() for i in range(100000)]
start=time.time()
mean_list=sum(data_list)/len(data_list)
end=time.time()
print("Mean (list):",mean_list)
print("Time taken (list):",end-start)

data_array=np.random.random(1000000)
start=time.time()
mean_array=np.mean(data_array)
end=time.time()
print("Mean (array):",mean_array)
print("Time taken (array):",end-start)

