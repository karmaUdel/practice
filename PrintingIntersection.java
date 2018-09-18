	import java.util.List;
	import java.util.ArrayList;
	import java.util.Map;
	import java.util.Collections;
	import java.util.stream.Collectors;
	/***
	* 1.    generates an array or list of 1000 random Integers with max value of 1000 and validates results
	* 2.    checks if there are duplicates within the array/list and produces a single message to that extent
	* 3.    prints duplicates (non-repetitive output) within the array/list
	* 4.    generates another array/list of 1000 random Integers with max value of 1000 and validates results
	* 5.    prints intersection of the 2 arrays/lists (non-repetitive, ordered output)
	*/
	
	/*
	* Positive : generate negative and positive both
	* Limitation : generates [-maxValue : maxValue] ..
	* Running Time : O(UniqueNumbersInList2 ^ UniqueNumbersInList1)
	* Space : O(maxValue)
	*/
	class PrintingIntersection{
		/* Driver */
		public static  void  main (String args[]){
			List<Integer> list1 = generateList(1000,1000,true);
			containsDuplicate(list1, 1000);
			List<Integer> list2 = generateList(1000,1000,true);
			intersection(list1, list2, 1000);
		}
		/* Random list generator */
		public static List<Integer> generateList(int howManyNumbers, int maxValue, boolean signAllowed){
			List<Integer> list = new ArrayList<Integer>();
			if(howManyNumbers < 1 ){
				return list;
			}
			int number = 0;
			double sign = 0;
			for (int i = 0; i<howManyNumbers;i++){
				number = ((int)(Math.random() * maxValue) )% maxValue ; 
				if(signAllowed){
					sign = Math.random();
					if ( maxValue > 0 && sign > 0.5) {
						number = -1 * number; // signed integer
					}
				}
				list.add(number);
			}
			return list;
		}
		/* checks for duplicates*/
		public static void containsDuplicate(List<Integer>list1, int limit){
			int countPos [] = new int [limit*2];
			int duplicateFound = 0;
			for (Integer i : list1){
				if( i < 0 ){
					i = -1 * i + limit;
				}
				if(countPos[i] == 1){
					duplicateFound = 1; // set flag that duplicate is found
				}
				countPos[i]++;		
			}
			if(duplicateFound == 1 ){
			  System.out.println("Duplicate is detected, Printing Duplicated elements");
			}
			int countOfDuplicates = 0;
			int m = 0;
			//print duplicates
			for (int i = 0 ; i< limit*2; i++){
				if(countPos[i]> 1){
					m = i; 
					if(i > limit){ 
						m = (-1*(i-limit)); // reading negative numbers
					}
					System.out.print(m  + " repeated = " + countPos[i] + "\n");
					countOfDuplicates += countPos[i];
				}
			}
			System.out.println("\n Duplicates : "+countOfDuplicates);
		}
		/* Detect Intersections */
		public static void intersection(List<Integer>list1, List<Integer>list2, int limit){
			Collections.sort(list1); //sort to create order
			list1 = list1.parallelStream().distinct().collect(Collectors.toList()); // stream and remove duplicates
			list2 = list2.parallelStream().distinct().collect(Collectors.toList()); // stream and remove duplicates
			int intersectionCount =0; // keep track of count of intersecting elements
			/*
			for (Integer i : list1){
				if(list2.contains(i)){ // if element is in another list 
					System.out.print(i + "\t");
					intersectionCount++;
				} 
			} //time : O(N^2) and space O(1)
			Map <Integer, Integer> map = new HashMap<> ();
			for(Integer i: list2){
				map.put(i,i);
			} // Generate Map for List2
			
			for (Integer i : list1){
				if(map.contains(i)){ // if element is in another list 
					System.out.print(i + "\t");
					intersectionCount++;
				} 
			} //time : O(N) and space O(N)
			*/
			for (Integer i : list1){
				if(Collections.binarySearch(list2, i) > (-1*limit)){
					System.out.print(i + "\t");
					intersectionCount++;
				}
			} // time : O(N log(N)) and  space : O(1)  
			System.out.println("\n Intersection Count " + intersectionCount);
		}
	}
	