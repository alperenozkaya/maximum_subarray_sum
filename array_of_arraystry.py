import math

import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt



def create_random_array(n):
    random_array = np.random.randint(low=-50, high=50, size=n) # creates an n-sized array with the random values
                                                               # between -50, 50
    return random_array

list_of_arrays = []
array_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
for i in range(0, 7):
    list_of_arrays.append(create_random_array(array_sizes[i]))


print(list_of_arrays)
