// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
/*
Task description

This is a demo task.

Write a function:

    class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [-1, -3], the function should return 1.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [-1,000,000..1,000,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


*/
class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int max = -1;
        int min = 9999999;
        
        for(int i = 0; i < A.length;i++){
            if(max < A[i]){
                max = A[i];
            }
            if(min > A[i]){
                min = A[i];
            }
        }
        if (max > 0){
            int count [] = new int[max+1];
            for(int i = 0; i < A.length;i++){
                if(A[i]>0){
                    count[A[i]]++; 
                }
            }
            for(int i = 1; i < count.length;i++){
                if(count[i] == 0){
                    return i; 
                }
            }
            return max + 1;
        }
        else{
            return 1;
        }
    }
}