<html>
<body>

<?php

$marks = 90;

if ($marks >= 60)
{
    $grade = "First Division";
} 
else if ($marks >= 40)
{
    $grade = "Second Division";
}
else if ($marks >= 33)
{
    $grade = "Third Division";
}
else 
{
    $grade = "Fail";
}
echo "Student Grade: $grade";
?>

</body>
</html>
