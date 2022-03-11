<?php 
// D:\GitAssignment\Flask\Flask\php\process.php
require 'func.php';

function getOrder($xml){
    $order = parseXml($xml);
    $title = str_replace(" ", "%20", $order->name[0]);
    $res = str_replace(" ", "%20", "Order Received!");

    $cmd = 'curl "http://localhost:5000/XXE/?form='.$res.'&res=true&title='.$title.'"';
    
    shell_exec($cmd);
}

getOrder($argv[1]);