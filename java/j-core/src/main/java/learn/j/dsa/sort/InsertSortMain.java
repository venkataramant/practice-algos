package learn.j.dsa.sort;

import java.util.Arrays;

public class InsertSortMain {

	public static void main(String[] args) {
		int[] myInts = new int[] { 6, 3, 5, 1, 2, 4, 9, 8 };
		Arrays.stream(myInts).forEach(x -> System.out.print(" " + x + " "));
		System.out.println();
		insertSort(myInts);
		Arrays.stream(myInts).forEach(x -> System.out.print(" " + x + " "));

	}

	private static void insertSort(int[] myInts) {
		for (int x = 1; x < myInts.length; x++) {
			for (int y = 0; y <= x; y++) {
				if (myInts[x] >= myInts[y]) {
					continue;
				} else {
					int temp = myInts[x];
					myInts[x] = myInts[y];
					myInts[y] = temp;
				}
			}
		}

	}

}
