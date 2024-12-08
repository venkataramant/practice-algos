package learn.j.java5;

import learn.j.java5.varargs.MyVarargs;

;

public class GenericVarArgsMethod {

    public static void main(String... args) {
        MyVarargs mva = new MyVarargs();
        mva.gprint(1, 2, 4, 6, null, mva, "myname");
        mva.gprint(Integer.valueOf(1), 2, 4, 6,Integer.valueOf(6));
        mva.gprint("fname", "mname", null);
         mva.another();
//        mva.gprint(); reference to gprint is ambiguous becauase of null


    }
}
