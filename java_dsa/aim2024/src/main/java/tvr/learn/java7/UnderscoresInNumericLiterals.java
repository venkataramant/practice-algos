package tvr.learn.java7;

public class UnderscoresInNumericLiterals {
	public static void main(String... strings) {
		long myLong = 123_456_7890l;
		float mypi = 3.14_15F;
		long hexaWords = 0xCAFE_Bdde;
		byte inByte = 0b11_1111_1;

		System.out.printf("%dl %f %d %d", myLong, mypi, hexaWords, inByte);
	}
}