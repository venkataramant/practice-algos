package tvr.learn.java7;

import java.io.IOException;

import tvr.learn.java7.tryWithResources.TryWithResourcesFile;

public class MultiCatchExceptionMain {



	public static void main(String[] args) {
		

		try (TryWithResourcesFile trfile = new TryWithResourcesFile()) {
			Class<?> cls = Class.forName("a.b.c");
			System.out.println(cls);

		} catch (ClassNotFoundException | IOException e1) {
			System.out.printf("handle Multiple Exceptions here %s%n", e1);
		}catch ( RuntimeException e1) {
			System.out.printf("handle runtime exception here %s%n", e1);
		} catch (Exception e1) {
			System.out.printf("catched close Exception %s%n", e1);
		}
	}
}
