a = [i + 1 for i in range(30)]
for i in range(28):
  a[int(input()) - 1] = 0

for i in range(30):
  if a[i] != 0:
    print(a[i])