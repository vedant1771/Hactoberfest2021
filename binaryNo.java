// Check given number is a Binary Number or not

public class Main {
	
	public static void isBinary (int number) {
		boolean isBinary = true;
		int copy = number;
		while (copy != 0) {
			int rem = copy % 10;
			if(rem > 1) {
				isBinary = false;
				break;
			}
			else {
				copy = copy / 10;
			}
		}
		if (isBinary) {
			System.out.println(number + " is a binary no.");
		} else {
			System.out.println(number + " is not a binary no.");
		}
	}
	
	public static void main(String[] args) {
		// Check given number is a Binary Number
		isBinary(1011);
		
	}

}
