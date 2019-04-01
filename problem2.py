
def fibonacci():
    sum = 2
    prev, current = 1, 2

    while current < 4000000:
        prev, current = current, prev + current
        if current % 2 == 0:
            sum += current
    return sum

sum = fibonacci()
print(sum)
