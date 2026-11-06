"""
Problem 13: Convert Nested Tuple into Dictionary
Description: Convert a tuple containing key-value pairs into a dictionary.

Example:

Input: ((1, 'A'), (2, 'B'), (3, 'C'))

Output: {1: 'A', 2: 'B', 3: 'C'}
"""

def tuple_to_dictionary(tup):
    result = {}

    for key, value in tup:
        result[key] = value

    return result

tup = ((1, 'A'), (2, 'B'), (3, 'C'))

print("Dictionary:", tuple_to_dictionary(tup))