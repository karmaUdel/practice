package com.lynda.javatraining;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Iterator;

public class Main {

	public static void main(String[] args) throws IOException {

		Path source = Paths.get("files/loremipsum.txt");
		System.out.println(source.getFileName());
		Path target = Paths.get("files/newfile.txt");
		System.out.println(target.getFileName());

		Charset charset = Charset.forName("US-ASCII");
		ArrayList<String> lines = new ArrayList<>();
		
		try (BufferedReader reader = Files.newBufferedReader(source, charset))
		{
			String line = null;
			while ((line = reader.readLine()) != null) {
				System.out.println(line);
				lines.add(line);
			}
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
		
		try (BufferedWriter writer = Files.newBufferedWriter(target, charset))
		{
			Iterator<String> iterator = lines.iterator();
			
			while(iterator.hasNext()) {
				String s = iterator.next();
				writer.append(s, 0, s.length());
				writer.newLine();
			}
			
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
