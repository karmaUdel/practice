import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {

	public static void main(String[] args) throws IOException {

		Path source = Paths.get("files/loremipsum.txt");
		System.out.println(source.getFileName());
		Path target = Paths.get("files/newfile.txt");
		System.out.println(target.getFileName());

	}
}
