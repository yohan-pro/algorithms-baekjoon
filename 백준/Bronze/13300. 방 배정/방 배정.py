import math
n, k = map(int, input().split())
a = [[0] * 7 for _ in range(2)]
r = 0
for i in range(n):
    s, y = map(int, input().split())
    a[s][y] += 1
for i in range(2):
    for j in range(1, 7):
        r += math.ceil(a[i][j]/k)
print(r)