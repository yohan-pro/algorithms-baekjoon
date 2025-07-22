from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
q.append((0, 0, 1))
a[0][0] = 0

while q:
  x, y, d = q.popleft()
  if x == n-1 and y == m-1:
    print(d)
    break
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == 1:
        q.append((nx, ny, d + 1))
        a[nx][ny] = 0