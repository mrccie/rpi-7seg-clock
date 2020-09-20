<!DOCTYPE html>
<html>

        <body style="background-color:#ff69b3;">

		<h1>Configuration Updated!</h1>

		<h2>Change Made:</h2>


<?php

        $error = FALSE;

	// !-------- Only Execute One Change --------!

	// !-- Set variables
	$webconfig_path="/var/www/html/7seg_files";

	// !-- EasyName all input
	$in_sysopt = $_POST['sys_opt'];
	$in_web_config = $_POST['web_config'];
	$in_web_interface = $_POST['web_interface'];

	// Do the things
	if( $in_sysopt == "reboot" )
	{
		echo "<b>Rebooting the System</b><br>";
		echo "This change may take a minute to process.";

		// Create the named file, content irrelevant
		$file = fopen("$webconfig_path/reboot-server","w")
			or die("Unable to create reboot-server file!");
		fwrite($file, 'reboot');
		close($file);
	}
	elseif( $in_sysopt == "shut_down" )
	{
		echo "<b>Shutting Down the System</b><br>";
		echo "This change may take a minute to begin.";

		// Create the named file, content irrelevant
		$file = fopen("$webconfig_path/shutdown-server","w")
			or die("Unable to create shutdown-server file!");
		fwrite($file, 'shutdown');
		close($file);
	}
	elseif( $in_web_config == "True" )
	{
		echo "<b>Now using configuration from the web interface</b><br>";
		echo "This change may take a minute to begin.";

		// Read in the current config file
		$in_env_file = fopen("./7seg_files/webconfig.conf", "r");
		while( !feof( $in_env_file ) )
		{
			$line = trim(fgets($in_env_file));
			$lineA = explode("=", $line);
			$env_data[$lineA[0]]=$lineA[1];
		}
		fclose( $in_env_file );

		// Update WEB_CONFIG
		$env_data[WEB_CONFIG] = "True";

		// Write out new file
		$out_env_file = fopen('./7seg_files/webconfig.conf', 'w')
				or die("Unable to write to config file!");
		foreach( $env_data as $key=>$value )
		{
			if( $key != "" )
			{
				fwrite($out_env_file, "$key=$value\n");
			}
		}
		fclose( $out_env_file );
	}
	elseif( $in_web_config == "False" )
	{
		echo "<b>No longer using configuration from the web interface</b><br>";
		echo "Only values coded in the script will be used until this is restored.<br>";

		// Read in the current config file
		$in_env_file = fopen("./7seg_files/webconfig.conf", "r");
		while( !feof( $in_env_file ) )
		{
			$line = trim(fgets($in_env_file));
			$lineA = explode("=", $line);
			$env_data[$lineA[0]]=$lineA[1];
		}
		fclose( $in_env_file );

		// Update WEB_CONFIG
		$env_data[WEB_CONFIG] = "False";

		// Write out new file
		$out_env_file = fopen('./7seg_files/webconfig.conf', 'w')
				or die("Unable to write to config file!");
		foreach( $env_data as $key=>$value )
		{
			if( $key != "" )
			{
				fwrite($out_env_file, "$key=$value\n");
			}
		}
		fclose( $out_env_file );
	}
	elseif( $in_web_interface == "disable" )
	{
		echo "<b>Disabling the web server</b><br>";
		echo "This change may take a minute to process.";

		// Create the named file, content irrelevant
		$file = fopen("$webconfig_path/disable-web","w")
			or die("Unable to create disable-web file!");
		fwrite($file, 'disable');
		close($file);
	}
	else
	{
		echo "<b>None?!</b><br>";
		echo "I guess you didn't pick anything or there was an error.";
	}


?>


                <br>
                <br>
                <form action="/index.html" method="post">
                        <input type="submit" value="Home">
                </form>

        </body>
</html>
