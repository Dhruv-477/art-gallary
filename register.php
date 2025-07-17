<?php
$servername = "localhost";
$username = "root"; 
$password = ""; 
$dbname = "art_gallery";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $date = $_POST['date'];
    $guests = (int)$_POST['guests'];
    $message = trim($_POST['message']);

    $stmt = $conn->prepare("INSERT INTO bookings (name, email, date, guests, message) VALUES (?, ?, ?, ?, ?)");
    $stmt->bind_param("sssds", $name, $email, $date, $guests, $message);

    if ($stmt->execute()) {
        echo "Booking submitted successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}
?>
