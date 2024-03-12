package tvr.learn.java5;

import static java.lang.System.out;

import java.util.Formatter;

import tvr.learn.java5.scanner_formatter.MyScanner;

public class Scanner {
    public static void main(String[] args){
        MyScanner ms=new MyScanner();
        
        int grade=ms.getInt("Whats your grade");
        String name=ms.getLine("whats your name");
        Formatter fm=new Formatter(out);
        fm.format("format example name %s grade %d", name,grade);
        fm.close();
    }
}
