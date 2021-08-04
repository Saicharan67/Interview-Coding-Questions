'''
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details. 
This is a famous Google interview question, also being asked by many other companies now a days.

Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, 
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes 
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" 
or "i like sam sung".

'''


def wordBreak(line, dic):
    def recurr(st):
        print(st)
        if st in dic:
            return 1
        if len(st) == 0:
            return 1
        ans = 0
        for i in range(1, len(st)):
            temp = st[:i] in dic and recurr(st[i:])

            ans = ans or temp

        return 1 if ans else 0
    
    return recurr(line)
