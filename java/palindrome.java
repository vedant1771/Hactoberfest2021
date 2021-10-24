import java.util.*;
class Palindrome {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a string:");
        String s = sc.nextLine();
        String s1="";

       for (int i = 0; i <= s.length() - 1; i++)
       {
           s1=s.charAt(i)+s1;
        }
        if (s.compareTo(s1)==0) {
            System.out.println("Palindrome");
        } else {
            System.out.println(" Not Palindrome");
        }
    }
}