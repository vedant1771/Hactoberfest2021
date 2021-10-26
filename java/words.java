import java.util.*;
public class words {

    public static void main(String[] args)
     {
             Scanner sc=new Scanner(System.in);
             System.out.println("Enter a string:");
            String s = sc.nextLine();
     
            int count = 1;
     
            for (int i = 0; i < s.length() - 1; i++)
            {
                if ((s.charAt(i) == ' ') && (s.charAt(i + 1) != ' '))
                {
                    count++;
                }
            }
            System.out.println("Number of words in the string : " + count);
        }
    }
     