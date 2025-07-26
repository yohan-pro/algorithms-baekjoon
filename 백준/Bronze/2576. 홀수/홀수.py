a = []
for i in range(7):
    x = int(input())
    if x % 2 == 1:
        a.append(x)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))