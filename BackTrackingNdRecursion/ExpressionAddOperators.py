'''

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

'''


class Solution:
    def addOperators(self, num: str, target: int):
        def dfs(curr, num):
            if curr in visited:
                return
            visited.add(curr)
            for i, ch in enumerate(num):
                if i == len(num) - 1:
                    if eval(curr + num) == target:
                        result.append(curr + num)
                else:
                    dfs(curr + num[:i+1] + "*", num[i+1:])
                    dfs(curr + num[:i+1] + "-", num[i+1:])
                    dfs(curr + num[:i+1] + "+", num[i+1:])

                if num[:i+1] == "0":
                    break
        result = []
        visited = set()
        dfs("", num)
        return result
