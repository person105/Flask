<?php

require 'func.php';

$ip = getIPAddress();

if($ip != '127.0.0.1'){
    die("Unauthorized");
}
else{
    print_r("SESSION SET");
}

?>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

</head>
<body style="background:black">
    <div class="container">
        <div id="header" style="color:white">FLAG{Watch out for XML injections!}</div>
    </div>
</body>
</html>
