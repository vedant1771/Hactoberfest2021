import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
public class JavaBigDecimal {
   
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<BigDecimal> bigDecimalList = new ArrayList<BigDecimal>();
        String[] stringArray = new String[n];
        String[] s = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
            bigDecimalList.add(new BigDecimal(stringArray[i]));
        }
        Collections.sort(bigDecimalList, Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            BigDecimal B = new BigDecimal(stringArray[i]);
            for (int j = 0; j < n; j++) {
                if (B.equals(bigDecimalList.get(j))) {
                    s[j] = stringArray[i];
                    bigDecimalList.set(j, null);
                    break;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println(s[i]);
        } 
    }
}
