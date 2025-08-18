s = input()
a = []
for i in range(97, 123):
    a.append(s.find(chr(i)))
print(*a)