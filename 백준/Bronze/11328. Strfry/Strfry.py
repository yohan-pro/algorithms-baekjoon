for _ in range(int(input())):
    a, b = map(str, input().split())
    c = sorted(list(map(str, a)))
    d = sorted(list(map(str, b)))
    print("Possible" if c == d else "Impossible")