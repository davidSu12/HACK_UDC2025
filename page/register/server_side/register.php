<?php
$servername = "localhost";
$username = "user";
$password = "123456";
$database = "servicio";

$conn = new mysqli($servername, $username, $password, $database);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if($_SERVER["REQUEST_METHOD"] == "POST"){
    $nombre = $_POST["nombre"];
    $apellido = $_POST["apellido"];
    $password = $_POST["password"];
    $email = $_POST["email"];
    $sql = "INSERT INTO alumnos (nombre, apellido, password, email) VALUES ('$nombre','$apellido','$password',$email)";
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    }else{
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

}

