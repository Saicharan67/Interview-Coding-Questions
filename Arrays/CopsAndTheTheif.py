"""
There are 100 houses located on a straight line. 
The first house is numbered 1 and the last one is numbered 100. 
Some M houses out of these 100 are occupied by cops.

Thief Devu has just stolen PeePee's bag and is looking for a house to hide in.

PeePee uses fast 4G Internet and sends the message to all 
the cops that a thief named Devu has just stolen her bag 
and ran into some house.

Devu knows that the cops run at a maximum speed of
 x houses per minute in a straight line and they will 
 search for a maximum of y minutes. 
 Devu wants to know how many houses are safe for him to 
 escape from the cops.
 Help him in getting this information.

"""


t = int(input())

for _ in range(t):
    a = [0]*101

    m, x, y = map(int, input().split())
    s = list(map(int, input().split()))
    for i in s:
        l = i-x*y
        r = i+x*y
        if sum(a) < 100:
            for j in range(l, r+1):
                if j > 0 and j <= 100:
                    a[j] = 1
    print(100-sum(a))
