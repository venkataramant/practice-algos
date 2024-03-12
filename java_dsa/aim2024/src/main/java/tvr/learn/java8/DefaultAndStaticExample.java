package tvr.learn.java8;

import tvr.learn.java8.defaultAndStatic.MyList;
import tvr.learn.java8.defaultAndStatic.StaticMethods1;

public class DefaultAndStaticExample {
	public static void main(String... args) {
		MyList<MyList> list = new MyList<>("Group");
		MyList<String> list1 = new MyList<>("Oracle");
		MyList<String> list2 = new MyList<>("Postgres");
		MyList<String> list3 = new MyList<>("MySQL");
		list.add(list1);
		list.add(list2);
		list.add(list3);
		list1.add("Name1");
		list2.add("Name2");
		list3.add("Name3");

		// Call the static method from the interface
		StaticMethods1.MyStaticMethod(list);
	}
}
