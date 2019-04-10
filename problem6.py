def find_squares(n):
    return sum([x * x for x in range(n + 1)])


def find_sum_square(n):
    return sum(list(range(n + 1))) ** 2


print(find_squares(100) - find_sum_square(100))
