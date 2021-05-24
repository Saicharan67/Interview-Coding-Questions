t = int(input())

for _ in range(t):
    n = int(input())
    min_m = float('inf')
    l = list(map(int, input().split()))
    res = 0
    for i in l:
        min_m = min(min_m, i)
        res += min_m
    print(res)
