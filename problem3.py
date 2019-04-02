NUM = 600851475143


def is_simple(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def product(array):
    if len(array) == 0:
        return 1
    else:
        return array[0] * product(array[1:])


primals = []

for i in range(2, 600851475144):
    if is_simple(i):
        if NUM % i == 0:
            primals.append(i)
            if product(primals) == NUM:
                break

print(max(primals))
