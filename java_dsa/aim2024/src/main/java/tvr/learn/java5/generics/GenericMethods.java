package tvr.learn.java5.generics;

import java.util.List;

public class GenericMethods {

	public <E extends Number, T extends List<E>> void print3(T t) {
		for (E e : t) {
			System.out.println(e);
		}
	}
	public <T extends List<? extends Number>> void print2(T t) {
		for (Number e : t) {
			System.out.println(e);
		}
	}
	
	public void print1(List<? extends Number> t) {
		for (Number e : t) {
			System.out.println(e);
		}
	}

	
}