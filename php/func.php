<?php

session_start();

function parseXml($doc) {

    libxml_disable_entity_loader(false);
    $dom = new DOMDocument('1.0', 'utf-8');
    $dom-> loadXML($doc, LIBXML_NOENT | LIBXML_DTDLOAD);
    
    // print $dom->saveXML();
    // echo ;

    $result = simplexml_import_dom($dom);
    if(!$result) {
        die('Error loading xml');
    }

    // print_r($result);
    return $result;
}


function check_session() {
    if (!isset($_SESSION['run'])){
        print_r("SESSION UNSET");
        die("Unauthorized");
    }
    else{
        print_r("SESSION SET");
    }
}

function getIPAddress() {  
    //whether ip is from the share internet  
     if(!empty($_SERVER['HTTP_CLIENT_IP'])) {  
                $ip = $_SERVER['HTTP_CLIENT_IP'];  
        }  
    //whether ip is from the proxy  
    elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {  
                $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];  
     }  
    //whether ip is from the remote address  
    else{  
        $ip = isset($_SERVER["REMOTE_ADDR"]) ? $_SERVER["REMOTE_ADDR"] : '127.0.0.1';
     }  

     print_r($ip);
     return $ip;  
}  

?>