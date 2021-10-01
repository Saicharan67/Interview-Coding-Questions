'''

Question: 
=========
You are given an array a consisting of n integers.

Let's call a pair of indices i, j good if 1≤i<j≤n and gcd(ai,2aj)>1 (where gcd(x,y) is the greatest common divisor of x and y).

Find the maximum number of good index pairs if you can reorder the array a in an arbitrary way.

---------------------------------------------------------------------------------------------------------------------------

Input:
======
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The first line of the test case contains a single integer n (2≤n≤2000) — the number of elements in the array.

The second line of the test case contains n integers a1,a2,…,an (1≤ai≤105).

It is guaranteed that the sum of n over all test cases does not exceed 2000.

---------------------------------------------------------------------------------------------------------------------------

Output:
======
For each test case, output a single integer — the maximum number of good index pairs if you can reorder the array a in an arbitrary way.

Example:

    Input:
        3
        4
        3 6 5 3
        2
        1 7
        5
        1 4 2 4 1

    Output:
        4
        0
        9

'''


from math import gcd
 
for t in range(int(input())):
    n=int(input())
    arr=[int(ele) for ele in input().split()]
    i,j=0,-1
    newArr=[-1]*n
    for ele in arr:
        if ele%2==0:
            newArr[i]=ele
            i+=1
        else:
            newArr[j]=ele
            j-=1


    count=0
    for i in range(n):
        for j in range(i+1,n):
            if gcd(newArr[i],2*newArr[j])>1:
                count+=1
 
    print(count)
