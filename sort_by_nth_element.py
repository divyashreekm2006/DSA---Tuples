"""
Problem 15: Sort Tuple List by Nth Element
Description: Sort a list of tuples based on the element at index N.

Example:

Input: ([(1, 5, 3), (2, 2, 4), (3, 4, 1)], 1)

Output: [(2, 2, 4), (3, 4, 1), (1, 5, 3)]

"""

def sort_by_nth_element(tuples_list, n):
    result = sorted(tuples_list, key=lambda x: x[n])

    return result

tuples_list = [(1, 5, 3), (2, 2, 4), (3, 4, 1)]
n = 1

print("Sorted Tuples:", sort_by_nth_element(tuples_list, n))
    