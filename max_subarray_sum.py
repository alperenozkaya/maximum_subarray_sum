import numpy as np
import time
import matplotlib.pyplot


def main():
    A1 = np.array([-2, -5, 6, -2, -3, 1, 5, -6])
    A3 = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
    A4 = create_random_array(16)  # np array with 16 random values
    print_max_sum(A1, 'n2')
    print_max_sum(A3, 'n2')
    print_running_time(A1, 'n2')
    print_running_time(A3, 'n2')
    print_running_time(A4, 'n2')


def max_subarray_sum_n2(arr):
    max_sum = 0
    for i in range(0, len(arr) - 1):
        sum = 0
        for j in range(i, len(arr) - 1):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

def max_subarray_sum_nlgn(arr):
    dummy = 0

def max_subarray_sum_n(arr):
    dummy = 0


def print_max_sum(arr, cmp):  # cmp = complexity
    if cmp == 'n2':
        print(max_subarray_sum_n2(arr))
    elif cmp == 'nlgn':
        print(max_subarray_sum_nlgn(arr))
    elif cmp == 'n':
        print(max_subarray_sum_n(arr))
    else:
        print('Wrong complexity input!')


def create_random_array(n):
    random_array = np.random.randint(low=-50, high=50, size=n) # creates an n-sized array with the random values
                                                               # between -50, 50
    return random_array


def print_running_time(arr, cmp):  # cmp = complexity
    if cmp == 'n2':
        sum = 0
        for i in range(0, 10):
            start = time.perf_counter()
            max_subarray_sum_n2(arr)
            end = time.perf_counter()
            sum += (end - start)
        exec_time = (sum / 10)

        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds

    elif cmp == 'nlgn':
        sum = 0
        for i in range(0, 10):
            start = time.perf_counter()
            max_subarray_sum_n2(arr)
            end = time.perf_counter()
            sum += (end - start)
        exec_time = (sum / 10)

        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds
    elif cmp == 'n':
        sum = 0
        for i in range(0, 10):
            start = time.perf_counter()
            max_subarray_sum_n2(arr)
            end = time.perf_counter()
            sum += (end - start)
        exec_time = (sum / 10)

        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds
    else:
        print('Wrong complexity input!')


def plot_running_time(arr):  # may be implemented
    dummy = 0


main()









