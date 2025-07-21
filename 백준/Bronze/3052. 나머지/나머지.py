from collections import defaultdict
d = defaultdict(int)
for i in range(10):
  d[int(input()) % 42] += 1
print(len(d))