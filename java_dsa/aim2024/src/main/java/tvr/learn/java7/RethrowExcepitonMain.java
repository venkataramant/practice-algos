package tvr.learn.java7;

class CustomException1 extends Exception {

}

class CustomException2 extends Exception {

}

public class RethrowExcepitonMain {
	public static void main(String... args) {
		try {
			someProcess_v6(0);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			someProcess_v7(0);
		} catch (CustomException1 | CustomException2 e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	// Before Java 7 We have to wrap it to supertype to throw it
	private static void someProcess_v6(int myint) throws Exception {
		try {
			if (myint == 1) {
				throw new CustomException1();
			} else if (myint == 2) {
				throw new CustomException2();
			}
			System.out.println("Doing someProcess_v6");

		} catch (CustomException1 | CustomException2 e) {
			e.printStackTrace();
			throw e;
		} catch (Exception e) {
			throw e;
		}
	}

	// Java 7
	private static void someProcess_v7(int myint) throws CustomException1, CustomException2 {
		try {
			if (myint == 1) {
				throw new CustomException1();
			} else if (myint == 2) {
				throw new CustomException2();
			}
			System.out.println("Doing someProcess_v7");

		} catch (CustomException1 | CustomException2 e) {
			e.printStackTrace();
			throw e;
		} catch (Exception e) {
			// After Java 7 catch_block can re-throw declared type or its parent type.
			throw e;
		}
	}
}