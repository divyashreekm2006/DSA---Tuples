"""
Problem 6: Join Tuples Having Similar Initial Elements
Description: Combine tuples having the same first element.

Example:

Input: [(1, 2), (1, 3), (2, 4), (2, 5)]

Output: [(1, 2, 3), (2, 4, 5)]
"""
def join_similar_tuples(tuples_list):
    result = {}

    for tup in tuples_list:
        key = tup[0]

        if key not in result:
            result[key] = []

        result[key].extend(tup[1:])

    return [(key, *values) for key, values in result.items()]


tuples_list = [(1, 2), (1, 3), (2, 4), (2, 5)]

print("Result:", join_similar_tuples(tuples_list))