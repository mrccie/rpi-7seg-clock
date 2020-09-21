<!DOCTYPE html>
<html>

        <body style="background-color:#ff69b3;">

<?php

        $error = FALSE;

        // !-------- Read File --------!

        // Read in the current config file
        $in_env_file = fopen("./7seg_files/webconfig.conf", "r");
        while (!feof($in_env_file)) {
            $line = trim(fgets ($in_env_file));
            $lineA = explode("=", $line);
            $env_data[$lineA[0]]=$lineA[1];
        }
        fclose( $in_env_file );



        // !-------- Validate and Update Attributes --------!

        // Validate and update HOUR_FORMAT, if updated by user
        $in_hf = $_POST['hour_format'];
        if( $in_hf != "" )
        {
                if( $in_hf == "12" || $in_hf == "24" )
                {
                        $env_data[HOUR_FORMAT] = $in_hf;
                }
                else
                {
                        $error = TRUE;
                }
        }

        // Validate and update DIMMER_TYPE, if updated by user
        $in_dt = $_POST['dimmer_type'];
        if( $in_dt != "" )
        {
                if( $in_dt == "0" || $in_dt == "1" || $in_dt == "2" )
                {
                        $env_data[DIMMER_TYPE] = $in_dt;
                }
                else
                {
                        $error = TRUE;
                }
        }

        // Validate and update COLON_ON, if updated by user
        $in_dc = $_POST['display_colon'];
        if( $in_dc != "" )
        {
                if( $in_dc == "True" || $in_dc == "False" )
                {
                        $env_data[COLON_ON] = $in_dc;
                }
                else
                {
                        $error = TRUE;
                }
        }

        // Validate and update DIMMER_MIN, if updated by user
        $in_dmin = $_POST['dimmer_min'];
        if( $in_dmin != "" )
        {
                if( $in_dmin >= 0.0 && $in_dmin <= 1.0 )
		{
                        $env_data[DIMMER_MIN] = $in_dmin;
                }
                else
                {
                        $error = TRUE;
                }
        }

        // Validate and update DIMMER_MAX, if updated by user
        $in_dmax = $_POST['dimmer_max'];
        if( $in_dmax != "" )
        {
                if( $in_dmax >= 0.0 && $in_dmax <= 1.0 )
                {
                        $env_data[DIMMER_MAX] = $in_dmax;
                }
                else
                {
                        $error = TRUE;
                }
        }


        // !-------- Write to File --------!
        if( $error == FALSE )
        {

		$out_env_file = fopen('./7seg_files/webconfig.conf', 'w') or die("Unable to write to config file!");

                foreach( $env_data as $key=>$value )
                {
                        if( $key != "" )
			{
                                fwrite($out_env_file, "$key=$value\n");
                        }
                }
                fclose( $out_env_file );

        }
?>


                <h1>Configuration Updated!</h1>

                <h2>Current Settings:</h2>

<?php
	foreach( $env_data as $key=>$value )
	{
		if( $key != "" )
		{
			echo "<li>$key=$value<br>";
		}
	}	

?>
                <br>
                <br>
                <form action="/index.html" method="post">
                        <input type="submit" value="Go Back">
                </form>

        </body>
</html>
