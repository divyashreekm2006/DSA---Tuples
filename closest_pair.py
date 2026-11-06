"""
Problem 5: Closest Pair to Kth Index Element in Tuple
Description: Find the closest lower and upper elements around the element at index K.

Example:

Input: ((10, 20, 25, 30, 40), 2)

Output: (20, 30)
"""

def closest_pair(tup, k):
    target = tup[k]

    lower = [x for x in tup if x < target]
    upper = [x for x in tup if x > target]

    if not lower or not upper:
        return None

    closest_lower = max(lower)
    closest_upper = min(upper)

    return closest_lower, closest_upper


tup = (10, 20, 25, 30, 40)
k = 2

print("Closest Pair:", closest_pair(tup, k))