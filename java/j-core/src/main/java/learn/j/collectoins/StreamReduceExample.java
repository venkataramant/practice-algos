package learn.j.collectoins;

import java.util.Arrays;
import java.util.List;

public class StreamReduceExample {
	public static void main(String[] args) {
		example_parallel_streams();
		example_non_parallel_streams();
	}

	private static void example_parallel_streams() {
		List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

		// Using reduce to find the sum of all elements in parallel
		int sum = numbers.parallelStream().reduce(0, // Identity value
				(partialSum, number) -> partialSum + number, // Accumulator function
				(s1, s2) -> s1 + s2); // Combiner function

		System.out.println("Sum of all elements: " + sum);
	}

	private static void example_non_parallel_streams() {

		List<String> strings = Arrays.asList("Java", "is", "awesome");

		// Using reduce to concatenate strings separated by comma
		String result = strings.stream().reduce("", // Identity value
				(partialString, str) -> {
					if (partialString.isEmpty()) {
						return str;
					} else {
						return partialString + ", " + str;
					}
				},
				// Combiner function (not used in this example)
				(s1, s2) -> s1 + s2);

		System.out.println("Concatenated string: " + result);
	}

}
