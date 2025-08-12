from collections import Counter
a = Counter(input())
b = Counter(input())
print((a-b).total() + (b-a).total())