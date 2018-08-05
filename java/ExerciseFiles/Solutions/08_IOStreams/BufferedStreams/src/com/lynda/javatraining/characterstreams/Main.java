package com.lynda.javatraining.characterstreams;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Main {

	public static void main(String[] args) {

		try (
				BufferedReader in = new BufferedReader(new FileReader("hamlet.xml"));
				BufferedWriter out = new BufferedWriter(new FileWriter("newfile.txt"));
				) {
			int c;
			while ((c = in.read()) != -1) {
				out.write(c);
			}
			System.out.println("All done!");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} 
		
	}
}
