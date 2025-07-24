from collections import deque

r, c = map(int, input().split())
maze = [list(map(str, input())) for _ in range(r)]
man = [[0] * c for _ in range(r)]
fire = [[0] * c for _ in range(r)]

man_q = deque()
fire_q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            man_q.append((i, j))
            man[i][j] = 1
        elif maze[i][j] == 'F':
            fire_q.append((i, j))
            fire[i][j] = 1

def bfs_fire():
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if maze[nx][ny] != '#' and fire[nx][ny] == 0:
                    fire_q.append((nx, ny))
                    fire[nx][ny] = fire[x][y] + 1

def bfs_man():
    while man_q:
        x, y = man_q.popleft()
        if x == 0 or x == r-1 or y == 0 or y == c-1:
            return man[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (maze[nx][ny] == '.' and man[nx][ny] == 0) and (fire[nx][ny] == 0 or fire[nx][ny] > man[x][y] + 1):
                    man_q.append((nx, ny))
                    man[nx][ny] = man[x][y] + 1
    return "IMPOSSIBLE"

bfs_fire()
print(bfs_man())