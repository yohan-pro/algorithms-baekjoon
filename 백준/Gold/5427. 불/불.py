from collections import deque

n = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    w, h = map(int, input().split())
    building = [list(map(str, input())) for _ in range(h)]
    man = [[0] * w for _ in range(h)]
    fire = [[0] * w for _ in range(h)]

    man_q = deque()
    fire_q = deque()

    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                man_q.append((i, j))
                man[i][j] = 1
            elif building[i][j] == '*':
                fire_q.append((i, j))
                fire[i][j] = 1
    
    def bfs_fire():
        while fire_q:
            x, y = fire_q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if building[nx][ny] != '#' and fire[nx][ny] == 0:
                        fire_q.append((nx, ny))
                        fire[nx][ny] = fire[x][y] + 1
    
    def bfs_man():
        while man_q:
            x, y = man_q.popleft()
            if x == 0 or x == h-1 or y == 0 or y == w-1:
                return man[x][y]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if (building[nx][ny] != '#' and man[nx][ny] == 0) and (fire[nx][ny] == 0 or fire[nx][ny] > man[x][y] + 1):
                        man_q.append((nx, ny))
                        man[nx][ny] = man[x][y] + 1
        return "IMPOSSIBLE"
    
    bfs_fire()
    print((bfs_man()))

for i in range(n):
    bfs()