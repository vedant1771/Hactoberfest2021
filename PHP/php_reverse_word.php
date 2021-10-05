<?php
$arr = range(1, 7);
$countArr = count($arr);
print_r($arr);

for ($i = 0; $i < count($arr); $i++) {
    print_r($arr[$i]);
    for ($j = $countArr - 1; $j > 0; $j--) {
        echo 0;
    }
    $countArr--;

    echo PHP_EOL;
}
