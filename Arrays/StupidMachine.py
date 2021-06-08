"""
There are N boxes in a line (numbered 1 through N). Initially, the boxes are empty, and I need to use the machine to put tokens in them. For each valid i, the i-th box has a maximum capacity Si tokens. I can perform the following operation any number of times: choose an integer L (1≤L≤N) and put one token in each of the boxes 1,2,…,L.

My manager told me to put as many tokens as possible into the boxes in total (the distribution of tokens in the boxes does not matter). Of course, it is not allowed to perform an operation that would result in the number of tokens in some box exceeding its capacity. Can you help me calculate the maximum number of tokens that can be put in these boxes?

"""


t = int(input())

for _ in range(t):
    n = int(input())
    min_m = float('inf')
    l = list(map(int, input().split()))
    res = 0
    for i in l:
        min_m = min(min_m, i)
        res += min_m
    print(res)
