package learn.j.collectoins;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import learn.j.java8.functionalInterfaces.MyFI1;

public class LambdaMain {
	public static void main(String... strings) {
		callLambdas();
		lamdasInCollections();
	}

	private static void callLambdas() {
		MyFI1 myFi = () -> System.out.println("Testing");
		System.out.println(myFi.equals(null));
		myFi.print1();
		MyFI1.staticPrint();

	}

	private static void lamdasInCollections() {
		Integer[] numbers = new Integer[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		List<Integer> numbersList = Arrays.asList(numbers);
		System.out.println(" just print numbers..1");
		numbersList.stream().forEach(x -> System.out.println(x));
		System.out.println(" just print numbers..2");
		numbersList.stream().forEach(System.out::println);
		System.out.println(" 2 factors cube");
		numbersList.stream().filter(x -> x % 2 == 0).map(x -> x * x * x).forEach(System.out::println);
		List<Integer> s = Arrays.stream(numbers).filter(x -> x % 5 == 0).map(x -> x * x).collect(Collectors.toList());
		System.out.println(" 5 factors square");
		s.forEach(System.out::println);
	}private static void lamdasInCollections2() {
		Integer[] numbers = new Integer[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		List<Integer> numbersList = Arrays.asList(numbers);
		System.out.println(" just print numbers..1");
		numbersList.stream().forEach(x -> System.out.println(x));
		System.out.println(" just print numbers..2");
		numbersList.stream().forEach(System.out::println);
		System.out.println(" 2 factors cube");
		numbersList.stream().filter(x -> x % 2 == 0).map(x -> x * x * x).forEach(System.out::println);
		List<Integer> s = Arrays.stream(numbers).filter(x -> x % 5 == 0).map(x -> x * x).collect(Collectors.toList());
		System.out.println(" 5 factors square");
		s.forEach(System.out::println);
	}
}
