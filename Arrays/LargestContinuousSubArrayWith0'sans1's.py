
def ArrayLength(arr, n):
    dt = {}
    s = 0
    res = 0
    dt[0] = 0
    for i in range(n):
        if arr[i]:
            s += 1
        else:
            s += -1

        try:
            l = i+1 - dt[s]
            if l > res:
                res = l
            print(res)
        except:
            dt[s] = i+1
    return res


print(ArrayLength([1, 0, 0, 1, 0, 1, 1], 7))
