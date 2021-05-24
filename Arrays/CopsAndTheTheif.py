t = int(input())

for _ in range(t):
    a = [0]*101

    m, x, y = map(int, input().split())
    s = list(map(int, input().split()))
    for i in s:
        l = i-x*y
        r = i+x*y
        if sum(a) < 100:
            for j in range(l, r+1):
                if j > 0 and j <= 100:
                    a[j] = 1
    print(100-sum(a))
