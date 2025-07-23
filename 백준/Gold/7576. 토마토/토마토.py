from collections import deque

def bfs():
    m, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    q = deque()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        result = max(result, a[x][y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                q.append((nx, ny))
                a[nx][ny] = a[x][y] + 1

    for row in a:
        if 0 in row:
            print(-1)
            return
    print(result - 1)

bfs()