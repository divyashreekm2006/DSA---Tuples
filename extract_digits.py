"""
Problem 7: Extract Digits from Tuple List
Description: Extract individual digits from numbers present in a list of tuples.

Example:

Input: [(12, 34), (56, 78)]

Output: [1, 2, 3, 4, 5, 6, 7, 8]

"""
def extract_digits(tuples_list):
    result = []

    for tup in tuples_list:
        for num in tup:
            for digit in str(abs(num)):
                result.append(int(digit))

    return result

tuples_list = [(12, 34), (56, 78)]

print("Digits:", extract_digits(tuples_list))