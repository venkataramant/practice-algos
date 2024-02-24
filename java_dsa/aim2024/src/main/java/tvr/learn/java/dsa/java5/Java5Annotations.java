package tvr.learn.java.dsa.java5;

import static  java.lang.System.out;


/*
 * Annotation is Metadata to provide an intention to compile and compiler 
 * will check those intentions are followed or any violations.
 * Ex:
 *  @override (Method)
 *  @Depreciated (Class/Method)
 *  @Functional (Interface)
 * Retension
 */
public class Java5Annotations {
    public static void main(String... args){
        Java5Annotations j5o=new Java5Annotations();
        j5o.run_override_annotation_example();
       
      }

      @Override
      public String toString(){
          return "Annotation is introduced in Java5";
      }
    
    public void run_override_annotation_example(){
        out.printf("\nthis.toString() has @override annoation and itsouput is %s\n",this.toString());
    }

    
}
