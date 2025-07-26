x, y = map(int, input().split())
if x > y:
    x, y = y, x
print(y - x - 1 if x != y else 0)
print(" ".join(map(str, list(i for i in range(x+1, y)))))