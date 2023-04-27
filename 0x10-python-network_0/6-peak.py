#!/usr/bin/python3
"""Defines a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_helper(array, low, high):
    """Find a peak in a list of unsorted integers."""
    if low == high:
        return array[low]
    mid = (low + high) // 2
    if array[mid] > array[mid + 1]:
        return find_peak_helper(array, low, mid)
    return find_peak_helper(array, mid + 1, high)
