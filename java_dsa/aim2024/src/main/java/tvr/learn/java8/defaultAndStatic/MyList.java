package tvr.learn.java8.defaultAndStatic;

import java.util.ArrayList;

public class MyList<E> extends ArrayList<E> {
	private String type;

	public MyList(String type) {
		super();
		this.type = type;
	}

	@Override
	public String toString() {
		return String.format(this.type, super.toString());
	}
}