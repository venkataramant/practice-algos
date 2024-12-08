package learn.j.collectoins;

import java.util.function.Supplier;
import java.util.stream.Stream;

public class StreamIteratreAndGenerateMain {

	public static void main(String[] args) {
		streamIterate();
		streamGenerate();
	}

	private static void streamIterate() {
		Stream.iterate(0, x -> x + 1).limit(10).forEach(System.out::println);
	}

	private static void streamGenerate() {
		int i=20;
		Stream.generate(MySupplier.of(i)).takeWhile(x -> x < i+10).forEach(System.out::println);
	}

}

class MySupplier implements Supplier<Integer> {
	int x;

	public static MySupplier of(int x) {
		return new MySupplier(x);
	}

	private MySupplier(int x) {
		this.x = x;
	}

	@Override
	public Integer get() {
		return x++;
	}
}
