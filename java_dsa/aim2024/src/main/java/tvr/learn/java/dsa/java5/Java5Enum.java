package tvr.learn.java.dsa.java5;
import static java.lang.System.out;
import tvr.learn.java.dsa.java5.enum_ex.MyStatusEnum;

public class Java5Enum {
    public static void main(String... args){
        Java5Enum j5enum=new Java5Enum();
        j5enum.loop_enums();
        out.println(j5enum.check_enum(MyStatusEnum.NoStatus1));
        out.println(j5enum.check_enum(MyStatusEnum.NoStatus2));
        out.println(j5enum.check_enum(MyStatusEnum.Status1));
        out.println(j5enum.check_enum(MyStatusEnum.Status2));
        
        System.out.println(MyStatusEnum.valueOf("Status1"));
        try{
            System.out.println(MyStatusEnum.valueOf("Status4"));
        }catch(IllegalArgumentException ex){
            System.err.println(ex);
        }
       
    }
    private void loop_enums(){
        for (MyStatusEnum status:MyStatusEnum.values()){
            System.out.println(status+"::"+ status.ordinal()+".."+status.getStatus());
        }
    }
    private String check_enum(MyStatusEnum status){
        switch(status){
            case Status1:
                return "status1 "+status.ordinal()+"::"+status.getStatus();
            case NoStatus1:
                return "NoStatus1 "+status.ordinal()+"::"+status.getStatus();
            default:
                return "default "+status.name()+"," +status.ordinal()+"::"+status.getStatus();
        }
    }
}
