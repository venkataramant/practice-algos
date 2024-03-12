package tvr.learn.java8.defaultAndStatic;

import java.util.List;

public interface StaticMethods1 {
	public static <T extends List<T>> T MyStaticMethod(T t) {
		t.forEach(x -> System.out.println(x));
		return t;
	}

	public static <T extends List> T MyStaticMethod2(T t) {
		t.forEach(x -> System.out.println(x));
		return t;
	}

	public static <T> void MyStaticMethod3(T t) {

	}

	// cannot override java.lang.Object methods as default methods
//	default boolean equals(Object obj) {
//		return False;
//	}

	default <T> void printMe(T t) {
		System.out.println(t == null ? "None" : t);
	}
}