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

        </body>
</html>
