

'Instead of partitioning linearly we do it binarly so that it will not give TLE'


class Solution:
    dp = [[-1 for _ in range(10001)] for _ in range(101)]

    def superEggDrop(self, e: int, f: int) -> int:
        if f == 0 or f == 1:
            return f
        if e == 1:
            return f
        if self.dp[e][f] != -1:
            return self.dp[e][f]
        mini = float('inf')
        l = 1
        r = f
        while l <= r:
            i = (l+r)//2
            if self.dp[e-1][i-1] != -1:
                low = self.dp[e-1][i-1]
            else:
                low = self.superEggDrop(e-1, i-1)
                self.dp[e-1][i-1] = low

            if self.dp[e][f-i] != -1:
                high = self.dp[e][f-i]
            else:
                high = self.superEggDrop(e, f-i)
                self.dp[e][f-i] = high
            if low < high:
                l = i+1
            else:
                r = i-1
            ans = 1 + max(low, high)  # 1 added becoz of current attempt

            mini = min(mini, ans)
        self.dp[e][f] = mini
        return mini
