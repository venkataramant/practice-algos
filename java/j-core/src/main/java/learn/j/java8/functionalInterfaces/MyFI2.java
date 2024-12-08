package learn.j.java8.functionalInterfaces;

@FunctionalInterface
public interface MyFI2 {
	void print2();

	default void commonDefaultPrint() {
		System.out.println("MyFI2 default Method");
		Long l=5l;
	}

	@Override
	String toString();

	static void staticPrint2() {
		System.out.println("This is static method");
	}
}