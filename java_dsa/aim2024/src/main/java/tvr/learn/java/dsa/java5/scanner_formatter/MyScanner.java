package tvr.learn.java.dsa.java5.scanner_formatter;

import java.util.Scanner;
import static java.lang.System.in;
import static java.lang.System.out;
public class MyScanner {
    Scanner MyScanner;
    public MyScanner(){
        this.MyScanner=new Scanner(in);
    }
    @Override
    public void finalize(){
        this.MyScanner.close();
    }
    public String getLine(String prompt){
        out.println(prompt+" :: ");
        return this.MyScanner.nextLine();
    }
    public int getInt(String prompt){
        out.println(prompt+" :: ");
        return this.MyScanner.nextInt();
    }
}
