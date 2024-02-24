package tvr.learn.java.dsa.java5;

import java.util.Formatter;
import static java.lang.System.out;
import tvr.learn.java.dsa.java5.scanner_formatter.MyScanner;

public class Java5Scanner {
    public static void main(String[] args){
        MyScanner ms=new MyScanner();
        
        int grade=ms.getInt("Whats your grade");
        String name=ms.getLine("whats your name");
        Formatter fm=new Formatter(out);
        fm.format("format example name %s grade %d", name,grade);
        fm.close();
    }
}
