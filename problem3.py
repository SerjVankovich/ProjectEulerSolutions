NUM = 600851475143


def is_simple(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


max_simple = 2

for i in range(2, 600851475144):
    if is_simple(i):
        if NUM % i == 0:
            max_simple = i
            print(max_simple)

print(max_simple)
