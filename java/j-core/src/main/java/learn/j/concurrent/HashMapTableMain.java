package learn.j.concurrent;

import java.util.HashMap;
import java.util.Hashtable;

public class HashMapTableMain {

	public static void main(String[] args) {
		Hashtable<String, String> nullAreNotAllowed = new Hashtable<String, String>();
//		ht.put("k", null); Null values are not allowed
//		ht.put(null, "v"); Null keys are not  allowed
		HashMap<String, String> nullsareAllowed = new HashMap<String, String>();
		nullsareAllowed.put("k", null); // Null values are allowed
		nullsareAllowed.put(null, null);
		System.out.println(nullsareAllowed);

	}

}
