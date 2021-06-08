"""
Chef is planning to open a new store at this street, 
where he would offer food of one of these N types.
 Chef assumes that the people who want to buy the type of food he'd offer 
 will split equally among all stores that offer it, and if this is 
 impossible, i.e. the number of these people p is not divisible by 
 the number of these stores s, then only ⌊ps⌋ people will buy food 
 from Chef.

Chef wants to maximise his daily profit. Help Chef
 choose which type of food to offer and find the maximum 
 daily profit he can make.

"""


from math import floor
n = int(input())

for _ in range(n):
    a = []
    for i in range(int(input())):
        a.append(list(map(int, input().split())))
    max_profit = 0
    for i in a:
        ppl = floor(i[1] / (i[0] + 1))
        max_profit = max(max_profit, ppl * i[2])
    print(max_profit)
