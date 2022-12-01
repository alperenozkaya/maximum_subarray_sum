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

    A3 = create_random_array(10)
    A4 = create_random_array(50)
    A5 = create_random_array(100)
    A6 = create_random_array(500)
    A7 = create_random_array(1000)
    A8 = create_random_array(5000)
    A9 = create_random_array(10000)
    # A10 = create_random_array(50000)
    # A11 = create_random_array(100000)
    array_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    list_of_arrays = []

    for i in range(0, 7):
        list_of_arrays.append(create_random_array(array_sizes[i]))

    list_sum_time_n2 = []  # stores the subarray sum and running time values indexes -> 0:sum 1:time
    list_sum_time_nlgn = []  # stores the subarray sum and running time values indexes -> 0:sum 1:time
    list_sum_time_n = []  # stores the subarray sum and running time values indexes -> 0:sum 1:time

    #for i in range(0, 3):
    #    for j in range(len(list_of_arrays)):
    #        if i == 0:
    #            print_running_time(list_of_arrays[j], 'n2', list_sum_time_n2)
    #        elif i == 1:
    #            print_running_time(list_of_arrays[j], 'nlgn', list_sum_time_nlgn)
    #        else:
    #            print_running_time(list_of_arrays[j], 'n', list_sum_time_n)
    #plot_running_time(list_sum_time_n2, list_sum_time_nlgn, list_sum_time_n)

    for i in range(0, 3):
        for j in range(len(list_of_arrays)):
            if i == 0:
                running_time_threads(list_of_arrays[j], 'n2', list_sum_time_n2)
            elif i == 1:
                running_time_threads(list_of_arrays[j], 'nlgn', list_sum_time_nlgn)
            else:
                running_time_threads(list_of_arrays[j], 'n', list_sum_time_n)
    plot_running_time(list_sum_time_n2, list_sum_time_nlgn, list_sum_time_n)


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


def max_subarray_sum_n(arr):
    return 0


def print_max_sum(arr, cmp):  # cmp = complexity
    if cmp == 'n2':
        print(max_subarray_sum_n2(arr), 'n2')
    elif cmp == 'nlgn':
        print(max_subarray_sum_nlgn(arr, 0, len(arr) - 1), 'nlgn')
    elif cmp == 'n':
        print(max_subarray_sum_n(arr))
    else:
        print('Wrong complexity input!')


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
    print(exec_time_ms, 'ms')
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
    if cmp == 'n':
        start = time.perf_counter()
        max_sum = max_subarray_sum_n(arr)
        end = time.perf_counter()
        exec_time = end - start
        total_t.append(exec_time)
        sum_lst.append(max_sum)  # BETTER SOLUTION???????????????



def print_running_time(arr, cmp, st: list):  # cmp = complexity
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
        st.append([max_sum, exec_time_ms])
        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds

    elif cmp == 'nlgn':
        max_sum = 0  # hold the value to add to list
        sum = 0
        for i in range(0, 5):
            if flag1 is True:
                start = time.perf_counter()
                max_sum = max_subarray_sum_nlgn(arr, 0, len(arr) - 1)
                end = time.perf_counter()
                sum += (end - start)
                flag1 = False
            else:
                start = time.perf_counter()
                max_subarray_sum_nlgn(arr, 0, len(arr) - 1)
                end = time.perf_counter()
                sum += (end - start)
        exec_time = (sum / 5)
        exec_time_ms = int(float("%.2f" % (exec_time * 10 ** 6)))
        st.append([max_sum, exec_time_ms])
        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds
    elif cmp == 'n':
        max_sum = 0  # hold the value to add to list
        sum = 0
        for i in range(0, 5):
            if flag1 is True:
                start = time.perf_counter()
                max_sum = max_subarray_sum_n(arr)
                end = time.perf_counter()
                sum += (end - start)
                flag1 = False
            else:
                start = time.perf_counter()
                max_subarray_sum_n(arr)
                end = time.perf_counter()
                sum += (end - start)
        exec_time = (sum / 5)
        exec_time_ms = int(float("%.2f" % (exec_time * 10 ** 6)))
        # st.append([max_sum, exec_time_ms])
        st.append([0, 0])
        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds
    else:
        print('Wrong complexity input!')


def plot_running_time(lst_n2, lst_nlgn, lst_n):  # may be implemented
    rt_n2 = []
    rt_nlgn = []
    rt_n = []
    # extract running time from the lise
    for i in range(0, 7):
        rt_n2.append(lst_n2[i][1])
    for i in range(0, 7):
        rt_nlgn.append(lst_nlgn[i][1])
    for i in range(0, 7):
        rt_n.append(lst_n[i][1])

    array_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    plt.plot(array_sizes, rt_n2)
    plt.plot(array_sizes, rt_nlgn)
    plt.plot(array_sizes, rt_n)
    plt.legend(['n^2', 'nlogn', 'n'], ncol=3, loc='upper left')
    plt.show()


main()
