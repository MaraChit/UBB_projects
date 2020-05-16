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

    $from = $_GET["from"];
    $to = $_GET["to"];
    $category = $_GET["category"];
    $prev = 0;
    $query = "SELECT * FROM `news`";
    
    if($from != "")
    {
        $query = $query . " WHERE `datePublished` >= '$from'";
        $prev = 1;
    }
    if($to != "")
    {
        if($prev == 1)
            $query = $query . " AND";
        else
            $query = $query . " WHERE";
        $query = $query . " `datePublished` <= '$to'";
        $prev = 1;
    }
    if($category != "")
    {
        if($prev == 1)
            $query = $query . " AND";
        else
            $query = $query . " WHERE";
        $query = $query . " `category` = '$category'";
        $prev = 1;
    }


    $result = mysqli_query($conn, $query);

    if(mysqli_num_rows($result)==0)
        echo "No news";
    else{
        
        while($row = mysqli_fetch_array($result))
        {
            echo "<table>";
            echo "<tr><td>",$row['title'],"</td><td>",$row['datePublished'],"</td><td>Category: ",$row['category'],"</td><td>",$row['producer'],"</td>";
            echo "<tr><td colspan=4>",$row['content'],"</td></tr>";
            echo "</table>";

        };
    }
    mysqli_close($conn);


?>