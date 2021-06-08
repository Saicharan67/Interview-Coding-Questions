"""
Teams A and B are having a penalty shoot-out to decide the winner of their football match. Each team gets to take a shot N times, and the team with the higher number of scored goals at the end wins. If the number of goals scored during the shoot-out by each team turns out to be the same even after all 2N shots, then they stop and agree that the result is a draw.

The two teams take shots alternately — team A shoots first, then team B shoots, then team A and so on until team B takes its N-th shot (at which point each team has taken exactly N shots). Even though all 2N shots are taken, the result of the shoot-out is often known earlier — e.g. if team A has already scored N−1 goals and team B has missed at least two shots, team A is definitely the winner.

For each shot, you know whether it was a goal or a miss. You need to find the earliest moment when the winner is known — the smallest s (0≤s≤2N) such that after s shots, the result of the shoot-out (whether team A won, team B won or the match is drawn) would be known even if we did not know the results of the remaining 2N−s shots.

"""


def new_func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = 0
        b = 0
        lefta = n
        leftb = n
        s = list(map(int, input()))
        for i in range(1, len(s)+1):
            if i % 2 == 0:
                a += s[i]
                lefta -= 1
            else:
                b += s[i]
                leftb -= 1
            if a > b+leftb or b > a+lefta or (a == b and i == 2*n):
                break

        print(i)


new_func()
