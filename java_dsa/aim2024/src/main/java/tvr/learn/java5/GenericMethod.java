package tvr.learn.java5;

import java.util.ArrayList;
import java.util.List;

import tvr.learn.java5.generics.GenericMethods;

public class GenericMethod {
	public static void main(String... strings) {
		GenericMethods gm = new GenericMethods();
		List<Integer> intList = new ArrayList<>();
		intList.add(1);
		intList.add(2);
		intList.add(3);

		List<String> strList = new ArrayList<>();
		strList.add("name1");
		strList.add("name2");
		strList.add("name3");

		List<Double> doubleList = new ArrayList<>();
		doubleList.add(2d);
		doubleList.add(2.045d);

		gm.print1(intList);
//		gm.print(strList); //Its Compile time error not accepting Lists with object of Non-Numbers
		gm.print1(doubleList);

		gm.print2(intList);
//		gm.print2(strList); //Its Compile time error not accepting Lists with object of Non-Numbers
		gm.print2(doubleList);

		gm.print3(intList);
//		gm.print3(strList); // Its Compile time error not accepting Lists with object of Non-Numbers
		gm.print3(doubleList);
	}
}
