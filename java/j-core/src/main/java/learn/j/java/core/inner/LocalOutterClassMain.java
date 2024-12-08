package learn.j.java.core.inner;

public class LocalOutterClassMain {
	static int GobalStaticInt;
	private int nestedInt;

	private void myLocalInnerMethod() {
		class MyLocalInnerClass {
			int localInnnerClassInt;
			int nestedInt;

			private void setinnerClassInt(int innerClassInt) {
				this.localInnnerClassInt = innerClassInt;
				LocalOutterClassMain.this.nestedInt = 2 * innerClassInt;
				nestedInt = innerClassInt / 2;

			}

			private void printAll() {
				System.out.printf(
						"Inner..innerClassInt %d%n NestedClassMain.this.nestedInt: %d%n Innerclass.nestedInt %d%n",
						localInnnerClassInt, LocalOutterClassMain.this.nestedInt, nestedInt);
			}
		}
		MyLocalInnerClass mync = new MyLocalInnerClass();
		mync.setinnerClassInt(10);
		System.out.printf("Access within method:: %d\n LocalInnerClassMain.this.nestedInt: %d%n ",
				mync.localInnnerClassInt, LocalOutterClassMain.this.nestedInt);
		mync.printAll();
		this.printAll();
	}

	private void printAll() {
		System.out.printf(
				"Inner..innerClassInt Cannot Access Local innerclass variables without a innerclass object %n Innerclass.nestedInt %d%n",
				LocalOutterClassMain.this.nestedInt, nestedInt);
	}

	public static void main(String[] args) {
		LocalOutterClassMain ncMain = new LocalOutterClassMain();

		ncMain.myLocalInnerMethod();

	}
}
