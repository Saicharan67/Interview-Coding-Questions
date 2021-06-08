"""
Given the arrival and departure times of all trains that
reach a railway station, the task is to find the minimum number
of platforms required for the railway station so that no train waits. 
We are given two arrays that represent the 
arrival and departure times of trains that stop.

"""


def MinPlatforms(arr, dep, n):
    s = set()
    for i in range(n):
        s.add((arr[i], 'a'))
        s.add((dep[i], 'd'))
    x = 0
    result = 0
    s = sorted(s, key=lambda x: x[0])
    for i in s:

        if i[1] == 'a':
            x += 1
        else:
            result = max(result, x)
            x -= 1
    return result


print(MinPlatforms([900, 940], [910, 1200], 2))
