// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.*;
class SolutionNeighboringDigit {
    
    // O(N)
    // extract digits from Number N
    public ArrayList<Integer> getDigits(int N){
        ArrayList<Integer> digits = new ArrayList<>();
        while (N > 0){
            digits.add(N%10);
            N = N/10;
        }
        return digits;
    }
    // using logic of counting sort with max limit 10
    // sort Extracted digits
    // O(N+max) = O(N)
    public ArrayList<Integer> countSort(ArrayList<Integer> list){
        
        int length = list.size();
        int sorted [] = new int [length]; // never cross size 10
        int count [] = new int[11]; // digits are 0 to 9
		for (int i=0; i<length; ++i)
    		++count[list.get(i)]; // get count
		for (int i=1; i<11; ++i)
			count[i] += count[i-1]; // change count
		
		// Build the output digit array
		for (int i = 0; i<length; ++i)
		{
			sorted[count[list.get(i)]-1] = list.get(i);
			--count[list.get(i)];
		}
		// build output
		ArrayList<Integer> newList = new ArrayList<>();
		for (int i = 0; i<length; ++i)
			newList.add( sorted[i]);
        return newList ; 
    }
    public int solution(int N) {
        // write your code in Java SE 8
        if (N < 12){
            return N;
        }
        ArrayList<Integer> digits = getDigits (N);
        int returnVal = 0;
        //Collections.sort(digits); // sorts in ascending order O(NlogN) :( 
        digits = countSort(digits) ; // O(N)
        int base = 1;
        for(int i =0  ;i < digits.size();i++){
            returnVal += digits.get(i)*base;
            base *=10;
        }
        return returnVal;
    }
}