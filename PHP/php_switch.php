<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>switch</title>
</head>
<body>

	<?php 
	
		# A: Administrator, P: Power User, U: User, G: Guest

		$user_group_code = "A";

		switch ($user_group_code) {
			case 'A':
				
				echo "User Group: Administrator <br>";
				break;			

			case 'P':
				
				echo "User Group: Power User <br>";
				break;			

			case 'U':
				
				echo "User Group: User <br>";
				break;			

			case 'G':
				
				echo "User Group: Guest <br>";
				break;
			
			default:
				echo "Invalid User Group!!! ";
				break;
		}

	 ?>
	
</body>
</html>