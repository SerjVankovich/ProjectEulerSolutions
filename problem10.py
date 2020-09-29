from problem3 import is_simple

primals = [x for x in range(2, 2000000) if is_simple(x)]


print(sum(primals))
