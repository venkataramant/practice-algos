package tvr.learn.java7.tryWithResources;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesFile implements AutoCloseable {

	public String getFirstLine(String fileName) {
		try (FileReader fr = new FileReader(fileName); BufferedReader br = new BufferedReader(fr)) {

			return br.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;
	}

	@Override
	public void close() throws Exception {
		String msg = "Throwing Explicit Exception";
		System.out.println(msg);
		throw new Exception(msg);

	}

}
