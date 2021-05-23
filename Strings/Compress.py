from icecream import ic


def compress(s):
    if not s:
        return s
    res = ''
    prev = ''
    for i in range(len(s)):

        if prev and s[i] != prev[-1]:
            if len(prev) == 1:
                res += prev
            else:
                res += prev[0]
                res += str(len(prev))
            prev = s[i]
        else:
            prev += s[i]
    if prev:
        if len(prev) == 1:
            res += prev
        else:
            res += prev[0]
            res += str(len(prev))

    return res if len(s) > len(res) else s


print(compress('AAABAACCDDDD'))
