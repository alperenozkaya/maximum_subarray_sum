import math
import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import threading


def main():

    A3 = create_random_array(10)
    A4 = create_random_array(50)
    A5 = create_random_array(100)
    A6 = create_random_array(500)
    A7 = create_random_array(1000)
    A8 = create_random_array(5000)
    A9 = create_random_array(10000)

    print('without thread')
    print_running_time(A3, 'n2')
    print_running_time(A4, 'n2')
    print_running_time(A5, 'n2')
    print_running_time(A6, 'n2')
    print_running_time(A7, 'n2')
    print_running_time(A8, 'n2')
    print_running_time(A9, 'n2')
    print('with thread')

    array_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    list_of_arrays = []
    for i in range(0, 7):
        list_of_arrays.append(create_random_array(array_sizes[i]))
    for i in range(0, 7):
        running_time_threads(list_of_arrays[i], 'n2')


# total_rt: list contains running time calculation of each threads
def running_time_threads(arr, cmplx):
    total_rt = []
    threads = []
    for i in range(0, 5):
        threads.append(threading.Thread(target=running_time_with_thread(arr, cmplx, total_rt)))
    for i in range(0, 5):
        threads[i].start()
    for i in range(0, 5):
        threads[i].join()
    sum = 0
    for i in range(len(total_rt)):
        sum += total_rt[i]
    exec_time = (sum / 5)
    exec_time_ms = int(float("%.2f" % (exec_time * 10 ** 6)))  # in ms

    print(exec_time_ms, 'ms')
    return exec_time_ms


def running_time_with_thread(arr, cmp, total_rt):  # cmp = complexity
    if cmp == 'n2':
        start = time.perf_counter()
        max_sum = max_subarray_sum_n2(arr)
        end = time.perf_counter()
        exec_time = end - start
        total_rt.append(exec_time)
        #print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds


def max_subarray_sum_n2(arr):
    max_sum = 0
    for i in range(0, len(arr) - 1):
        sum = 0
        for j in range(i, len(arr) - 1):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

def print_running_time(arr, cmp):  # cmp = complexity
    flag1 = True  # check whether the sum and time values already stored
    max_sum = 0  # hold the value to add to list
    if cmp == 'n2':
        sum = 0
        for i in range(0, 5):
            if flag1 is True:
                start = time.perf_counter()
                max_sum = max_subarray_sum_n2(arr)
                end = time.perf_counter()
                sum += (end - start)
                flag1 = False
            else:
                start = time.perf_counter()
                max_subarray_sum_n2(arr)
                end = time.perf_counter()
                sum += (end - start)
        exec_time = (sum / 5)
        exec_time_ms = int(float("%.2f" % (exec_time * 10 ** 6)))
        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds


def create_random_array(n):
    random_array = np.random.randint(low=-50, high=50, size=n) # creates an n-sized array with the random values
                                                               # between -50, 50
    return random_array


main()