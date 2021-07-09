'''

Given a string str we need to tell minimum characters to be added at front of string to make string palindrome.
Examples: 
 

Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.

Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string.




Efficient approach: We can solve this problem efficiently in O(n) time using lps array of KMP algorithm. 
First we concat string by concatenating given string, a special character and reverse of given string then we will get lps array for this concatenated string, recall that each index of lps array represent longest proper prefix which is also suffix. We can use this lps array for solving the problem. 
 



For string = AACECAAAA
Concatenated String = AACECAAAA$AAAACECAA
LPS array will be {0, 1, 0, 0, 0, 1, 2, 2, 2, 
                   0, 1, 2, 2, 2, 3, 4, 5, 6, 7}
Here we are only interested in the last value of this lps array because it shows us the largest suffix of the reversed string that matches the prefix of the original string i.e these many characters already satisfy the palindrome property. Finally minimum number of character needed to make the string a palindrome is length of the input string minus last entry of our lps array. 
'''


def computeLPSArray(string):

    M = len(string)
    lps = [None] * M

    length = 0
    lps[0] = 0  # lps[0] is always 0

    # the loop calculates lps[i]
    # for i = 1 to M-1
    i = 1
    while i < M:

        if string[i] == string[length]:

            length += 1
            lps[i] = length
            i += 1

        else:  # (str[i] != str[len])

            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is
            # similar to search step.
            if length != 0:

                length = lps[length - 1]

                # Also, note that we do not
                # increment i here

            else:  # if (len == 0)

                lps[i] = 0
                i += 1

    return lps

# Method returns minimum character
# to be added at front to make
# string palindrome


def getMinCharToAddedToMakeStringPalin(string):

    revStr = string[::-1]

    # Get concatenation of string,
    # special character and reverse string
    concat = string + "$" + revStr

    # Get LPS array of this
    # concatenated string
    lps = computeLPSArray(concat)

    # By subtracting last entry of lps
    # vector from string length, we
    # will get our result
    return len(string) - lps[-1]
