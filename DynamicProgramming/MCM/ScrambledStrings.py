
'''
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

'''


def solve(a, b):
    if a == b:
        return True
    if len(a) <= 1:
        return False
    flag = False
    for i in range(1, len(a)-1):
        temp1 = solve(a[:i], b[-i:]) and solve(a[i:], b[:-i])  # swapped
        temp2 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])    # not swapped

        if temp1 or temp2:
            flag = True
            break

    return flag


if __name__ == 'main':
    s1 = input()
    s2 = input()
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        print(False)
    elif n1 == 0 and n2 == 0:
        print(True)

    print(solve(s1, s2))
