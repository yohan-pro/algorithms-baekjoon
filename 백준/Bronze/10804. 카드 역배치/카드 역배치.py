n = [i + 1 for i in range(20)]
for i in range(10):
    a, b = map(int, input().split())
    n[a-1:b] = n[a-1:b][::-1]
print(" ".join(map(str, n)))