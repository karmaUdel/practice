import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

import com.lynda.javatraining.filetree.FileFinder;

public class Main {

	public static void main(String[] args) throws IOException {

		Path fileDir = Paths.get("files");

		FileFinder finder = new FileFinder("file*.txt");
		Files.walkFileTree(fileDir, finder);
		
		ArrayList<Path> foundFiles = finder.foundPaths;
		
		if (foundFiles.size() > 0) {
			for (Path path : foundFiles) {
				System.out.println(path.toRealPath(LinkOption.NOFOLLOW_LINKS));
			}
		}
		else {
			System.out.println("No files were found!");
		}
		
	}
	
}
