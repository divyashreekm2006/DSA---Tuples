"""
Problem : Find the Size of a Tuple

Description: Given a tuple, find the total number of elements.

Example:
Input: (10, 20, 30, 40, 50)
Output: 5

"""
def tuple_size(tup):
    return len(tup)

tup = (10, 20, 30, 40, 50)

result = tuple_size(tup)

print("Tuple:", tup)
print("Size:", result)