"""

Given a balanced parentheses string s, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

"""


def scoreOfParentheses(s) -> int:
    stack = []
    ans = 0
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            res = 0
            count = 1
            j = len(stack)-1
            while stack[j] != '(':
                res += stack[j]
                stack.pop()
                j -= 1
            res *= 2
            if res == 0:
                res = 1
            stack[-1] = res
    for i in stack:
        ans += i
    return ans
