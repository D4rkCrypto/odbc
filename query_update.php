<?php
include 'config.php';
$stu_number = $_REQUEST['stu_number'];
echo "<script>location.href=\"admin_update.php?id=$stu_number\";</script>";
?>
