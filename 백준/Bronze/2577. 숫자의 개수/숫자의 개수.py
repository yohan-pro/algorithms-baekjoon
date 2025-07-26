from collections import Counter
a = 1
for i in range(3):
    a *= int(input())
c = Counter(str(a))
for i in range(10):
    print(c[str(i)])