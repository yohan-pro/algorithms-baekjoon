a = [list(map(int, input().split())) for _ in range(9)]
m = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if m <= a[i][j]:
            x = i
            y = j
            m = a[i][j]
print(m)
print(x+1, y+1)