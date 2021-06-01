def knapSack(wt, val, x, n):
    if(n == 0 or x == 0):
        return 0
    else:
        if wt[n-1] <= x:
            return max(val[n-1]+knapSack(wt, val, x-wt[n-1], n-1), knapSack(wt, val, x, n-1))
        else:
            return knapSack(wt, val, x, n-1)


print(knapSack([10, 20, 30], [60, 100, 120], 50, 3))
