<?php
    putenv('ODBCSYSINI=/usr/local/etc'); 
    putenv('ODBCINI=/usr/local/etc/odbc.ini'); 
    $username = "root"; 
    $password = "test123!"; 
    try { 
        $db = new PDO("odbc:MySQLServer", "$username", "$password"); 
    } catch (PDOException $exception) { 
      echo $exception->getMessage(); 
      exit; 
    }
?>