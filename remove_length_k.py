"""
Problem 9: Remove Tuples of Length K
Description: Remove all tuples having length K from a list.

Example:

Input: ([(1, 2), (3, 4, 5), (6,), (7, 8)], 2)

Output: [(3, 4, 5), (6,)]
"""
def remove_length_k(tuples_list, k):
    result = []

    for tup in tuples_list:
        if len(tup) != k:
            result.append(tup)

    return result


tuples_list = [(1, 2), (3, 4, 5), (6,), (7, 8)]
k = 2

print("Result:", remove_length_k(tuples_list, k))