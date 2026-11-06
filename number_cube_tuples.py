"""
Problem 3: Create Tuples of Numbers and Their Cubes
Description: Create tuples containing each number and its cube.

Example:

Input: [1, 2, 3, 4]

Output: [(1, 1), (2, 8), (3, 27), (4, 64)]

"""
def number_cube_tuples(arr):
    result = []

    for num in arr:
        cube = num ** 3
        result.append((num, cube))

    return result


arr = [1, 2, 3, 4]

result = number_cube_tuples(arr)

print("Result:", result)