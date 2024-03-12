package tvr.learn.java5.varargs;

import static java.lang.System.out;

public class MyVarargs {
	public Integer sum(Integer... integers) {
		int sum = 0;
		for (int integer : integers) {
			sum += integer;
		}
		return sum;
	}

	public void print(Object... integers) {
		for (Object obj : integers) {
			if (obj != null) {
				out.printf(" %s %s \n", obj, obj.getClass());
			}else {
				out.printf("object is %s\n",obj);
			}
		}
	}
}