"""
Problem : 
Cameron and Jamie's kid is almost 3 years old! However, even though the child is more independent now, scheduling kid activities and domestic necessities is still a challenge for the couple.
Cameron and Jamie have a list of N activities to take care of during the day. Each activity happens during a specified interval during the day. They need to assign each activity to one of them, so that neither of them is responsible for two activities that overlap. An activity that ends at time t is not considered to overlap with another activity that starts at time t.
For example, suppose that Jamie and Cameron need to cover 3 activities: one running from 18:00 to 20:00, another from 19:00 to 21:00 and another from 22:00 to 23:00. One possibility would be for Jamie to cover the activity running from 19:00 to 21:00, with Cameron covering the other two. Another valid schedule would be for Cameron to cover the activity from 18:00 to 20:00 and Jamie to cover the other two. Notice that the first two activities overlap in the time between 19:00 and 20:00, so it is impossible to assign both of those activities to the same partner.
Given the starting and ending times of each activity, find any schedule that does not require the same person to cover overlapping activities, or say that it is impossible.

Input :
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing a single integer N, the number of activities to assign. Then, N more lines follow. The i-th of these lines (counting starting from 1) contains two integers Si and Ei. The i-th activity starts exactly Si minutes after midnight and ends exactly Ei minutes after midnight.

Output :
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if there is no valid schedule according to the above rules, or a string of exactly N characters otherwise. The i-th character in y must be C if the i-th activity is assigned to Cameron in your proposed schedule, and J if it is assigned to Jamie.

"""

c=1
for i in range(int(input())):
    
    interval=[]
    for j in range(int(input())):
        a=list(map(int,input().split()))
        interval.append(a);
        
    res=[""]*(len(interval))
    duplicate=interval[:]
    interval.sort()
    l=duplicate.index(interval[0])
    duplicate[l]=0
    res[l]=('C')
    z=0
    y=0
    flag=True
    for k in range(1,len(interval)):
        if(interval[k][0]>=interval[z][1]):
            l=duplicate.index(interval[k])
            duplicate[l]=0
            res[l]='C'
            z=k
        elif(y==0):
            
            l=duplicate.index(interval[k])
            duplicate[l]=0
            res[l]='J'
            y=k
        elif(interval[k][0]>=interval[y][1]):
            l=duplicate.index(interval[k])
            duplicate[l]=0
            res[l]='J'
            y=k
        else:
            flag=False
            break
         
    if(flag):
        print("Case #{n}:".format(n=c),"".join(res))
    else:
        print("Case #{n}:".format(n=c),"IMPOSSIBLE")
    
    c+=1
