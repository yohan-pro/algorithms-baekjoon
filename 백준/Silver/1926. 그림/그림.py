from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
v = [[False] * m for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
count, size = 0, 0

def bfs(i, j):
  q = deque()
  q.append((i, j))
  v[i][j] = True
  area = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if not v[nx][ny] and a[nx][ny] == 1:
          q.append((nx, ny))
          v[nx][ny] = True
          area += 1
  
  return area

for i in range(n):
  for j in range(m):
    if not v[i][  j] and a[i][j] == 1:
      size = max(size, bfs(i, j))
      count += 1

print(count)
print(size)