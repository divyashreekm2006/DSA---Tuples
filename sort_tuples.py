"""
Problem 10: Sort a List of Tuples by Second Item
Description: Sort a list of tuples based on the second element in ascending order.

Example:

Input: [(1, 3), (4, 1), (2, 2)]

Output: [(4, 1), (2, 2), (1, 3)]
"""

def sort_tuples(tuples_list):
    result = sorted(tuples_list, key=lambda x: x[1])

    return result

tuples_list = [(1, 3), (4, 1), (2, 2)]

print("Sorted Tuples:", sort_tuples(tuples_list))