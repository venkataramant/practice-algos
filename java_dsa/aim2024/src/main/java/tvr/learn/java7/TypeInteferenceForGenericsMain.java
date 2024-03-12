package tvr.learn.java7;

import java.util.ArrayList;
import java.util.List;

public class TypeInteferenceForGenericsMain {
	public static void main(String... strings) {
		List<String> java6List = new ArrayList<String>();
		List<String> java7List = new ArrayList<String>();
		java6List.add("java6");
		java7List.add("java7");
		for (String item : java6List) {
			System.out.println(item);
		}
		for (String item : java7List) {
			System.out.println(item);
		}
		List list1=new ArrayList<>();
		List list2=new ArrayList();
		System.out.printf("%s %s\n",list1, list1.getClass());
		System.out.printf("%s %s\n",list2, list2.getClass());
	}
}