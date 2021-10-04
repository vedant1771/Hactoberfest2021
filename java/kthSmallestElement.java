import java.util.Arrays;
import java.util.Scanner;

public class kthSmallestElement {
    public static int kthSmallest(int a[], int k) {
        Arrays.sort(a);
        return a[k - 1];
    }

    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int a[] = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        int k;
        System.out.println("Enter k , k Should be smaller than n");
        k = sc.nextInt();
        if (k < n)
            System.out.println("kth smallest element is " + kthSmallest(a, k));
        else
            System.out.println("k is greater than n");
    }
}
