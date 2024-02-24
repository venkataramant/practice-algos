package tvr.learn.java.dsa.java5;

import static  java.lang.System.out;
import static tvr.learn.java.dsa.java5.static_ex.MyStaticUtil.MyConstants;
import static tvr.learn.java.dsa.java5.static_ex.MyStaticUtil.myStaticMethod;


import static java.lang.Math.*;

/*
 * Use "import static" and either import a particular static members(variable or a method)
 * Here in this example java.lang.System.out, only "out variable is imported"
 * Access out as direct static variable anywhere in this java class
 * 
 * Second Approach, import all static variables/methods
 */
public class Java5Static {
    public static void main(String... args){
        Java5Static j5f=new Java5Static();
        j5f.run_static_example();
      }

   
    public void run_static_example(){
        out.println("out is imported as static, a feature of Java 5");
        out.printf("sql is imported staticly from java.lang.Math.* %f",sqrt(25));
        out.printf("\nThese are custom static methods/variables %d and %s \n",MyConstants,myStaticMethod());
    
    }

}
