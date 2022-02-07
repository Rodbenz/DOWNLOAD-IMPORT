<?php
    // $out = shell_exec('ipconfig/all');
    // echo '<pre>'.$out.'</pre>';
    //  exec('C:\Windows\System32\cmd.exe /c START D:\TESTFILE.BAT\TESTBAT.bat');
    // echo '<pre>'.$out.'</pre>';
    pclose(popen("start /B TESTFILE.BAT/TESTBAT.bat", "r")); die();
?>