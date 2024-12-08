package learn.j.collectoins;

import learn.j.java8.functionalInterfaces.MyFI1;
import learn.j.java8.functionalInterfaces.MyFI2;

public class FIMain {
	public static void main(String... strings) {
		fiLambda();
		MyFIClass fiObject = new MyFIClass();
		fiObject.commonDefaultPrint();
	}

	static void fiLambda() {
		MyFI1 myFi = () -> System.out.println("lambda way of printing");
		System.out.println(myFi.equals(null));
		myFi.print1();
		MyFI1.staticPrint();
	}
}

class MyFIClass implements MyFI1, MyFI2 {

	@Override
	public void print1() {
		System.out.println("implementing print1");
	}

	@Override
	public void print2() {
		System.out.println("implementing print2");

	}

	@Override
	public void commonDefaultPrint() {
		System.out.println("Calling default methods from interfaces");
		MyFI1.super.commonDefaultPrint();
		MyFI2.super.commonDefaultPrint();
		System.out.println("overriding commonDefaultPrint");
	}

}