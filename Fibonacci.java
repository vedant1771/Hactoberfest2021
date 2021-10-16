import java.util.*;
public class fibonacci {
    void cal(int n){
        int a=1,b=1;
        System.out.print(a+" "+b+" ");
        for(int i=2;i<n;i++){
            int d=a+b;
            System.out.print(d+" ");
            a=b;
            b=d;
        }
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter number of elements you want in series:");
        int n=sc.nextInt();
        fibonacci ob=new fibonacci();
        ob.cal(n);
    }
}
