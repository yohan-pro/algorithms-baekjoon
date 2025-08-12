import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

for _ in range(int(input())):
    cmd = input().split()
    op = cmd[0]

    if op == 'L':
        if left:
            right.append(left.pop())
    elif op == 'D':
        if right:
            left.append(right.pop())
    elif op == 'B':
        if left:
            left.pop()
    elif op == 'P':
        left.append(cmd[1])

print(''.join(left + right[::-1]))