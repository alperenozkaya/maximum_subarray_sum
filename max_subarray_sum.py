import numpy
import numpy as np
import time
import matplotlib.pyplot


def main():
    A1 = np.array([-2, -5, 6, -2, -3, 1, 5, -6])
    A3 = np.array([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
    A4 = create_random_array(100)  # np array with 16 random values
    print_max_sum(A1, 'n2')
    print_max_sum(A3, 'n2')
    print_running_time(A1, 'n2')
    print_running_time(A3, 'n2')
    print_running_time(A4, 'n2')
    max_subarray_sum_n(A1)

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

    test = [2, 3 ,1, 2, 5, 6, 9, 4] # TODO: I will delete this
    counting_sort(test, 1)  # TODO: I will also, delete this

    dummy = 0

'''This is used to find the largest number, and by that extend, largest number of digits.'''
def extract_max(arr):

    max_val = arr[0]

'''Counting sort will run in each digit.'''
def counting_sort(arr, digit):

    # Array C to store the occurrences
    C =np.empty(10); C.fill(0)

    # Array for cumulative sum
    CC = np.empty(10); CC.fill(0)

    B = np.empty(len(arr)); B.fill(0)

    for i in range(len(arr)): # calculate C
        C[arr[i]] +=1

    # finds cumulative sum array, and by extension; place indicators for each element
    cumulative_sum = 0 # calculate CC
    for i in range(len(C)):
        cumulative_sum += C[i]
        CC[i] = cumulative_sum

    CC -=1 # subtract 1 from CC to get actual indicies, not indicators

    # puts new elements in place.
    arr_index = len(arr) - 1
    while arr_index >= 0:
        index = int(CC[arr[arr_index]])
        B[index] = arr[arr_index]
        CC[arr[arr_index]] -= 1
        arr_index -=1


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
        for i in range(0, 5):
            start = time.perf_counter()
            max_subarray_sum_n2(arr)
            end = time.perf_counter()
            sum += (end - start)
        exec_time = (sum / 5)

        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds

    elif cmp == 'nlgn':
        sum = 0
        for i in range(0, 5):
            start = time.perf_counter()
            max_subarray_sum_n2(arr)
            end = time.perf_counter()
            sum += (end - start)
        exec_time = (sum / 5)

        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds
    elif cmp == 'n':
        sum = 0
        for i in range(0, 5):
            start = time.perf_counter()
            max_subarray_sum_n2(arr)
            end = time.perf_counter()
            sum += (end - start)
        exec_time = (sum / 5)

        print("%.2f" % (exec_time * 10 ** 6), 'ms')  # running time in miliseconds
    else:
        print('Wrong complexity input!')


def plot_running_time(arr):  # may be implemented
    dummy = 0


main()









