def PigeonHoleSort(a):
    max_a = max(a)
    min_a = min(a)
    size = max_a-min_a+1

    holes = [0]*size

    for i in a:
        holes[i-min_a] += 1
    i = 0
    for count in range(size):
        while holes(count) > 0:
            holes[count] -= 1
            a[i] = count+min_a
            i += 1
    return a
