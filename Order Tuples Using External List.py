"""
Problem 11: Order Tuples Using External List
Description: Rearrange a list of tuples according to the order specified in another list.

Example:

Input: ([(1, 'A'), (2, 'B'), (3, 'C')], [3, 1, 2])

Output: [(3, 'C'), (1, 'A'), (2, 'B')]
"""
def order_tuples(tuples_list, order):
    tuple_dict = {tup[0]: tup for tup in tuples_list}

    result = []

    for num in order:
        if num in tuple_dict:
            result.append(tuple_dict[num])

    return result


tuples_list = [(1, 'A'), (2, 'B'), (3, 'C')]
order = [3, 1, 2]

print("Ordered Tuples:", order_tuples(tuples_list, order))