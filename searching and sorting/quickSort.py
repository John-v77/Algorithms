"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    if len(array) <=1: return array

    smaller_numbers_arr = []
    bigger_numbers_arr = []
    sorted_arr = []
    pivot = array[-1]

    for num in array:
        if num > pivot: bigger_numbers_arr.append(num)
        if num < pivot: smaller_numbers_arr.append(num)
        else: sorted_arr.append(num)
    
    return quicksort(smaller_numbers_arr) + sorted_arr + quicksort(bigger_numbers_arr)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))