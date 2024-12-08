package learn.j.java.core.inner;

public class StaticOutterClassMain {
	static int GobalStaticInt;

	static class MyStaticClass {
		int myiscInstanceInt;
		final static int MyISCStaticInt;
		static {
			MyISCStaticInt = 10;
		}
	}

	public static void main(String[] args) {
		System.out.println(args);
		System.out.println(MyStaticClass.MyISCStaticInt);
		System.out.println(GobalStaticInt);

	}
}
