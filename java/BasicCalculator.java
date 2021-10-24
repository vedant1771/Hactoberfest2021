import java.util.Scanner;
class BasicCalculator
{
  public static void main (String args[])
  {
    System.out.println ("Enter the string expression: (like-  2-1 + 2 )");
    Scanner sc = new Scanner (System.in);
    // String input
      result (sc.nextLine ());
  }
  public static void result (String s)
  {
    // Initialization
    int[] opArray = new int[30]; //for making a operation stack
    int top = -1;             //for stack
    int operand = 0;
    int answer = 0;              // For the on-going answer
    int sign = 1;              // 1 means positive, -1 means negative (for easy to calcutale)
    int i = 0;
    char ch;
    while (i < s.length ())
      {
 ch = s.charAt (i);
 if (ch == '+')
   {
     answer += sign * operand;
     sign = 1;
     operand = 0;
   }
 else if (ch == '-')
   {
     answer += sign * operand;
     sign = -1;
     operand = 0;
   }
 else if (ch == '(')
   {
     // (answer outside parenthesis) + (sign * (anwswer from parenthesis))
     if (top > 27)
       {
 System.out.println ("sorry, too many ()");
 return;
       }
     opArray[++top] = answer;
     opArray[++top] = sign;
     sign = 1;
     answer = 0;
   }
 else if (ch == ')')
   {
     // (answer outside parenthesis) + (sign * (answer from parenthesis))
     answer += sign * operand;
     answer *= opArray[top--];
     answer += opArray[top--];
     operand = 0;
   }
 else if (ch == ' ')
   {
     // for " " -space nothing to do
   }
 else if (Character.isDigit (ch))
   {
     //operand can be more 9 i.e. more than 1 digit
     operand = 10 * operand + (int) (ch - '0');
   }
 else
   {
     System.out.println ("invaild input");
     return;
   }
 i++;
      }
    System.out.println (answer + (sign * operand));
  }
}
