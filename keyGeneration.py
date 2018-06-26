# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
We are given a string S consisting of N characters and an integer K. The string represents a software license key which we would like to format. The string is composed of alphanumerical characters and/or dashes. The dashes split the alphanumerical characters within the string into groups (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are possibly misplaced.

We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but still must contain at least one character). To satisfy this requirement, we will reinsert the dashes. Additionally, all the lower case letters in the string must be converted to upper case.

For example, in the license key "2-4A0r7-4k" there are two dashes which split it into three groups of lengths 1, 5 and 2, respectively. If we want each group to be of length 4, then we would have to reinsert the dashes. Thus, for K = 4, the correctly formatted string is "24A0-R74K".

Write a function:

    def solution(S, K)

that, given a non-empty string S consisting of N characters, representing a license key to format, and an integer K, returns the license key formatted according to the description above.

For example, given S = "2-4A0r7-4k" and K = 4, the function should return "24A0-R74K", and for K = 3, the function should return "24-A0R-74K" as the first group could be shorter. Given S = "r" and K = 1, the function should return "R".
"""
def solution(S, K):
    # write your code in Python 3.6
    string = S.split("-")
    dashes = len(string)-1
    if dashes == 0 :
        return S.upper()
    key = ''
    for i  in range (dashes, 0, -1):
        length = len(string[i])
        #print (string[i])
        if length<K:
            key = string[i-1][(length - K)::].upper() +string[i].upper() + key
            string[i-1] = string[i-1][:(length - K)]
            if not(i== 0 or (i ==1 and len(string[0]) == 0)):
                key = '-'+key
                
            #print (string[i-1])
        else:
            if length>K:
                key = string[i][-K::].upper() +key
                #print(string[i][-K::].upper())
                string[i-1] +=string[i][:-K].upper() 
                if not(i== 0 or (i ==1 and len(string[0]) == 0)):
                    key = '-'+key
            
            else:
                key = string[i].upper()  + key
                if not(i== 0 or (i ==1 and len(string[0]) == 0)):
                    key = '-'+key
    key = string[0] + key
    return key