import matplotlib.pyplot as plt
import numpy as np

A = np.array([10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000], dtype=np.int64)  # dtype for n^2


n2 = np.power(A, 2)  # n^2 run time
nlgn = np.log10(A) * A
n = A
print(n2)
print(nlgn)
print(n)



figure, axis = plt.subplots(2, 2, figsize=(10, 10))


#for i in range(0, 2):
#    for j in range(0, 2):
 #       axis[i, j].set_ylim(0, 100000)

# For n^2 algorithm
axis[0, 0].plot(A, n2)
axis[0, 0].set_title("n^2 Algorithm")
axis[0, 0].set_ylim(0)

# For nlogn algorithm
axis[0, 1].plot(A, nlgn)
axis[0, 1].set_title("nlogn Algorithm")

# For n algorithm
axis[1, 0].plot(A, n)
axis[1, 0].set_title("n Algorithm")

# To compare
axis[1, 1].set_ylim(0, 100000)
axis[1, 1].plot(A, n2)
axis[1, 1].plot(A, nlgn)
axis[1, 1].plot(A, n)
axis[1, 1].set_title("Three Algorithms")

axis[1, 1].legend(['n^2', 'nlgn', 'n'], ncol=3, loc='upper left')

plt.show()