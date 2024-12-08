package learn.j.collectoins;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class SortingMain {
	public static void main(String... strings) {
		reverseOrder();
		System.out.println("reverseOrder________________________________");
		sort();
		System.out.println("sort________________________________");
		sortDescending();
		System.out.println("sortDescending________________________________");
		sortArray();
		System.out.println("sortArray________________________________");
		sortDescendingArray();
		System.out.println("sortDescendingArray________________________________");
		sortStream();
		System.out.println("sortStream________________________________");
		sortDescendingStream();
		System.out.println("sortDescendingStream________________________________");
	}

	private static void reverseOrder() {
		List<Integer> intsList = Arrays.asList(1, 3, 5, 7, 4, 6, 9);
		System.out.println(intsList);
		Collections.reverse(intsList);
		System.out.println(intsList);
	}

	private static void sort() {
		List<Integer> intsList = Arrays.asList(1, 3, 5, 7, 4, 6, 9);
		System.out.println(intsList);
		Collections.sort(intsList);
		System.out.println(intsList);
	}

	private static void sortDescending() {
		List<Integer> intsList = Arrays.asList(1, 3, 5, 7, 4, 6, 9);
		System.out.println(intsList);
		Collections.sort(intsList, Collections.reverseOrder());
		System.out.println(intsList);
	}

	private static void sortArray() {
		Integer[] intArray = new Integer[] { 1, 3, 5, 7, 4, 6, 9 };
		Arrays.asList(intArray).forEach(x -> System.out.printf(" %d ", x));
		System.out.println();
		Arrays.sort(intArray);
		Arrays.asList(intArray).forEach(x -> System.out.printf(" %d ", x));
		System.out.println();
	}

	private static void sortDescendingArray() {
		Integer[] intArray = new Integer[] { 1, 3, 5, 7, 4, 6, 9 };
		Arrays.asList(intArray).forEach(x -> System.out.printf(" %d ", x));
		System.out.println();
		Arrays.sort(intArray, Collections.reverseOrder());
		Arrays.asList(intArray).forEach(x -> System.out.printf(" %d ", x));
		System.out.println();
	}

	private static void sortStream() {
		List<Student> students = Arrays.asList(new Student(1, "name1", 35), new Student(7, "name7", 31),
				new Student(2, "name2", 32), new Student(6, "name6", 26), new Student(4, "name4", 31),
				new Student(5, "name5", 28), new Student(3, "name3", 23), new Student(8, "name8", 29));

		System.out.println(students);
		List<Student> sortedList = students.stream().sorted().collect(Collectors.toList());
		System.out.println(sortedList);
		sortedList = students.stream().sorted(Comparator.comparing(Student::getAge).thenComparing(Student::getName))
				.collect(Collectors.toList());
		System.out.println(sortedList);
	}

	private static void sortDescendingStream() {
		List<Integer> intsList = Arrays.asList(1, 3, 5, 7, 4, 6, 9);
		System.out.println(intsList);
		List<Integer> sortedList = intsList.stream().sorted(Collections.reverseOrder()).collect(Collectors.toList());
		System.out.println(sortedList);
	}
}
