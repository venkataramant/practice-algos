package tvr.learn.java.design_pattern.creational;

public class MySingleton {
    private static volatile MySingleton myself; // read from memory
    private String data=null;
    private MySingleton(String input1,int input2){
        this.data=new StringBuilder().append(input1)
                                    .append("::")
                                    .append(input2)
                                    .toString();
    }
    public String getData(){
        return this.data;
    }
    public static MySingleton getInstance(String input1,int input2){
        if (myself==null){
            synchronized(MySingleton.class){
                if (myself==null){
                    myself=new MySingleton(input1,input2);
                }
            }
        }
        return myself;
    }

    public MySingleton getInstance2(String input1,int input2){ // optimized
        MySingleton result=myself;
        if (result==null){
            synchronized(MySingleton.class){
                result=myself;
                if (result==null){
                    result=myself=new MySingleton(input1, input2);
                }
            }
        }
        return result;
    }

}
