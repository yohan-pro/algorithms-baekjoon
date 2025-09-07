a = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0, 'P':0.0}
c = 0
r = 0
for _ in range(20):
    z, s, g = input().split(' ')
    r += (float(s) * a[g])
    if g != 'P':
        c += float(s)
print(r/c)