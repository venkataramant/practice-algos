package tvr.learn.java5.covariant_return;

import java.util.LinkedList;
import static java.lang.System.out;

public class MyCTSubClass1 extends MyCTSuperClass{
    @Override
    public LinkedList getList(){
        LinkedList myList=new LinkedList<>();
         out.println("I am from MyCovariantReturnSubClass1 new LinkedList");
         return myList;
    }
}
