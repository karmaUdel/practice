package com.lynda.javatraining;

import java.util.TreeSet;

import com.lynda.javatraining.olives.Kalamata;
import com.lynda.javatraining.olives.Ligurio;
import com.lynda.javatraining.olives.Olive;
import com.lynda.javatraining.olives.Picholine;

public class Main {

	public static void main(String[] args) {
		
		Olive lig = new Ligurio();
		Olive kal = new Kalamata();
		Olive pic = new Picholine();

		TreeSet<Olive> set = new TreeSet<>();
		
		try {
			set.add(pic);
			set.add(kal);
			set.add(lig);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		
		System.out.println(set);
	}

}
