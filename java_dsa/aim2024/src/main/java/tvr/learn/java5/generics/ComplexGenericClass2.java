package tvr.learn.java5.generics;

import java.io.Serializable;
import java.util.List;

// can Have multiple extends first shouldbe only Class if class exits, only one class is allowed
public class ComplexGenericClass2<T extends List & Serializable> {

	public void print(T t) {
		System.out.println(t);
	}

	public boolean isNull(T t) {
		return t == null ? true : false;
	}

	public boolean equals(T t1, T t2) {
		boolean isT1Null = this.isNull(t1);
		boolean isT2Null = this.isNull(t2);
		if (isT1Null && isT2Null) {
			return true;
		} else if (isT1Null || isT2Null) {
			return false;
		} else {
			return t1.equals(t2);
		}
	}

}