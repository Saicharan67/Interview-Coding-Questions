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
