package learn.j.dsa.leetcode;

import java.util.Arrays;

public class LC_274_H_Index {
	public int hIndex(int[] citations) {
		int ans = citations.length;
		int rIndex = citations.length - 1;
		Arrays.sort(citations);
		int prev_count = 0;
		while (ans >= 0 && rIndex >= 0) {
			System.out.println(ans + "..PC " + prev_count + "::" + rIndex);
			for (int index = rIndex; index >= 0; index--) {
				if (prev_count >= ans) {
					return ans;
				}
				if (citations[index] < ans) {

					System.out.println("not_ans::" + ans-- + " " + prev_count + "::" + index);
					rIndex = index;
					break;
				} else {
					++prev_count;
					if (prev_count >= ans) {
						return ans;
					}

				}

			}
		
			ans--;
		}
		return ans >= 0 ? ans : 0;

	}

	public static void main(String[] args) {
		int[] citations = new int[] { 3, 0, 6, 1, 5 };
//		citations = new int[] { 0 };
		citations = new int[] { 4, 4, 0, 0 };
		System.out.println(new LC_274_H_Index().hIndex(citations));
	}

}
