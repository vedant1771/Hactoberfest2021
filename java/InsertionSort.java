import java.util.Arrays;

public class InsertionSort {
    public static void sort(int a[])
    {
        int n = a.length;
        for(int i=1;i<n;i++)
        {
            int temp = a[i];
            int j = i-1;
            while(j>=0 && a[j] > temp)
            {
                a[j+1] = a[j];
                j--;
            }
            a[j+1] = temp;
        }
    }

    public static void main(String[] args) {
        int a[] = {2,5,4,8,9,7,6,1,3};
        System.out.println(Arrays.toString(a));
        sort(a);
        System.out.println(Arrays.toString(a));
    }
}
