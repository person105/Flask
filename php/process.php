<?php 
// D:\GitAssignment\Flask\Flask\php\process.php
require 'func.php';
session_start();

function getOrder($xml){
    $order = parseXml($xml);
    print_r($order);

    $res = "Got your order!";

    $cmd = "curl -d 'form={$res}&res=true' http://127.0.0.1:5000/XXE/ ";
    
    echo shell_exec($cmd);

}



// echo htmlentities($argv[1]);
getOrder($argv[1]);