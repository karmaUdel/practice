# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# merge groups 
def merge(lis):#O(K*K)
    for item in lis:
        for check in lis:
            if not(check == item):# skip same group check
                if item[1]+1 == check[0]: # if groups are continous
                    check[0]=item[0]
                    lis.remove(item)
                if item[0]-1 == check[1]: #  if groups are continous but reverse ordered
                    check[1]= item[1]
                    lis.remove(item)
    return lis
# check are there M groups of size K 
def check(group,K,M): #O(K)
    count = 0 
    for item in group:
        if item[1]-item[0]+1>=K:
            count+=1
    return count==M
    
#solution
def solution(A, K, M):
    if K <1 or M<1 or not A:
        return -1
    #if M <1:
    #    return -1
    
    group = [] # holds gropus of roses that bloomed of type [[start, end], ...]
    i = 1
    output = [] # list that holds how many days were there when M groups of K are found
    for rose in A: # O(N * merge * check)
        group.append([rose,rose]) # add newly bloomed rose 
        group = merge(group) # check if new rose adds to any group or not
        #print (group)
        if check(group,K,M):# check if we've M groups or not
            output.append(i) # append day on which we've M groups of K
        i +=1# get next day
    if not output: # empty
        return -1 # no M groups found
    else:
        return output[-1]# the last element which is max