
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

    $query = "SELECT * FROM `news`";
    $result = mysqli_query($conn, $query);
    if(mysqli_num_rows($result)==0)
        echo "No news";
    else{
        
        while($row = mysqli_fetch_array($result))
        {
            echo "<table>";
            echo "<tr><td>",$row['title'],"</td><td>",$row['datePublished'],"</td><td>Category: ",$row['category'],"</td><td>",$row['producer'],"</td>";
            echo "<tr><td colspan=4>",$row['content'],"</td></tr>";
            //echo "<tr><td colspan=4><button type='button' onclick='update(",$row['nID'],")'>Update news</button></td></tr>";
            echo "</table>";

        };
    }
    mysqli_close($conn);

?>