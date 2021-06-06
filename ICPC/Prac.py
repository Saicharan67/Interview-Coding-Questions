# # from functools import cmp_to_key
# # t = int(input())


# # def rangefnx(x, y):
# #     if x[1]-x[0] >= y[1]-y[0]:
# #         return 1
# #     else:
# #         return -1


# # for _ in range(t):

# #     n = int(input())
# #     l = []
# #     for i in range(n):
# #         l.append(list(map(int, input().split())))
# #     count = 0
# #     #l = sorted(l, key=cmp_to_key(rangefnx))
# #     for i in range(n):
# #         count = 0
# #         for j in range(n):
# #             if l[j][2] == l[i][2]:
# #                 if l[i][0] <= l[j][0] and l[j][0] <= l[i][1]:
# #                     count += 1
# #                 elif l[i][0] <= l[j][1] and l[j][1] <= l[i][1]:
# #                     count += 1

# #         if count > 2:
# #             print("NO")
# #             break
# #     if count <= 2:
# #         print('YES')


# # 30 21 22 20 19 18 17 25 7 8

# # 9  6   6  5  4  3  2  2 0 0

# import math
# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = []
#     for i in range(n):
#         l.append(list(map(float, input().split())))
#     min_dis = 999999
#     for i in range(n):
#         for j in range(i+1, n):
#             for x in range(j+1, n):
#                 temp = math.sqrt((l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2) + math.sqrt((l[x][0]-l[j][0])**2+(
#                     l[x][1]-l[j][1])**2) + math.sqrt((l[i][0]-l[x][0])**2+(l[i][1]-l[x][1])**2)
#                 min_dis = min(min_dis, temp)
#     print(min_dis)

def new_func(arr):
    res = 0
    while arr:
        res += sum(arr)
        i = 0
        while i < len(arr)-1:
            arr[i] = min(arr[i], arr[i+1])
            i += 1
        arr.pop()

    print(res)


new_func([11, 81, 94, 43, 3])
