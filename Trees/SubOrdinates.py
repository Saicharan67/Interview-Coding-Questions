'''
Given the structure of a company, your task is to calculate for each employee the number of their subordinates.

Input

The first input line has an integer n: the number of employees. The employees are numbered 1,2,…,n, and employee 1 is the general director of the company.

After this, there are n−1 integers: for each employee 2,3,…,n their direct boss in the company.

Output

Print n integers: for each employee 1,2,…,n the number of their subordinates.

Constraints
1≤n≤2⋅105
Example

Input:
5
1 1 2 3

Output:
4 1 1 0 0

'''
from collections import defaultdict
from functools import lru_cache
n = int(input())
arr = list(map(int, input().split()))

dt = defaultdict(list)


for i in range(len(arr)):
    dt[arr[i]].append(i+2)
    dt[i+2].append(arr[i])

ans = [0]*n
vis = [False]*(n)


@lru_cache(maxsize=None)
def findsubs(x):
    vis[x-1] = True
    temp = 1
    for y in dt[x]:
        if vis[y-1] == False:
            temp += findsubs(y)

    ans[x-1] = temp

    return temp


findsubs(1)

for i in ans:
    print(i-1, end=" ")
