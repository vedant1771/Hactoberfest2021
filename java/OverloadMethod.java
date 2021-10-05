public class OverloadMethod {
 static int plusnum( int x,int y){
     return x+y;
 }
 static String plusnum( String x,String y){
    return x+y;
}
public static void main (String[] args ){
    int num1= plusnum(8,3);
    String num2= plusnum("names","play");
    System.out.println("int ="+num1);
    System.out.println("string="+num2);
   
}



}
