package learn.j.core;

public class BasicDoubts {
	public static void main(String... strings) {
		P[] parents = null;
		C[] childrens = new C[10];
		parents = childrens;
		parents[0] = new P();
		childrens[0].print();
		System.out.println("Children..");
	}

}

class P {
	public void print() {
		System.out.println("P");
	}
}

class C extends P {
	public void print() {
		System.out.println("C");
	}
}