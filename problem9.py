import math

a = 0
b = 1
c = 2

for i in range(2, 1000):
    for k in range(3, 1000):
        j = math.sqrt(i ** 2 + k ** 2)
        if j * 10 == int(j * 10):
            if i < k:
                if i + j + k == 1000:
                    print(i * k * j)
