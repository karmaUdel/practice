package com.lynda.javatraining.filetree;

import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Path;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;

public  class FileFinder extends SimpleFileVisitor<Path> {

	public FileFinder() {
	}
	
	@Override
	public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
			throws IOException {
		return FileVisitResult.CONTINUE;
	}
}
