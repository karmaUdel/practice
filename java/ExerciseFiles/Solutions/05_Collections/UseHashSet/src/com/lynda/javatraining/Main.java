package com.lynda.javatraining;

import java.util.HashSet;

import com.lynda.javatraining.olives.Kalamata;
import com.lynda.javatraining.olives.Ligurio;
import com.lynda.javatraining.olives.Olive;
import com.lynda.javatraining.olives.Picholine;

public class Main {

	public static void main(String[] args) {
		
		Olive lig = new Ligurio();
		Olive kal = new Kalamata();
		Olive pic = new Picholine();
		
		HashSet<Olive> set = new HashSet<>();
		set.add(lig);
		set.add(kal);
		System.out.println("There are " + set.size() + " olives in the set.");
		
		set.add(pic);
		System.out.println("There are " + set.size() + " olives in the set.");
		
		set.add(lig);
		System.out.println("There are " + set.size() + " olives in the set.");
		
		set.add(null);
		System.out.println("There are " + set.size() + " olives in the set.");
	
		set.remove(lig);
		System.out.println("There are " + set.size() + " olives in the set.");
		
		
	}

}
