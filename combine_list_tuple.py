"""
Problem 4: Combine List and Tuple
Description: Combine the elements of a list and a tuple into a single list.

Example:

Input: ([1, 2, 3], (4, 5, 6))

Output: [1, 2, 3, 4, 5, 6]
"""

def combine_list_tuple(arr, tup):
    result = list(arr) + list(tup)

    return result


# Main program
arr = [1, 2, 3]
tup = (4, 5, 6)

result = combine_list_tuple(arr, tup)

print("Combined:", result)