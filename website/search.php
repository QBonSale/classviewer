<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
$mysqli = new mysqli('localhost','root','lahacks2015','classviewer');
$myArray = array();

$empty = true;
$whereClause = "";

foreach($_GET as $query_string_variable => $value) {
    //echo "$query_string_variable  = $value <Br />";
    if(!$empty) {
        $whereClause = $whereClause . " AND ";
    }
    $empty = false;
    $whereClause = $whereClause . $query_string_variable . " = " . $value;
}

//echo $whereClause . "<Br />";

$query = "SELECT * FROM class";

if($whereClause != "") {
    $query = $query . " WHERE " . $whereClause;
}

//echo $query . "<Br />";

if ($result = $mysqli->query($query)) {

    while($row = $result->fetch_array(MYSQL_ASSOC)) {
        $myArray[] = $row;
    }
    echo json_encode($myArray);
}

$result->close();
$mysqli->close();
?>
