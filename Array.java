import java.util.*;
class Array
{
    public static void main(String args[])
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the limit of array");
        int l= in.nextInt();
        int arr[]= new int[l];
        int sum=0,n;
        System.out.println("Enter the elements of the array");
        for(int i=0;i<l;i++)
        {
            n=in.nextInt();
            sum=sum+n;
        }
        System.out.println("The sum is=/t"+ sum);



    }

}
