"""
Problem 12: Flatten Tuple of Lists to Tuple
Description: Convert a tuple containing multiple lists into a single flat tuple.

Example:

Input: ([1, 2], [3, 4], [5, 6])

Output: (1, 2, 3, 4, 5, 6)
"""
def flatten_tuple(tup):
    result = []

    for lst in tup:
        for element in lst:
            result.append(element)

    return tuple(result)


tup = ([1, 2], [3, 4], [5, 6])

print("Flattened Tuple:", flatten_tuple(tup))