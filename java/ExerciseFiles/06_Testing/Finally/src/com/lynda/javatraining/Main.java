package com.lynda.javatraining;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		FileReader fr = new FileReader("ATextFile.txt");
		BufferedReader br = new BufferedReader(fr); 
		String s;
		while((s = br.readLine()) != null) { 
			System.out.println(s); 
		} 
		fr.close();
		br.close();
	}

}
