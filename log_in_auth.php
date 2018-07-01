<?php
$user_name = $_REQUEST['user_name'];
$password = $_REQUEST['password'];
$level = $_REQUEST['level'];
if($level=="administrator")
{
    $db = new SQLite3("student.sqlite");
    $query = "select * from admin WHERE user_name='$user_name' AND password='$password'";
    $result = $db->query($query);
    if(!$result){
        echo "<script>alert(\"数据库错误\")</script>";
        echo "<script>location.href=\"index.html\";</script>";
    }else{
        $item = $result->fetchArray();
        if($item){
            echo "<script>alert(\"管理员登录成功\")</script>";
            echo "<script>location.href=\"admin_index.html\";</script>";
        }else{
            echo "<script>alert(\"用户名或密码错误\")</script>";
            echo "<script>location.href=\"index.html\";</script>";
        }
    }
}else{
    $db = new SQLite3("student.sqlite");
    $query = "select * from student WHERE name='$user_name' AND password='$password';";
    var_dump($query);
    $result = $db->query($query);
    if(!$result){
        echo "<script>alert(\"数据库错误\");
                    location.href=\"index.html\";</script>";
    }else{
        $item = $result->fetchArray();
        if($item){
            echo "<script>alert(\"登录成功\")</script>";
            $student_number = $item['student_number'];
            echo "<script>location.href=\"student_index.php?id=$student_number\";</script>";
        }else{
            echo "<script>alert(\"用户名或密码错误\")</script>";
            echo "<script>location.href=\"index.html\";</script>";
        }

    }
}
?>