'''
01234567
xyyzyzyx
iteration 1:
Step 1: 
identify substring
x
xy
xyyz
 beg = 0
 end = 4
step2 : 
remove unnece.. chars

iteration 2: 
step 1
 beg = 1
 y
 yy
 yyz
 yyzy
 yyzyz
 yyzyzy
 yyzyzyx
step2:
 beg = 1
 yzyzyx [y:3 z:2 x:1]
 
 zyzyx
 yzyx
 zyx
 beg = 5
 end = 7
 
beg, end
trackerMap{y: .. z : .. x: ..}  = arr o(1)
while all chars exhausted:

Problem statement::::

Smallest Substring of All Characters

Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"

Constraints:

    [time limit] 5000ms

    [input] array.character arr
        1 = arr.length = 30

    [input] string str
        1 = str.length = 500

    [output] string

Took an eternity to solve this!!!

'''

  # [x,y,z] "xyzx" -> xyz, yzx
  # abcx  -> ""
  # xyz -> xayz
  # xyysszyx
  # minCount = 4
  # 0 : xyyz > map {0 : 4}
  # 1 : yzyx > map {1: 4}
  # 2 : x
  # arr = [x,y,z],  str = "xxxyxxaz"
  # 0 : 1: 2:x 3:x 4: 5: map {2:0}arr = [yz]< 3  
  # xyxxyxxaz yxxaz
  # 12314501
  # xyxyaz -> beg = 0, end = 0
  # end = 1, sub = "xy", end = 2, "xyx", end = 3, "xyxy", end = 4, xyxya, end = 5, xyxyaz
  # beg = 1, beg = 2
  # xyaz
def get_shortest_unique_substring(arr, str):
    head = 0 # begin pointer
    result = "" # holds the substring
    counter = 0 # keeps track of uniqueness of char in subsequence
    countMap = {} # map to hold subsequencing char count

    # initialize countMap get count of all possible chars in arr
    for item in arr:
        countMap[item] = 0

    # scan string character by character
    for tail in range(len(str)):
        # set end pointer
        lastItem = str[tail]

        # skip all the characters which are not in arr
        if not(lastItem in countMap):
            continue
        # get how many time we should see the character
        endCount = countMap[lastItem]
        # if we have seen char before then increase counter, Unique counter
        if endCount == 0:
            counter += 1
        # keep track of how many times char is encountered
        countMap[lastItem]+= 1

        # push begin forward
        while counter == len(arr):
            subLen = tail - head + 1
            if subLen == len(arr):
                # return a substring of str from
                # head to tail
                return str[head: tail+1]

            if result == "" or subLen < len(result):
                # return a substring of str from
                # head to tail
                result = str[head: tail+1]
            #begin index
            firstItem = str[head]
            # remove non-unique items, from head of subsequence
            if firstItem in countMap:
                beginCount = countMap[firstItem] - 1
                if beginCount == 0:
                    counter = counter - 1
                countMap[firstItem]= beginCount

            head += 1

    return result