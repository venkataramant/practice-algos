package tvr.learn.java5.generics;

import java.util.Arrays;
import java.util.List;

public class ComplexGenericMethods {

	public <E extends Number, T extends List<E>> void print1(T t) {
		for (E e : t) {
			System.out.println(e);
		}
	}

	public <T extends List<? extends Number>> void print2(T t) {
		for (Number e : t) {
			System.out.println(e);
		}
	}

	public void print3(List<? extends Number> t) {
		for (Number e : t) {
			System.out.println(e);
		}
	}
	public void print4(List<? extends Number> t) {
		for (Number e : t) {
			System.out.println(e);
		}
	}
	public void print5(List<? extends Parent> t) {
		for (Parent e : t) {
			e.printP();
		}
	}

	// Method overloading with wildcard types
    public void processList3(List<?> list) {
        System.out.println("Processing list with wildcard: " + list);
    }

    public void processList1(List<? extends Number> numbers) {
        System.out.println("Processing list with wildcard bounded to Number: " + numbers);
    }

    public void processList2(List<? extends String> strings) {
        System.out.println("Processing list with wildcard bounded to String: " + strings);
    }

    public static void main(String[] args) {
    	ComplexGenericMethods example = new ComplexGenericMethods();
        example.processList1(Arrays.asList(1, 2, 3));            // Calls processList(List<?>)
        example.processList3(Arrays.asList(1.1, 2.2, 3.3));      // Calls processList(List<? extends Number>)
        example.processList2(Arrays.asList("one", "two", "three")); // Calls processList(List<? extends String>)
    }
}
