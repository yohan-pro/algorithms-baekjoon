n, m = map(int, input().split())
a = [i+1 for i in range(n)]
for i in range(m):
  i, j = map(int, input().split())
  a[i-1], a[j-1] = a[j-1], a[i-1]
print(' '.join(map(str, a)))