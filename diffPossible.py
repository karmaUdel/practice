'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2

Output :

1

as 3 - 1 = 2

    Return 0 / 1 for this problem.
'''
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
	   index = 0
	   hashMap = {} # key,Val store
	   # B =2 current logic  actual
	   # 3, 1   true 3-1      true
	   # 1, 1   true          false
	   # 1, 3   true 3-1      true
	   for item in A:
	       if item in hashMap:
	           return 1
	       else:
	           if B > item :
	               if not(B+item in hashMap): 
        	           hashMap[B+item] = index # looking for lager number
    	       if B <= item:
    	           if not(item-B in hashMap): 
        	           hashMap[item-B] = index # looking for smaller number
	       
	       index+=1 #keeps track of index
	       
	   return 0
