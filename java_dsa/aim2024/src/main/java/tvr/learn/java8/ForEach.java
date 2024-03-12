package tvr.learn.java8;

import java.util.Arrays;

public class ForEach {
	public static void main(String... args) {
		Arrays.asList(args).stream().forEach(x -> System.out.println(x));
	}
}
