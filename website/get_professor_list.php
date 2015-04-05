<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
$mysqli = new mysqli('localhost','root','lahacks2015','classviewer');
$myArray = array();

$major = $mysqli->real_escape_string($_GET["major"]);
$course_number = $mysqli->real_escape_string($_GET["course_number"]);
$year = $mysqli->real_escape_string($_GET["year"]);
$quarter = $mysqli->real_escape_string($_GET["quarter"]);

$query = "SELECT professor, lecture_number FROM class WHERE major = '".$major."' AND course_number = '".$course_number."' AND year = '".$year."' AND quarter = '".$quarter."' group by professor, lecture_number";

if ($result = $mysqli->query($query)) {

    while($row = $result->fetch_array(MYSQL_ASSOC)) {
        $myArray[] = $row;
    }
    echo json_encode($myArray);
}

$result->close();
$mysqli->close();
?>