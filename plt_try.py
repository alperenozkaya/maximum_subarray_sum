import matplotlib.pyplot as plt
import numpy as np

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1100]
B = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
C = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331]
D = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 3331]


plt.plot(A, B)
plt.plot(A, C)
plt.plot(A, D)
plt.legend(['n^2', 'nlogn', 'n'], ncol=3, loc='upper left')
plt.show()