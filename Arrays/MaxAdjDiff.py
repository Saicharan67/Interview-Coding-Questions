def MaxAdjDiff(a):
    max_a = max(a)
    min_a = min(a)
    size = max_a-min_a+1

    holes = [0]*size

    for i in a:
        holes[i-min_a] += 1
    diff = -9999
    prev = holes[0]
    for i in range(1, size):
        if holes[i]:
            diff = max(diff, i+min_a-prev)
            prev = i+min_a
    print(diff)


MaxAdjDiff([10, 9, 5, 1])
