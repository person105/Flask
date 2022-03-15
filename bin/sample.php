<?php 

require 'funcs.php';
session_start();

function genmap($xml){
    $mapConfig = parseXml($xml);

    if(!isset($mapConfig -> name)){
        die("Needs name");
    }
    if(!isset($mapConfig -> country)){
        die("Needs one country");
    }

    if(is_string($mapConfig["country"])){
        $mapConfig["country"] = array($mapConfig["country"]);
    
    }

    $validated = array();
    foreach ($mapConfig -> country as $country) {
        if (preg_match('/[A-Z]{2}'. $country)){
            array_push($validated, $country);
        }
    }

    if(count($validated) < 1) {
        die("Needs one country");
    }

    $target = "localhost:5000/XXE/?country[]=" . join("&country[]=", $validated) . "&name" . urlecode($mapConfig -> name);

    $ch = curl_init();

    if(!$ch) {
        die("Error init curl");
    }
    if(!$curl_setopt($ch, CURLOPT_URL, $target)) {
        die("Error setting target in curl");
    }
    if(!$curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1)) {
        die("Error setting opt in curl");
    }

    $output = curl_exec($ch);

    if(!$output) {
        die('No output');
    }

    curl_close($ch);
    echo $output;
}

genmap($_POST['xml']);