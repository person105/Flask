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
        <h1 style="color:white">You have redirected the admin to the attackers website upon viewing of the feedback</h1>
        <div id="header" style="color:white">FLAG{Watch out for &lt &gt tags!}</div>
    </div>
</body>
</html>

