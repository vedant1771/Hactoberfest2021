<?php

// Associative Array Sorting
$age = array("a" => "45" , "b" => "33" , "c" => "99");

// Sorting
// here we use ksort
ksort($age);
print_r($age);

// Reverse Sorting
krsort($age);
print_r($age);

?>