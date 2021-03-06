#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if(index >= len(array)):
        return None
    if(array[index] == item):
        return index
    return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    middle = round((len(array)/2))
    bottom = 0
    top = len(array) - 1

    while bottom < top:
        if (item == array[middle]):
            return middle
        if (item < array[middle]):
            top = middle - 1
            middle = bottom + round((middle - bottom)/2)
        else:
            bottom = middle + 1
            middle = top - round((top - middle)/2)
        print('%d , %d , %d, ' % (bottom, middle, top))
    if (item == array[middle]):
        return middle
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # passed in empty set
    if len(array) < 1:
        return None

    # in case this is the first iteration
    if left == None:
        left = 0
        right = len(array) - 1
    # calculate middle using new fancy pythonic floor division
    middle = right - ((right - left) // 2)

    if array[middle] == item:
        return middle
    elif middle == left:
        return None
    elif array[middle] < item:
        return binary_search_recursive(array,item,middle+1,right)
    elif array[middle] > item:
        return binary_search_recursive(array, item, left, middle - 1)


    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
