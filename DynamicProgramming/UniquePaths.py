"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

"""
# Recursion Method


def UniquePath(m, n):
    if m == 1 or n == 1:
        return 1
    return UniquePath(m-1, n)+UniquePath(m, n-1)


print(UniquePath(3, 4))

# DP approch


def UniqueDp(m, n):
    dp = [[1 for _ in range(m)]for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[n-1][m-1]


'''
On an Island, there is an airport that has an unlimited number of identical air-planes. 
Each air-plane has a fuel capacity to allow it to fly exactly 1/2 way around the world, along a great circle. 
The planes have the ability to refuel in flight without loss of speed or spillage of fuel. 
Though the fuel is unlimited, the island is the only source of fuel. You can ignore the time and fuel consumption of refuelling.
What is the minimum number of air-planes required to get one air plane all the way around the world assuming that all of the air planes must return safely to the airport?

'''
