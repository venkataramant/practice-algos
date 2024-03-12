package tvr.learn.java8;

import java.util.Arrays;
import java.util.List;

interface Display<T>{
	void print(T t);
}
public class MyStreams {
	public static void main(String... args) {
		int[] ints = { 1, 2, 3, 4, 5 };
		for (Integer myint : ints) {
			System.out.println(myint);
		}
		Display<Integer> display = x -> System.out.println(x);
		Display<List<Integer>> display2 = x -> x.stream().forEach(y->System.out.println(y));
		Display<int[]> display3 =x-> Arrays.stream(x).forEach(y->System.out.println(y));
		System.out.println(Arrays.asList(ints));
		Arrays.asList(ints).stream().forEach(x -> display3.print(x));
		Arrays.stream(ints).forEach(x -> display.print(x));
		List<Integer> intsList = Arrays.asList(1, 2, 3, 4, 5);
		intsList.stream().forEach(x->display.print(x));
		display3.print(ints);
	}
}
