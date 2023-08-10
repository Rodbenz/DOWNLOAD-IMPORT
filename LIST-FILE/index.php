<?php
// connect and login to FTP server
try{
set_time_limit(300);//for setting 
$path='/usr/sap/trans/Interface/GIS';
$ftp_server = "192.168.100.24";
$ftp_username = "gisuser";
$ftp_userpass = "gis!1234";
$ftp_conn = ftp_connect($ftp_server) or die("Could not connect to $ftp_server");
$login = ftp_login($ftp_conn, $ftp_username, $ftp_userpass);

// then do something...
// check connection and login result
if ((!$ftp_conn) || (!$login)) { 
    echo "Fail</br>";
} else {
    // echo "Success</br>";
    // enabling passive mode
    ftp_pasv( $ftp_conn, true );
    // get contents of the current directory
    $contents = ftp_nlist($ftp_conn, $path);
    // print_r($contents);
    if($contents){
        foreach ( $contents as $item ) {
            $data[] = $item . PHP_EOL;
        }
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
    }else{
        echo json_encode([], JSON_UNESCAPED_UNICODE);
    }
   
}
} catch (\Throwable $th) {
    //throw $th;
    // echo json_encode([], JSON_UNESCAPED_UNICODE);
}
// close connection
ftp_close($ftp_conn);
?>