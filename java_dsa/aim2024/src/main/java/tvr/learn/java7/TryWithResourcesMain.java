package tvr.learn.java7;

import java.io.FileInputStream;
import java.io.IOException;

import tvr.learn.java7.tryWithResources.TryWithResourcesFile;

public class TryWithResourcesMain {

	public static void displayContent(String fileName) throws IOException {
		try (FileInputStream fis = new FileInputStream(fileName)) {
			while (fis.available() > 0) {
				System.out.printf("%s%n", fis.read(new byte[fis.available()]));
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			throw e;
		}
	}

	public static void main(String[] args){
		try {
			displayContent("test.txt");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		 
		try (TryWithResourcesFile trfile = new TryWithResourcesFile()) {
			System.out.println("done");
		} catch (IOException e) {
			System.out.println(e);;
		} catch (Exception e1) {
			System.out.printf("catched close Exception %s%n",e1);
		} 
	}
}
