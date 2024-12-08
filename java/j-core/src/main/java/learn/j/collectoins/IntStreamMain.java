package learn.j.collectoins;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class IntStreamMain {
	public static void main(String... args) {
		List<Integer> myInts = Arrays.asList(1, 2, 3, 4, 5, 6, 7);
		BiFunction<Integer, Integer, Map<Integer, Integer>> convertMap = (x, y) -> {
			Map<Integer, Integer> m = new HashMap<>();
			m.put(x, y);
			return m;
		};

		IntStream.range(0, 10).boxed().peek(x -> System.out.println(x)).count();
		IntStream myInts2 = IntStream.range(0, 10);
		Map myMap = myInts2.boxed().collect(Collectors.toMap(
				// Key mapper
				key -> key,
				// Value mapper
				value -> value,
				// Merge function (in case of duplicate keys)
				(existing, replacement) -> existing,
				// Supplier for the target map
				HashMap::new));
		System.out.println(myMap);

	}
}
