<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
$mysqli = new mysqli('localhost','root','lahacks2015','classviewer');
$myArray = array();

$year = $mysqli->real_escape_string($_GET["year"]);
$quarter = $mysqli->real_escape_string($_GET["quarter"]);
$major = $mysqli->real_escape_string($_GET["major"]);
$course_number = $mysqli->real_escape_string($_GET["course_number"]);
$lecture_number = $mysqli->real_escape_string($_GET["lecture_number"]);

$query = "SELECT * FROM class_over_time WHERE" . 
       " major = '" . $major . 
       "' AND year = '" . $year .
       "' AND quarter = '" . $quarter .
       "' AND course_number = '" . $course_number . 
       "' AND lecture_number = '" . $lecture_number .
       "' ORDER by snapshot_time asc";

if ($result = $mysqli->query($query)) {

    while($row = $result->fetch_array(MYSQL_ASSOC)) {
        $myArray[] = $row;
    }
    echo json_encode($myArray);
}

$result->close();
$mysqli->close();
?>