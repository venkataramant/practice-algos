package tvr.learn.java5;

import tvr.learn.java5.varargs.MyVarargs;

public class VarArgsMethod {

	public static void main(String... args) {
		MyVarargs mva=new MyVarargs();
		mva.print(1,2,4,6,null,mva,"myname");
		mva.print("myname","myaddress","mymailid");
		mva.print("");
		System.out.printf("sum is %d\n",mva.sum(1,2,4,6,8,9));
		System.out.printf("sum is %d\n",mva.sum());
		System.out.printf("sum is %d\n",mva.sum(1));
		
	}
}
