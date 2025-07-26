from itertools import combinations
a = sorted(list(int(input()) for _ in range(9)))
for i in combinations(a, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break