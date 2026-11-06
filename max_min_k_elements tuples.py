"""
Problem 2: Maximum and Minimum K Elements in Tuple
Description: Find the K smallest and K largest elements in a tuple.

Example:

Input: ((4, 1, 7, 9, 2, 6), 2)

Output: ([1, 2], [7, 9])

"""

def max_min_k_elements(tup, k):
    sorted_tup = sorted(tup)

    smallest = sorted_tup[:k]
    largest = sorted_tup[-k:]

    return smallest, largest

tup = (4, 1, 7, 9, 2, 6)
k = 2

result = max_min_k_elements(tup, k)

print("Smallest elements:", result[0])
print("Largest elements:", result[1])