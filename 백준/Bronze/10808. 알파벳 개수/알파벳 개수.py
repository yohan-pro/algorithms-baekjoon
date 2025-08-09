from collections import Counter
s = Counter(list(map(str, input())))
print(' '.join(map(str, list(s[chr(i)] for i in range(97, 123)))))