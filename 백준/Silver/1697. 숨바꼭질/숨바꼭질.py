from collections import deque

MAX = 100000
n, k = map(int, input().split())
v = [-1] * (MAX + 1)

q = deque()
q.append(n)
v[n] = 0

while q:
    x = q.popleft()
    dx = [x - 1, x + 1, x * 2]
    for d in dx:
        if 0 <= d <= MAX and v[d] == -1:
            q.append(d)
            v[d] = v[x] + 1

print(v[k])