<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
$mysqli = new mysqli('localhost','root','lahacks2015','classviewer');
$myArray = array();

$major = $mysqli->real_escape_string($_GET["major"]);
$course_number = $mysqli->real_escape_string($_GET["course_number"]);

$query = "SELECT year, quarter FROM class WHERE major = '".$major."' AND course_number = '".$course_number."' group by year, quarter";

if ($result = $mysqli->query($query)) {

    while($row = $result->fetch_array(MYSQL_ASSOC)) {
        $myArray[] = $row;
    }
    echo json_encode($myArray);
}

$result->close();
$mysqli->close();
?>