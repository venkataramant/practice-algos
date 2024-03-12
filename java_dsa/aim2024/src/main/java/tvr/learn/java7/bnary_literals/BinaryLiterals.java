package tvr.learn.java7.bnary_literals;

public class BinaryLiterals {
	private int myInt = (int) 0b1010;
	private long myLong = (int) 0B10101010;

	public void setInt(int myInt) {
		this.myInt = myInt;
		this.showMyInt();
	}
	public void setLong(long myLong) {
		this.myLong=myLong;
		this.showMyLong();
	}

	private void showMyInt() {
		System.out.println(myInt);
		System.out.printf("%d%n", myInt);
	}
	private void showMyLong() {
		System.out.println(myLong);
		System.out.printf("%d%n", myLong);
	}
}