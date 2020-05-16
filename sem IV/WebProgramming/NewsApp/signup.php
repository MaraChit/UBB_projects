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
$username = $object["username"];
$password = $object["password"];

$query = "INSERT INTO `admin` (`username`, `passwordAdmin`) VALUES ('$username', '$password')";
mysqli_query($conn, $query);
mysqli_close($conn);
?>