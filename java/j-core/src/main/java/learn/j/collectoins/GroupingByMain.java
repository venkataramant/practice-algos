package learn.j.collectoins;

import java.util.Arrays;
import java.util.Hashtable;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class GroupingByMain {
	public static void main(String... strings) {
		List<Student> students = Arrays.asList(new Student(1, "name1", 25), new Student(2, "name2", 25),
				new Student(3, "name3", 27), new Student(4, "name4", 28), new Student(5, "name5", 28),
				new Student(6, "name4", 30), new Student(7, "name4", 31), new Student(8, "name8", 30));
		Map<Integer, List<Student>> studentsMap = students.stream()
				.collect(Collectors.groupingBy(student -> student.getAge()));
//		System.out.println(studentsMap);
		Map<Integer, Set<Student>> studentsSet = students.stream()
				.collect(Collectors.groupingBy(student -> student.getAge(), Collectors.toSet()));
//		System.out.println(studentsSet);

		Map<Integer, Set<Integer>> studentIdsMoreThan30Age = students.stream().filter(student -> student.getAge() > 30)
				.collect(Collectors.groupingBy(student -> student.getAge(),
						Collectors.mapping(Student::getId, Collectors.toSet())));
		System.out.println(studentIdsMoreThan30Age);
		Map<Integer, List<String>> studentNames = students.stream().collect(Collectors.groupingBy(s -> s.getAge(),
				Hashtable::new, Collectors.mapping(s -> s.getName(), Collectors.toList())));
		System.out.println(studentNames);

		Map<Integer, List<Integer>> intMap = Arrays.asList(1, 3, 5, 6, 3, 6, 9).stream()
				.collect(Collectors.groupingBy(x -> x));

		System.out.println(intMap);
	}

}