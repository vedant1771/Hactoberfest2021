
import java.io.*;
import java.util.ArrayList;
  
 public class ArrayListDemo {
public static void main(String[] args)
    {
   ArrayList<Integer> arrlist = new ArrayList<Integer>(5);
       arrlist.add(100);
        arrlist.add(200);
        arrlist.add(250);
   for (Integer number : arrlist) {
            System.out.println("Number is  = " + number);
        }
    }
}