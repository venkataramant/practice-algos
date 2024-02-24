package tvr.learn.java.dsa.java5.covariant_return;

import java.util.ArrayList;
import static java.lang.System.out;

public class MyCTSubClass2 extends MyCTSuperClass {
    @Override
    public ArrayList getList(){
        ArrayList myList=new ArrayList<>();
         out.println("I am from MyCovariantReturnSubClass2");
         return myList;
    }
}
