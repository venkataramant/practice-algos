package learn.j.collectoins;

import java.util.Arrays;
import java.util.List;
import java.util.StringJoiner;

public class StreamCollectExample {
	public static void main(String[] args) {
		List<String> strings = Arrays.asList("Java", "is", "awesome");
		example1(strings);
		example2(strings);
	}

	private static void example1(List<String> strings) {

		// Concatenate strings into a single string with space using collect
		String result = strings.stream()
				.collect(() -> new StringJoiner(" "), (sj, str) -> sj.add(str), (sj, str) -> sj.merge(str)).toString();

		System.out.println("Concatenated string: " + result);
	}

	private static void example2(List<String> strings) {

		// Concatenate strings into a single string with space using collect
		String result = strings.stream().collect(() -> new StringJoiner(" "), StringJoiner::add, StringJoiner::merge)
				.toString();

		System.out.println("Concatenated string: " + result);
	}
}
