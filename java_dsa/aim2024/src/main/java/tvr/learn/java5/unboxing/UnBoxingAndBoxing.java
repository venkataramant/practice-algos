package tvr.learn.java5.unboxing;

import static java.lang.System.out;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class UnBoxingAndBoxing {
	public static void main(String[] args) {
		UnBoxingAndBoxing ubab=new UnBoxingAndBoxing();
		ubab.print_different_boxings_unboxings();
		Integer I1 = 10;
		int i4 = 40;
		ubab.printInteger(I1);
		ubab.printInteger(i4);
		ubab.printInt(I1);
		ubab.printInt(i4);
		Integer[] myIntegers =  new Integer[]{1,2,3,4,5};
		int[] myInts =   new int[]{6,7,8,9,10};
		ubab.printIntegers(myIntegers);
		// ubab.printIntegers(myInts); // Lession_1:: UnBoxing is not applied at Array Level
		ubab.printInts(myInts);
//		ubab.printInts(myIntegers); // Lession_1:: UnBoxing is not applied at Array Level
		List<Integer> listIntegers=new ArrayList<>(Arrays.asList(12,3,4,5));
//		List<int> listInts=new ArrayList<>(Arrays.asList(12,3,4,5)); -// Lession_1::  Generics doesn't allow primitive types
		ubab.printIntegerList(listIntegers);
		ubab.printIntegerList2(listIntegers);
//		ubab.printIntegerList3(myIntegers); // Lession_1:: UnBoxing is not applied at Array Level
//		ubab.printIntegerList3(listIntegers.toArray(new Integer[3])); // Lession_1:: UnBoxing is not applied at Array Level
	}
	private void print_different_boxings_unboxings() {
		Integer i1 = 10;
		Integer i2 = new Integer(10);
		Integer i3 = Integer.valueOf(30);
		int i4 = Integer.valueOf(30);
		out.printf("unboxing %d %d %d %d\n", i1, i2, i3, i4);	
	}
	private void printInteger(Integer myInteger) {
		out.printf("printInteger::Argument is Integer %d \n", myInteger);
	}

	private void printInteger(int myInteger) {
		out.printf("printInteger::Argument is int %d \n", myInteger);
	}
	private void printInt(int myInteger) {
		out.printf("printInt::Argument is int %d \n", myInteger);
	}

	private void printIntegers(Integer[] myIntegers) {
		for(int x : myIntegers) {
			out.printf("printIntegers::using int to print Integer %d\n", x);
		}
		out.println();
	}
	private void printInts(int[] myInts) {
		for(Integer x : myInts) {
			out.printf("using Integer to print int %d\n", x);
		}
		out.println();
	}
	private void printIntegerList(List<Integer> myInts) {
		for(Integer x : myInts) {
			out.printf("Input::List<Integer> using Integer to print int %d\n", x);
		}
		out.println();
	}
	private void printIntegerList2(List<Integer> myInts) {
		for(int x : myInts) {
			out.printf("Input::List<Integer> and convert it int to print int %d\n", x);
		}
		out.println();
	}
	private void printIntegerList3(int[] myInts) {
		for(Integer x : myInts) {
			out.printf("Input::List<Integer> and convert it int to print int %d\n", x);
		}
		out.println();
	}
}