package learn.j.java.core.inner;

public class NestedOutterClassMain {
	static int GobalStaticInt;
	private int nestedInt;

	class MyNestedClass {
		int innerClassInt;
		int nestedInt;

		private void setinnerClassInt(int innerClassInt) {
			this.innerClassInt = innerClassInt;
			NestedOutterClassMain.this.nestedInt = 2 * innerClassInt;
			nestedInt = innerClassInt / 2;

		}
		private void printAll() {
			System.out.printf("Inner..innerClassInt %d%n NestedClassMain.this.nestedInt: %d%n Innerclass.nestedInt %d%n",
					innerClassInt,
					NestedOutterClassMain.this.nestedInt,
					nestedInt);
		}
	}
	private void printAll() {
		System.out.printf("Inner..innerClassInt Cannot Access innerclass variables without a innerclass object %n Innerclass.nestedInt %d%n",
				NestedOutterClassMain.this.nestedInt,
				nestedInt);
	}


	public static void main(String[] args) {
		NestedOutterClassMain ncMain = new NestedOutterClassMain();
		NestedOutterClassMain.MyNestedClass mync = ncMain.new MyNestedClass();
		mync.setinnerClassInt(10);
		mync.printAll();
		ncMain.printAll();

	}
}
