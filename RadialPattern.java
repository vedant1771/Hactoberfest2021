import java.util.Scanner;

public class RadialPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int dec = 0;
        int inc = 0;
        int cons = 2 * n - 1;

        for (int i = 1; i <= 2 * n - 1; i++) {
            int val = n;
            // loop for decreasing
            for (int j = 1; j <= dec; j++) {
                System.out.print(val + "\t");

                val--;
            }

            // loop for constant
            for (int j = 1; j <= cons; j++) {
                System.out.print(val + "\t");

            }

            // loop for increasing
            for (int j = 1; j <= inc; j++) {
                val++;
                System.out.print(val + "\t");

            }

            // updating inc,dec,cons
            if (i < n) {
                inc++;
                dec++;
                cons -= 2;
            } else {
                cons += 2;
                inc--;
                dec--;

            }
            System.out.println();
        }

        sc.close();
    }
}
