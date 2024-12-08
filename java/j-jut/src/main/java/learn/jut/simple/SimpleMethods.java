package learn.jut.simple;

import java.util.Optional;


public class SimpleMethods {
	public SimpleMethods() {
		System.out.println("SimpleMethods is created");
	}

	public Integer add(Optional<Integer> i1, Optional<Integer> i2) {
		return i1.orElseThrow(() -> new NullPointerException()) + i2.orElseThrow(() -> new NullPointerException());
	}

}
