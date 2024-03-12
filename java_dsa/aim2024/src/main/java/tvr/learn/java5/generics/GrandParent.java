package tvr.learn.java5.generics;

public class GrandParent {
	public String printGP() {
		return this.toString();
	}
}

class Parent extends GrandParent{
	public String printP() {
		return this.toString();
	}
}

class Child extends Parent{
	public String printC() {
		return this.toString();
	}
}
class GrandChild extends Child{
	public String printGC() {
		return this.toString();
	}
}