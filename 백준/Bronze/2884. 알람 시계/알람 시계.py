h, m = map(int, input().split(' '))
t = h * 60 + m - 45
print(t // 60 if t >= 0 else 23, t % 60)