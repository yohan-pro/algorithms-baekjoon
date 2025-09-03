s = input()
a = 1
l = len(s)
for i in range(l//2):
    if s[i] != s[l-i-1]:
        a = 0
print(a)