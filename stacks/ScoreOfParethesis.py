"""
Given a balanced parentheses string s, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
"""


def score(s):
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        else:
            temp = 0

            while st[-1] != '(':
                temp += st[-1]
                st.pop()
            temp *= 2
            if temp == 0:
                temp = 1
            st[-1] = temp
    print(sum(st))


score("()()")
