
dt = {}


def solve(a, b):
    if a == b:
        return True
    if len(a) <= 1:
        return False
    flag = False
    temp = a + '-' + 'b'
    if temp in dt:
        return dt[temp]
    for i in range(1, len(a)):
        temp1 = solve(a[:i], b[-i:]) and solve(a[i:], b[:-i])  # swapped
        temp2 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])    # not swapped

        if temp1 or temp2:
            flag = True
            break
    dt[temp] = flag
    return flag
