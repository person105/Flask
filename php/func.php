<?php

function parseXml($doc) {

    libxml_disable_entity_loader(false);
    $dom = new DOMDocument();
    if (!$dom-> loadXML($doc, LIBXML_NOENT | LIBXML_DTDLOAD)) {
        die('Error loading xml');
    }

    $result = simplexml_import_dom($dom);
    if(!$result) {
        die('Error loading xml');
    }

    echo($result);
    return $result;
}

?>