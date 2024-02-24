package tvr.learn.java.dsa.java5;

import tvr.learn.java.dsa.java5.enum_ex.MyStatusEnum;

public class Java5EnhancedFor {
    public static void main(String... args){
        for (MyStatusEnum status:MyStatusEnum.values()){
            System.out.println(status+"::"+ status.ordinal()+".."+status.getStatus());
        }

       Integer[] myNums={1,2,3,4,5,6};
       for(Integer mynum: myNums){
        System.out.println("myNum::"+mynum);
       }

       int[] myNums2={7,8,9};
       for(Integer mynum: myNums2){
        System.out.println("Boxing(int to Integer)::"+mynum);
       }
       int[] myNums3=new int[0];
       for(Integer mynum: myNums3){
        System.out.println("Boxing(int to Integer)::"+mynum);
       }
       
    }
}
