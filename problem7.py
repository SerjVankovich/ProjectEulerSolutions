from problem3 import is_simple

n = 0
i = 2
while True:
    if is_simple(i):
        n += 1
    if n == 10001:
        break
    i += 1
print(i)
