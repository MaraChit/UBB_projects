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
    $query = "SELECT * FROM `admin` WHERE `username`='$user'";
    $result = mysqli_query($conn, $query);
    if(mysqli_num_rows($result)==0)
        echo "false";
    else{
        $row = mysqli_fetch_array($result);
        echo $row['aID'];
    }
    mysqli_close($conn);

?>