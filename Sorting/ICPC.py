# t1 = int(input())

# for _ in range(t1):
#     n, m, t = list(map(int, input().split()))
#     p = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     k = list(map(int, input().split()))
#     x = []
#     for i, j in zip(k, a):
#         x.append([i, j])
#     x = sorted(x, key=lambda x: x[0], reverse=True)
#     for i in range(m//2):
#         t = t-x[i][1]

#     p.sort()
#     i = 0
#     prob = 0
#     while prob <= t and i < n:
#         prob += p[i]
#         if prob <= t:
#             i += 1
#         else:
#             break
#     print(i)

# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     st = []
#     res = m
#     for i in range(n):
#         st.append(input())
#     st.sort()
#     for i in range(1, n):
#         count = 0
#         for j in range(m):
#             if st[i-1][j] == st[i][j]:
#                 count += 1
#             else:
#                 break
#         res += m-count
#     print(res)

import math
import copy
a = []

for i in range(2, 451):
    a.append(i*i)

f = []
for i in a:
    temp = []
    for j in range(1, int(math.sqrt(i))):

        if i % j == 0:
            temp.append(j)
    f.append(temp)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    temparr = copy.deepcopy(arr)
    lim = n-3
   # print('lim', lim)
    if lim != -1:
        for i in range(0, 1):
           # print('i', i)
            for j in range(0, lim+1):
               # print('j', j)
                num = a[j]
                for k in range(len(f[j])):
                    snum = num//f[j][k]
                    if snum <= n and arr[f[j][k]] > arr[snum]:
                        arr[f[j][k]], arr[snum] = arr[snum], arr[f[j][k]]
    temparr.sort()
    if temparr == arr:
        print("YES")

    else:
        print('NO')
