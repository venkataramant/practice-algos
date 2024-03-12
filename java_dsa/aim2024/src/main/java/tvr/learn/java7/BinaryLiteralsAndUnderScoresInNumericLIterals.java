package tvr.learn.java7;

import tvr.learn.java7.bnary_literals.BinaryLiterals;

public class BinaryLiteralsAndUnderScoresInNumericLIterals {
	public static void main(String... args) {
		BinaryLiterals bl = new BinaryLiterals();
		bl.setInt(0b1010_1010);
		bl.setLong(0b11_111_111);
		Integer myInteger = 0b111_010101;
		System.out.println(myInteger);
		System.out.println(Integer.toBinaryString(myInteger));
		Long myLong = (long) 0b101111101;
		System.out.println(myLong);
		System.out.println(Long.toBinaryString(myLong));
	}
}