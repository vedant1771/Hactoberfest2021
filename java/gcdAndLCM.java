import java.util.*;
import java.util.Scanner;

public class gcdAndLcm {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scn = new Scanner(System.in);
		int num1 = scn.nextInt();
		int num2 = scn.nextInt();

		// To find GCD
		int n = num1;
		int m = num2;
		int r = 1;
		while (r != 0) {
			r = m % n;
			m = n;
			if (r == 0) {
				break;
			}
			n = r;
		}
		System.out.println(n);

		// To find LCM
		num1 = num1 / n;
		num2 = num2 * num1;
		System.out.println(num2);
	}
}
