package com.lynda.javatraining;

import java.text.NumberFormat;

public class NumericLiteralDemo {

	public static void main(String[] args) {
		int numberOfOlives = 1_000_000_000;
		NumberFormat formatter = NumberFormat.getInstance();
		System.out.println(formatter.format(numberOfOlives));
	}

}
