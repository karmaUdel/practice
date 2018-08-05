import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.lynda.javatraining.filetree.MyFileVisitor;

public class Main {

	public static void main(String[] args) throws IOException {

		Path fileDir = Paths.get("files");
		MyFileVisitor visitor = new MyFileVisitor();
		Files.walkFileTree(fileDir, visitor);
	}
}
