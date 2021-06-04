def recurr(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + recurr(s[:-1])


print(recurr('saicharan'))
