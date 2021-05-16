# cook your dish here
n = int(input())


def val(e):
    return e[0]


for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    count = 0
    l = sorted([a, b, c], key=val)
    a = l[0]
    b = l[1]
    c = l[2]

    for i in range(3):

        if a[i] < b[i] < c[i]:
            count += 1
        elif a[i] == b[i] < c[i]:
            count += 1
        elif a[i] < b[i] == c[i]:
            count += 1
        elif a[i] == b[i] == c[i]:
            pass
        else:
            count -= 20
    print(count)
