package learn.j.dsa.sort;

import java.util.Arrays;

 abstract class Tuple {
	public final Integer x;
	public final Integer y;

	public Tuple(Integer x, Integer y) throws Exception {
		if (y > x) {
			throw (new Exception("Y cannot more than x"));
		}
		this.x = x;
		this.y = y;
		my();
	}
	 abstract void my();

}

public class MergeSortMain {

	public static void main(String[] args) throws Exception {
		int[] myInts = new int[] { 6, 3, 5, 1, 2, 4, 9, 8 };
		Arrays.stream(myInts).forEach(x -> System.out.print(" " + x + " "));
		System.out.println();
		mergeSort(myInts, 0, myInts.length - 1);
		Arrays.stream(myInts).forEach(x -> System.out.print(" " + x + " "));

	}

	private static void mergeSort(int[] myInts, Integer x, Integer y) {
		if (size(x, y) == 1) {
			return;
		} else if (size(x, y) == 2) {
			if (myInts[x] > myInts[y]) {
				Integer temp = myInts[x];
				myInts[x] = myInts[y];
				myInts[y] = temp;
			}
			return;
		}
		Integer mid = (x + y) / 2;
		mergeSort(myInts, x, mid);
		mergeSort(myInts, mid + 1, y);

		return;
	}

	private static Integer size(Integer x, Integer y) {
		return y - x + 1;
	}
}
