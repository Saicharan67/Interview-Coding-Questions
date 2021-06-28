'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''


def combine(n: int, k: int):
    res = []

    def Combo(arr, op=[]):
        if len(op) == k:
            res.append(op)
            return
        for i in range(len(arr)):
            Combo(arr[i+1:], op+[arr[i]])
    Combo([i+1 for i in range(n)])
    return res
