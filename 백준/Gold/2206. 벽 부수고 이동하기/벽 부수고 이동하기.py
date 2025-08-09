from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

while q:
    x, y, broken = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                q.append((nx, ny, broken))
                visited[nx][ny][broken] = visited[x][y][broken] + 1
            elif maps[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                q.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][0] + 1

y = visited[n-1][m-1][1]
n = visited[n-1][m-1][0]

if y and n:
    print(min(y, n))
elif y:
    print(y)
elif n:
    print(n)
else:
    print(-1)