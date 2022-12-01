import math
import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import threading

def main():
    # initialize arrays
    A1 = np.array([-2, -5, 6, -2, -3, 1, 5, -6])  # 8
    A2 = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])  # 16
    A = []
    A.append(A1)
    A.append(A2)

    array_sizes =  [10, 25, 50, 100,250, 500, 1000,2500, 5000, 10000]

    for i in range(0, 2):
            print('A{0} max sub-array sum for N2 algorithm: {1}'.format(i + 1, max_subarray_sum_n2(A[i])))
            print('A{0} max sub-array sum for NLGN algorithm: {1}'.format(i + 1, max_subarray_sum_nlgn(A[i], 0, len(A[i]) - 1)))
            print('A{0} max sub-array sum for N algorithm: {1}'.format(i + 1, max_subarray_sum_n(A[i])))


                                                         # too much time to run
    list_of_arrays = []

    for i in range(len(array_sizes)):
        list_of_arrays.append(create_random_array(array_sizes[i]))

    list_sum_time_n2 = []  # stores the subarray sum and running time values indexes -> 0:sum 1:time
    list_sum_time_nlgn = []  # stores the subarray sum and running time values indexes -> 0:sum 1:time
    list_sum_time_n = []  # stores the subarray sum and running time values indexes -> 0:sum 1:time

    for i in range(0, 3):
        for j in range(len(list_of_arrays)):
            if i == 0:
                running_time_threads(list_of_arrays[j], 'n2', list_sum_time_n2)
            elif i == 1:
                running_time_threads(list_of_arrays[j], 'nlgn', list_sum_time_nlgn)
            else:
                running_time_threads(list_of_arrays[j], 'n', list_sum_time_n)

    # print the values calculated
    for i in range(0, 3):
        if i == 0:
            print('**** Values For n^2 Algorithm ****')
        elif i == 1:
            print('**** Values For nlogn Algorithm ****')
        else:
            print('**** Values For n Algorithm ****')
        for j in range(len(list_of_arrays)):
            if i == 0:
                print('For the size', array_sizes[j], 'Maximum Sum:', list_sum_time_n2[j][0],
                      'Running Time:', list_sum_time_n2[j][1], 'ms')
            elif i == 1:
                print('For the size', array_sizes[j], 'Maximum Sum:', list_sum_time_nlgn[j][0],
                      'Running Time:', list_sum_time_nlgn[j][1], 'ms')
            else:
                print('For the size', array_sizes[j], 'Maximum Sum:', list_sum_time_n[j][0],
                      'Running Time:', list_sum_time_n[j][1], 'ms')
    plot_running_time(list_sum_time_n2, list_sum_time_nlgn, list_sum_time_n, array_sizes)
def max_subarray_sum_n2(arr):
    max_sum = 0
    for i in range(0, len(arr) - 1):
        sum = 0
        for j in range(i, len(arr) - 1):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum


def max_subarray_sum_nlgn(arr, p, r):  # initially p:0 r:last index of array
    if p > r:
        return -math.inf
    elif p == r:
        return arr[p]
    else:
        q = int((p + r) / 2)
        return max(max_subarray_sum_nlgn(arr, p, q),
                   max_subarray_sum_nlgn(arr, q + 1, r),
                   find_max_sum(arr, p, q, r))


def find_max_sum(arr, p, q, r):  # nlgn
    sum = 0
    l_sum = -math.inf
    r_sum = -math.inf

    for i in range(q, p - 1, -1):  # search left part
        sum += arr[i]
        if sum > l_sum:
            l_sum = sum

    sum = 0
    for i in range(q, r + 1):
        sum += arr[i]
        if sum > r_sum:
            r_sum = sum

    return max(l_sum, r_sum, l_sum + r_sum - arr[q])



'''This implements kadane's algorithm, a linear time max sub-array finding algorithm.'''
def max_subarray_sum_n(arr):

    max_local = max_sum = arr[0]   # initial and global maximum sums.

    for i in range(1, len(arr)):
        max_local = max(arr[i], arr[i] + max_local) # compare previous max subarray with current value, if greater, update local

        if max_local > max_sum: # if current max is greater than max up to now, update global max.
            max_sum = max_local

    return max_sum

def create_random_array(n):
    random_array = np.random.randint(low=-50, high=50, size=n)  # creates an n-sized array with the random values
    # between -50, 50
    return random_array


# total_rt: list contains running time calculation of each threads
def running_time_threads(arr, cmplx, sum_time: list):
    total_t = []
    sum_lst = []
    threads = []
    for i in range(0, 5):
        threads.append(threading.Thread(target=running_time_with_thread(arr, cmplx, total_t, sum_lst)))
    for i in range(0, 5):
        threads[i].start()
    for i in range(0, 5):
        threads[i].join()
    time_sum = 0
    for i in range(len(total_t)):
        time_sum += total_t[i]

    exec_time = (time_sum / 5)
    exec_time_ms = int(float("%.2f" % (exec_time * 10 ** 6)))  # in ms
    # print(exec_time_ms, 'ms')
    arr_sum = sum_lst[0]
    sum_time.append([arr_sum, exec_time_ms])



def running_time_with_thread(arr, cmp, total_t: list, sum_lst: list):  # cmp = complexity t = time s = sum
    if cmp == 'n2':
        start = time.perf_counter()
        max_sum = max_subarray_sum_n2(arr)
        end = time.perf_counter()
        exec_time = end - start
        total_t.append(exec_time)
        sum_lst.append(max_sum)
    elif cmp == 'nlgn':
        start = time.perf_counter()
        max_sum = max_subarray_sum_nlgn(arr, 0, len(arr) - 1)
        end = time.perf_counter()
        exec_time = end - start
        total_t.append(exec_time)
        sum_lst.append(max_sum)
    elif cmp == 'n':
        start = time.perf_counter()
        max_sum = max_subarray_sum_n(arr)
        end = time.perf_counter()
        exec_time = end - start
        total_t.append(exec_time)
        sum_lst.append(max_sum)
    else:
        print('Wrong complexity')


def plot_running_time(lst_n2, lst_nlgn, lst_n, array_sizes):  # may be implemented
    rt_n2 = []
    rt_nlgn = []
    rt_n = []
    # extract running time from the lise
    for i in range(len(lst_n)):
        rt_n2.append(lst_n2[i][1])
    for i in range(len(lst_n)):
        rt_nlgn.append(lst_nlgn[i][1])
    for i in range(len(lst_n)):
        rt_n.append(lst_n[i][1])

    #array_sizes = [] #= np.array([10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000], dtype=np.int64)


    figure, axis = plt.subplots(2, 2, figsize=(10, 10))
    # For n^2 algorithm
    axis[0, 0].plot(array_sizes, rt_n2)
    axis[0, 0].set_title("n^2 Algorithm")
    axis[0, 0].set_ylim(0)

    # For nlogn algorithm
    axis[0, 1].plot(array_sizes, rt_nlgn)
    axis[0, 1].set_title("nlogn Algorithm")

    # For n algorithm
    axis[1, 0].plot(array_sizes, rt_n)
    axis[1, 0].set_title("n Algorithm")

    # To compare
    axis[1, 1].set_ylim(0, 100000)
    axis[1, 1].plot(array_sizes, rt_n2)
    axis[1, 1].plot(array_sizes, rt_nlgn)
    axis[1, 1].plot(array_sizes, rt_n)
    axis[1, 1].set_title("Three Algorithms")
    axis[1, 1].legend(['n^2', 'nlgn', 'n'], ncol=3, loc='upper left')

    plt.show()


main()
