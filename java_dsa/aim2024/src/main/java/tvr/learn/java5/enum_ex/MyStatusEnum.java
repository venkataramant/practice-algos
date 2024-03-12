package tvr.learn.java5.enum_ex;

public enum MyStatusEnum {
    NoStatus1,NoStatus2,NoStatus3,Status1(1),Status2(1),Status3(2),; // Named Constants
    // oridnal() returns integer/sequence number
    private int status=-1;
    private MyStatusEnum(int status){
        this.status=status;
    }
    private MyStatusEnum(){

    }
    public int getStatus(){
        return this.status;
    }
}

/*
    java.lang.Enum
 * Methods
 * 
 * values()
 * ordinal()
 * 
 * 
 */
