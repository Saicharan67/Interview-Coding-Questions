class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.rigt = None
        self.col = 0


def topview(root):
    if root is None:
        return None

    mp = dict()
    st = [root]

    while st:
        q = st.pop(0)
        col = q.col

        if col not in mp:
            mp[col] = q.data
        if q.left:
            q.left.col = col-1
            st.append(q.left)
        if q.right:
            q.right.col = col+1
            st.append(q.right)
    for i in sorted(mp):
        print(mp[i])
