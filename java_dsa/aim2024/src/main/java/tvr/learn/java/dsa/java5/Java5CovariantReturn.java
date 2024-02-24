package tvr.learn.java.dsa.java5;

import static  java.lang.System.out;

import tvr.learn.java.dsa.java5.covariant_return.MyCTSubClass1;
import tvr.learn.java.dsa.java5.covariant_return.MyCTSubClass2;
import tvr.learn.java.dsa.java5.covariant_return.MyCTSuperClass;



public class Java5CovariantReturn {
    public static void main(String... args){
        Java5CovariantReturn j5cr=new Java5CovariantReturn();
        j5cr.run_covariant_return_example();
      }

      @Override
      public String toString(){
          return "Annotation is introduced in Java5";
      }

    public void run_covariant_return_example(){
        MyCTSuperClass sc=new MyCTSuperClass();
        out.printf("\ntype from Superclass %s \n",sc.getList().getClass());
        sc=new MyCTSubClass1();
        out.printf("\ntype from MyCTSubClass1 %s\n",sc.getList().getClass());
        sc=new MyCTSubClass2();
        out.printf("\ntype from MyCTSubClass2 %s\n",sc.getList().getClass());
    }
    
}
