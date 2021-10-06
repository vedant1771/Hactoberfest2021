// A CPP program to find GCD of two given positive integers and using only these arithmetic operations: 
//• Compare two integers.
//• Add two integers.
//• Subtract one integer from another.
//• Multiply/Divide a number by two


#include<bits/stdc++.h>
using namespace std;


bool isEven(long long int a) // Function to check whether given number is odd or even
{
	if ((a / 2) * 2 == a)
	{
		return true;
	}
	return false;
}

// maine function to find GCD
int GCD(long long int a, long long int b)
{
	if (a == b || a == 0)
	{
		return b;
	}
	else if (b == 0)
	{
		return a;
	}
	else if (isEven(a) && isEven(b))
	{
		return  2 * GCD(a / 2, b / 2);
	}
	else if (isEven(a) && (!isEven(b)))
	{
		return GCD(a / 2, b);
	}
	else if (!isEven(a) && isEven(b))
	{
		return GCD(a, b / 2);
	}
	else {
		if (a > b)
		{
			return GCD((a - b) / 2, b);
		}
		else
		{
			return GCD((b - a) / 2, a);
		}
	}
}

int main()
{
	long long int x , y ;
	cout << "Enter two number whose GCD to be calculated: ";
	cin >> x >> y;
	cout << "\nThe GCD of " << x << " and " << y << " is: " << GCD(x, y);


	return 0;
}
