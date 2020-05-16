<?php
$object = json_decode(file_get_contents("php://input"), true);

$servername = "localhost";
$usernameDb = "root";
$passwordDb = "";
$db = "news";

// Create connection
$conn = mysqli_connect($servername, $usernameDb, $passwordDb, $db);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
var_dump($object);
$title = $object["title"];
$text = $object["text"];
$producer = $object["producer"];
$category = $object["category"];
$date = $object["date"];


$query = "UPDATE `news` SET  `content` = '$text', `producer`='$producer',
                  `datePublished`='$date', `category` = '$category'  WHERE `title`='$title'";

mysqli_query($conn, $query);
mysqli_close($conn);
?>

//background-image: url('pics/background.jpg');