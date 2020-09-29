from problem3 import is_simple


def is_same_nums(num):
    num_str = str(num)
    for letter in num_str:
        if num_str.count(letter) >= 2:
            return True
    return False


def is_end_3(num):
    num_str = str(num)

    return num_str[-1] == '3'


def equal_mask(num, mask):
    num_str = str(num)
    num_star = None
    if len(num_str) != len(mask):
        return False
    for i in range(len(mask)):
        if mask[i] == '*':
            if num_star is None:
                num_star = num_str[i]
            else:
                if num_star != num_str[i]:
                    return False
            continue
        elif mask[i] == num_str[i]:
            continue
        else:
            return False
    return True


primes = [x for x in range(56000, 1000000) if is_simple(x) and is_same_nums(x) and is_end_3(x)]
for i in range(10):
    for j in range(10):
        prs = list(filter(lambda x: equal_mask(x, '*' + str(i) + '*' + str(j) + '*' + '3'), primes))
        if len(prs) > 5:
            print(prs)
