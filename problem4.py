def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


max_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        if is_palindrome(n) and n > max_palindrome:
            max_palindrome = n

print(max_palindrome)
