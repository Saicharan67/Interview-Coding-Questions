from functools import cmp_to_key
t = int(input())


def rangefnx(x, y):
    if x[1]-x[0] >= y[1]-y[0]:
        return 1
    else:
        return -1


for _ in range(t):

    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    count = 0
    #l = sorted(l, key=cmp_to_key(rangefnx))
    for i in range(n):
        count = 0
        for j in range(n):
            if l[j][2] == l[i][2]:
                if l[i][0] <= l[j][0] and l[j][0] <= l[i][1]:
                    count += 1
                elif l[i][0] <= l[j][1] and l[j][1] <= l[i][1]:
                    count += 1

        if count > 2:
            print("NO")
            break
    if count <= 2:
        print('YES')
