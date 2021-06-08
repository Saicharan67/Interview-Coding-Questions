"""
In ACM-ICPC contests, there are usually three people in a team. For each person in the team, you know their scores in three skills - hard work, intelligence and persistence.

You want to check whether it is possible to order these people (assign them numbers from 1 to 3) in such a way that for each 1 ≤ i ≤ 2, i+1-th person is stricly better than the i-th person.

A person x is said to be better than another person y if x doesn't score less than y in any of the skills and scores more than y in at least one skill.

Determine whether such an ordering exists.

"""


n = int(input())


def val(e):
    return e[0]


def isBetter(a, b):
    ok = False
    for i in range(3):
        if a[i] > b[i]:
            return False
        if a[i] < b[i]:
            ok = True
    return ok


for _ in range(n):
    s = []
    for _ in range(3):
        s.append(list(map(int, input().split())))
    for i in range(3):
        for j in range(i+1, 3):
            if not isBetter(s[i], s[j]):
                s[i], s[j] = s[j], s[i]

    if isBetter(s[0], s[1]) and isBetter(s[1], s[2]):
        print('yes')
    else:
        print('no')
