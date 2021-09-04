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

        echo date("Y-m-d h:i:sa")
?>




		<br>
                <br>
                <b>Display Driver Script Status</b><br>
                pi@raspberrypi:~ $ systemctl status rpi_7seg | grep Active<br>

<?php
        $service = "rpi_7seg";
        $systemctl_status = shell_exec("systemctl status $service | grep Active");
        echo "&emsp; $systemctl_status";
?>



                <br>
		<br>
                <b>Script Run Logs</b><br>
		<div style="height:200px;width:500px;overflow:auto;background-color:grey;color:black;font-family:sans-serif;padding:10px;">

<?php
	$log_file = fopen("/home/pi/rpi-clock/log/startup.log", "r");

	if( $log_file )
	{
		while(! feof($log_file) )
		{
			$log_line = fgets($log_file);
			echo $log_line . "<br>";
		}
	}
	else
	{
		echo "There was an error in the opening file";
	}

	fclose( $log_file );
?>

                </div>



        </body>
</html>
