def multiple_inv(b, n):
    for i in range(1, n):
        if (i * b) % n == 1:
            return i
    return 0

print(multiple_inv(5, 3))