package learn.j.java8.functionalInterfaces;

@FunctionalInterface
public interface MyFI1 {
	void print1();

	default void commonDefaultPrint() {
		System.out.println("MyFI1 default Method");
	}

	@Override
	boolean equals(Object o);

	static void staticPrint() {
		System.out.println("This is static method");
	}
}