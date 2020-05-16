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

    $id = $_GET["id"];
    $query = "SELECT * FROM `news` where `Nid`='$id'";
    $result = mysqli_query($conn, $query);
    if(mysqli_num_rows($result)==0)
        echo "No news";
    else{
        $row = mysqli_fetch_array($result);
        $myObj = new \stdClass();
        $myObj->title = $row['title'];
        $myObj->date = $row['datePublished'];
        $myObj->category  = $row['category'];
        $myObj->text = $row['content'];
        echo json_encode($myObj);
            
    }
    mysqli_close($conn);

?>