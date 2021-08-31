<!DOCTYPE html>
<html>

    <body style="background-color:#ff69b3;">

		<h1>Raspberry Pi 7-Segment Clock</h1>

    <form action="/index.html" method="post">
            <input type="submit" value="<<< Go Back">
    </form>


		<h2>Diagnostics</h2>

    <b>Current Time</b><br>
<?php
  echo "Current date is: " . date("Y-m-d h:i:sa");
?>
    <br>
    <br>


    <b>Display Driver Script Status</b><br>
<?php
  $service = "rpi_7seg";
  function isactive($service) {
    $output = shell_exec("systemctl is-active $service");
    if (trim($output) == "active") {
      echo "<td style=\"color: green;\">Active</td>";
    }
    else {
      echo '<td style="color: red;">Inactive</td>';
    }
  }
?>


        </body>
</html>
