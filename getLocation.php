<?php
// if latitude and longitude are submitted
if (!empty($_POST['latitude']) && !empty($_POST['longitude'])) {
    // send request and receive json data by latitude and longitude
    $url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='.trim($_POST['latitude']).','.trim($_POST['longitude']).'&sensor=false';
    $json = @file_get_contents($url);
    $data = json_decode($json);
    $status = $data->status;
    
    // if request status is successful
    if ($status == "OK") {
        // get address from json data
        $location = $data->results[0]->formatted_address;
    } else{
        $location =  '';
    }
    
    // return address to ajax 
    echo $location;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Get Visitor Location Using Html5 Geolocation API & PHP</title>
</head>
<body>
    <p>Your Location: <span id="location"></span></p>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script>
          $(document).ready(function() {
              if (navigator.geolocation) {
                  navigator.geolocation.getCurrentPosition(showLocation);
              } else { 
                  $('#location').html('Geolocation is not supported by this browser.');
              }
          });

          function showLocation(position) {
              var latitude = position.coords.latitude;
              var longitude = position.coords.longitude;
              $.ajax({
                  type:'POST',
                  url:'getLocation.php',
                  data:'latitude='+latitude+'&longitude='+longitude,
                  success:function(msg) {
                      if (msg) {
                         $("#location").html(msg);
                      } else {
                          $("#location").html('Not Available');
                      }
                  }
              });
          }
    </script>
</body>
</html>
