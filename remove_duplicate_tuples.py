"""
Problem 14: Remove Duplicate Tuples from List
Description: Remove duplicate tuples while preserving the original order.

Example:

Input: [(1, 2), (3, 4), (1, 2), (5, 6)]

Output: [(1, 2), (3, 4), (5, 6)]
"""

def remove_duplicate_tuples(tuples_list):
    result = []

    for tup in tuples_list:
        if tup not in result:
            result.append(tup)

    return result

tuples_list = [(1, 2), (3, 4), (1, 2), (5, 6)]

print("Unique Tuples:", remove_duplicate_tuples(tuples_list))