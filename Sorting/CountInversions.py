def merge(a, l, m, h):
    c = []
    i = l
    j = m + 1
    s = 0

    while i <= m and j <= h:
        if a[i] > a[j]:
            # there is an inversion
            s += (m - i + 1)
            c.append(a[j])
            j += 1
        else:
            c.append(a[i])
            i += 1

    # Adding remaning numbers
    while i <= m:
        c.append(a[i])
        i += 1
    while j <= h:
        c.append(a[j])
        j += 1

    a[l: h + 1] = c

    return s


def count(a, l, h):
    if l >= h:
        return 0
    #print(l, h)
    m = l + (h - l) // 2
    s = 0
    s += count(a, l, m)
    s += count(a, m + 1, h)

    s += merge(a, l, m, h)
    return s


def countInversions(a):
    return count(a, 0, len(a) - 1)
