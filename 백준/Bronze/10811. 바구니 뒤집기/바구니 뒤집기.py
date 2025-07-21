n, m = map(int, input().split())
a = [i+1 for i in range(n)]
for _ in range(m):
  i, j = map(int, input().split())
  a[i-1:j] = a[i-1:j][::-1]
print(' '.join(map(str, a)))