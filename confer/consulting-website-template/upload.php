<?php
$targetDir = "uploads/";
$targetFile = $targetDir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));
$message = "";

// Verificar si se ha enviado el formulario
if (isset($_FILES["fileToUpload"])) {
    // Crear la carpeta uploads si no existe
    if (!file_exists($targetDir)) {
        mkdir($targetDir, 0777, true);
    }

    // Verificar si hay errores en la carga
    if ($_FILES["fileToUpload"]["error"] !== 0) {
        $message = "Error al subir el archivo.";
        $uploadOk = 0;
    }

    // Verificar el tamaño del archivo
    if ($_FILES["fileToUpload"]["size"] > 500000) {
        $message = "Lo siento, tu archivo es demasiado grande.";
        $uploadOk = 0;
    }

    // Permitir ciertos formatos de archivo
    $allowedFileTypes = array('pdf', 'doc', 'docx', 'txt');
    if (!in_array($fileType, $allowedFileTypes)) {
        $message = "Lo siento, solo se permiten archivos PDF, DOC, DOCX y TXT.";
        $uploadOk = 0;
    }

    // Verificar si $uploadOk está configurado a 0 por un error
    if ($uploadOk == 0) {
        $message = "Lo siento, tu archivo no fue subido.";
    // Si todo está bien, intenta subir el archivo
    } else {
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $targetFile)) {
            $message = "El archivo " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " ha sido subido.";
        } else {
            $message = "Lo siento, hubo un error al subir tu archivo.";
        }
    }

    // Imprimir solo el mensaje
    echo $message;
}
?>
