# from icecream import ic
# from functools import cmp_to_key
# t = int(input())


# # def comparator(a, b):
# #     if a[0] > b[0]:
# #         return 1
# #     elif a[0] < b[0]:
# #         return -1
# #     elif a[0] == b[0]:
# #         if a[1] > b[1]:
# #             return 1
# #         else:
# #             return -1


# for _ in range(t):

#     m, n = map(int, input().split())
#     checkpoints = list(map(int, input().split()))
#     cord = list(map(int, input().split()))
#     velocity = list(map(int, input().split()))
#     l = []
#     count = 0
#     for i, j in zip(cord, velocity):
#         if j > 0:
#             count += 1
#             l.append([i, 1])
#         else:
#             count -= 1
#             l.append([i, -1])

#     l = sorted(l, key=lambda x: x[0])
#     if m == 1:
#         if n == abs(count):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         i = 1
#         flag = 1
#         while(i < m and flag == 1):
#             ans = 0
#             temp = 0
#             j = 0
#             x = 0
#             while(j < n and l[j][0] <= checkpoints[i]):
#                 if l[j][1] < 0:
#                     if x == 1:
#                         print("NO")
#                         flag = 0
#                         break

#                 if l[j][1] == 1:
#                     x = l[j][1]
#                 if l[j][0] < checkpoints[i]:
#                     temp += 1
#                     ans += l[j][1]
#                 j += 1
#             if (abs(ans) != temp):
#                 print("NO")
#                 ic(temp)
#                 ic(checkpoints[i])
#                 ic(ans)
#                 flag = 0
#                 break
#             i += 1
#         if(flag):
#             print("YES")

from collections import defaultdict
from icecream import ic
t = int(input())
Mod = 10**9+7
fact = [1]

for i in range(1, 10):
    fact.append(fact[i-1]*i)
for _ in range(t):
    n = int(input())

    l = list(map(int, input().split()))
    res = 1
    Map = defaultdict(int)
    cnt = n
    for i in l:
        Map[i] += 1
    ic(Map)
    for i in range(n):
        if Map[i] == 0:
            break
        res = (res*Map[i]) % Mod
        ic(res)
        Map[i] -= 1
        cnt -= 1
    ic(fact[cnt])
    print(res*fact[cnt] % Mod)