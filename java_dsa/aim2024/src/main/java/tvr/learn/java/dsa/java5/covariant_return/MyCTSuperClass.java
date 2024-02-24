package tvr.learn.java.dsa.java5.covariant_return;

import java.util.List;
import java.util.Stack;

import static java.lang.System.out;

public class MyCTSuperClass {
    public List getList(){
        List myList=new Stack<>();
         out.println("I am from MyCovariantReturnSuperClass");
         return myList;
    }
}
