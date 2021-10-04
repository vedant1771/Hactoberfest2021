import java.util.*;
public class armstrong
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Armstrong numbers under 1000 are:");
    
       for (int i=1;i<1000;i++)
            {
                  int nd=0;double sd=0;
       for (int k=i;k>=1;k=k/10)
       {
              nd++;
    }
 for (int j=i;j>=1;j=j/10)
    {
              int d=j%10;
              sd=sd+(Math.pow(d,nd));
    }
    if(sd==i)
         System.out.println(i);
   }
}
}