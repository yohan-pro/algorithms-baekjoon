c = [1, 1, 2, 2, 2, 8]
d = list(map(int, input().split()))
print(*(a - b for a, b in zip(c, d)))