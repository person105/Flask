<?php

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

?>