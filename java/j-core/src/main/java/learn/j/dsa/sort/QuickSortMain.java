package learn.j.dsa.sort;

import java.util.Arrays;

public class QuickSortMain {

	public static void main(String[] args) {
		int[] myInts = new int[] { 6, 3, 5, 1, 2, 4, 9, 8 };
		Arrays.stream(myInts).forEach(x -> System.out.print(" " + x + " "));
		System.out.println();
		quickSort(myInts, 0, myInts.length - 1);
		Arrays.stream(myInts).forEach(x -> System.out.print(" " + x + " "));

	}

	private static void quickSort(int[] myInts, int l, int r) {
		System.out.printf("Sorting %d %d for %n", l, r);
		Arrays.stream(myInts).forEach(x -> System.out.print(" " + x + " "));
		System.out.println();
		if (l > r) {
			System.out.printf("ignore %d %d %n", l, r);
		}
		int pivotIndex = l;
		int lIndex = l + 1;
		int rIndex = r;
		while (lIndex <= rIndex) {
			for (; lIndex < myInts.length; lIndex++) {
				if (myInts[lIndex] < myInts[pivotIndex]) {
					continue;
				}
				break;
			}

			for (; rIndex > 0; rIndex--) {
				if (myInts[rIndex] > myInts[pivotIndex]) {
					continue;
				}
				break;
			}
			if (lIndex < rIndex) {
				// Swamp those elements
				int temp = myInts[lIndex];
				myInts[lIndex] = myInts[rIndex];
				myInts[rIndex] = temp;

			} else {
				int temp = myInts[rIndex];
				myInts[rIndex] = myInts[pivotIndex];
				myInts[pivotIndex] = temp;
				if (l <= rIndex - 1) {
					quickSort(myInts, l, rIndex - 1);
				}
				if (rIndex + 1 < r) {
					quickSort(myInts, rIndex + 1, r);
				}
			}

		}

	}
}
