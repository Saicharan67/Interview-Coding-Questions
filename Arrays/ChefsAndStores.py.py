n = int(input())
from math import floor

for _ in range(n):
    a = []
    for i in range(int(input())):
        a.append(list(map(int, input().split())))
    max_profit = 0
    for i in a:
        ppl = floor(i[1] / (i[0] + 1))
        max_profit = max(max_profit, ppl * i[2])
    print(max_profit)