### map&reduce&filter&sorted ###
# from functools import reduce

# a = range(1, 11)
# print(list(map(lambda x:x**2 + 1, a)))

# print(reduce(lambda x, y: x * 2 + y, a))

# def is_even(x):
#     return x % 2 == 0
#
# print(list(filter(is_even, a)))

b = [1, 6, 9, -5.3, 6.4, -2, 2]
# print(list(sorted(b)))

def num_process(x):
    return abs(round(x))

print(list(sorted(b, key=num_process)))
