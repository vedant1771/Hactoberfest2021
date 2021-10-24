<!DOCTYPE html>
<html>
<body>
    <?php
    $num1 = 70;
    $num2 = 100;
    $num3 = 10;

    echo "Num1 is 70 <br>";
    echo "Num2 is 100 <br>";
    echo "Num3 is 10 <br><br>";

   if( $num1 > $num2 ) {
       if ( $num3 > $num1 ) {
           echo "Num3 which is $num3 is biggest <br> ";
       }else {
        echo "Num1 which is $num1  is biggest <br> ";
       }
   }else {
        if ( $num3 > $num2 ) {
            echo "Num3 which is $num3  is biggest <br> ";
        }else{
            echo "Num2 which is $num2  is biggest <br> ";
        }
   }    
?>
</body>
</html>