package tvr.learn.java5.generics;

import java.util.ArrayList;
import java.util.List;

// After Class Name <> inside Diamond
public class ComplexGenericClass3<T> {
	List<T> myTList;
	List<?> unknownList;
	List<? extends Number> numList;
	List<? extends String> strList;
	List<? super Number> objParentList;
	List<? super Integer> childParentList;

	public void printBoth() {
		for (T t : myTList) {
			System.out.println(t);
		}
		for (Object t : unknownList) {
			System.out.println(t);
		}
		for (Number t : numList) {
			System.out.println(t.longValue());
		}
		for (String t : strList) {
			System.out.println(t.length());
		}
		for (Object t : objParentList) {
			System.out.println(t);
		}
		
	}


}
