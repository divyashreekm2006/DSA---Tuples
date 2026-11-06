"""
Problem 8: All Pair Combinations of Two Tuples
Description: Generate all possible pairs by combining elements from two tuples.

Example:

Input: ((1, 2), ('A', 'B'))

Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
"""
def pair_combinations(tup1, tup2):
    result = []

    for i in tup1:
        for j in tup2:
            result.append((i, j))

    return result

tup1 = (1, 2)
tup2 = ('A', 'B')

print("Pairs:", pair_combinations(tup1, tup2))