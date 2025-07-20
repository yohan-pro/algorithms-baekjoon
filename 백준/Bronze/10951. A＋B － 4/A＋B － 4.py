import sys
input = lambda: sys.stdin.readline().strip()

while True:
    line = input()
    if not line:
        break
    a, b = map(int, line.split(' '))
    print(a + b)