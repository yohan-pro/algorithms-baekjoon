a = []
b = {}
for i in range(9):
  n = int(input())
  a.append(n)
  b[n] = i + 1
x = max(a)
print(x)
print(b[x])