package learn.j.dsa.leetcode;

import java.util.PriorityQueue;


public class LC215KthLargestElementinanArray {

	public static void main(String[] args) {
		int[] nums = new int[] { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
		int k = 4;
		PriorityQueue<Integer> heap = new PriorityQueue<>();
		for(Integer num: nums) {
			heap.add(num);
			System.out.println(heap.peek());
			if (heap.size()>k) {
				System.out.println(heap);
				System.out.println("removing "+ heap.poll());
			}
		}
		System.out.println(heap.peek());
	}

}
