package learn.j.java5.varargs;

import java.util.Optional;

import static java.lang.System.out;

public class MyVarargs {
    public Integer sum(Integer... integers) {
        int sum = 0;
        for (int integer : integers) {
            sum += integer;
        }
        return sum;
    }

    public void print(Object... integers) {
        for (Object obj : integers) {
            if (obj != null) {
                out.printf(" %s %s \n", obj, obj.getClass());
            } else {
                out.printf("object is %s\n", obj);
            }
        }
    }

    public <T extends Integer> void gprint(T... ts) {
        for (T obj : ts) {
            out.printf("gprint_T_Int %s %s \n", Optional.ofNullable(obj).orElse(null), Optional.ofNullable(obj).map(o -> o.getClass().getName()).orElse("NOClassEmpty"));

        }
    }
    public <T> void another(T... ts) {
        for (T obj : ts) {
            out.printf("gprint_T %s %s \n", Optional.ofNullable(obj).orElse(null), Optional.ofNullable(obj).map(o -> o.getClass().getName()).orElse("NOClassEmpty"));

        }
        if (ts==null){
            out.println("ts is Null");
        }else if(ts.length==0){
            out.println("ts length is zero");
        }
    }
    public <T> void gprint(T... ts) {
        for (T obj : ts) {
            out.printf("gprint_T %s %s \n", Optional.ofNullable(obj).orElse(null), Optional.ofNullable(obj).map(o -> o.getClass().getName()).orElse("NOClassEmpty"));

        }
    }

    public <T extends String> Integer gprint(T... ts) {
        for (T obj : ts) {
            out.printf("gprint_T_String %s %s \n", Optional.ofNullable(obj).orElse(null), Optional.ofNullable(obj).map(o -> o.getClass().getName()).orElse("NOClassEmpty"));
        }
        return ts.length; //AutoBoxing
    }

    @Override
    public String toString() {
        return "MyVargsClassString";
    }
}