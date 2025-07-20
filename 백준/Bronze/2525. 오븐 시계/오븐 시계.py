a, b = map(int, input().split(' '))
c = int(input())
d = a * 60 + b + c
print(d // 60 % 24, d % 60)