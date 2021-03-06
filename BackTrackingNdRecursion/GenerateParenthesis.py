"""
Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.

"""


def generateParenthesis(n):
    st = []
    ans = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            print("".join(st))
            return
        if openN < n:
            st.append('(')
            backtrack(openN+1, closeN)
            st.pop()
        if closeN < openN:
            st.append(')')
            backtrack(openN, closeN+1)
            st.pop()
    backtrack(0, 0)
    return ans


generateParenthesis(7)
