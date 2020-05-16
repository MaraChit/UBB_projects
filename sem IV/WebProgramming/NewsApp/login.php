<?php
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

    $user = $_GET["user"];
    $pass = $_GET["password"];
	
    $query = "SELECT * FROM `admin` WHERE `username`='$user' and `passwordAdmin`='$pass'";
    $result = mysqli_query($conn, $query);
    if(mysqli_num_rows($result)==0)
        echo "false";
    else{
        $row = mysqli_fetch_array($result);
        $myObj = new \stdClass();
        $myObj->id = $row['aID'];
        $myObj->name= $row['username'];
        echo json_encode($myObj);
    }
    mysqli_close($conn);

?>