import sys
input = lambda: sys.stdin.readline().strip()
print = sys.stdout.write
for i in range(int(input())):
  a, b = map(int, input().split(' '))
  print(f'{a + b}\n')