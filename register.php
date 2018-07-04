<?php
include 'config.php';
// 表单其他的处理部分
$name = $_REQUEST["name"];
$password = $_REQUEST["password"];
$re_password = $_REQUEST["confirm_pwd"];
$class = $_REQUEST["class"];
$student_number = $_REQUEST["std_number"];
$sex = $_REQUEST["sex"];
$avatar = "";
$hobby = "";

if(isset($_REQUEST['internet'])){
    $checkbox = $_REQUEST['internet'];
    if(count($checkbox)==0)
        $hobby = "";
    else
        $hobby = implode(",",$checkbox);
}
# check class
$pattern1 = '/^\d{7}$/';
if(!preg_match($pattern1, $class)) {
    echo "<script>alert(\"班级格式错误\");location.href=\"register.html\"</script>";
    return;
}

# check student number
$pattern2 = '/^(SZ|SX|BX)\d{7}$|^\d{9}$/';
if(!preg_match($pattern2, $student_number)) {
    echo "<script>alert(\"学号格式错误\");location.href=\"register.html\"</script>";
    return;
}

# grade
if(isset($_REQUEST["grades"]))
    $grade = $_REQUEST["grades"];
else
    $grade = 0;

if(isset($_REQUEST["remark"]))
    $remark = $_REQUEST["remark"];
else
    $remark = "";

# handle password
if($password != $re_password){
    echo "<script>alert(\"两次输入的密码不一致\");location.href=\"register.html\"</script>";
    return;
}
# 文件处理发生错误
$avatar = handleFile($student_number);
if(!$avatar){
    echo "<script>;location.href=\"register.html\"</script>";
    return;
}

$insert = "insert into student VALUES ( '$name', '$password', '$class', '$student_number', '$sex',
 '$hobby', $grade, '$remark', '$avatar');";
$query = "select * from student WHERE student_number = '$student_number'";

# check if db has this one
$result = $db->query($query);
if(!$result){
    echo "<script>alert(\"数据库错误\");location.href=\"register.html\"</script>";
}else{
    $item = $result->fetch();
    if(!$item){
        # 如果数据库中没有这个学号，插入
        echo $insert;
        $result = $db->exec($insert);
        if(!$result){
            echo "<script>alert(\"数据库错误\");location.href=\"register.html\"</script>";
        }else{
            echo "<script>alert(\"注册成功\");location.href=\"index.html\";</script>";
        }
    }else{
        # 数据库中有这个学号，爆出错误
        echo "<script>alert(\"该学生已经存在了\");location.href=\"register.html\"</script>";
    }
}

function handleFile($student_number){
    # handle the file
    echo $_FILES["file"]["type"];
    if (($_FILES["file"]["type"] == "image/jpeg")
        && ($_FILES["file"]["size"] < 1024000))
    {
        if ($_FILES["file"]["error"] > 0)
        {
            echo "Error: " . $_FILES["file"]["error"] . "<br />";
            echo "<script>alert(\"头像错误\")</script>";
            return false;
        }
        else
        {
            echo "Upload: " . $_FILES["file"]["name"] . "<br />";
            echo "Type: " . $_FILES["file"]["type"] . "<br />";
            echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
            echo "Stored in: " . $_FILES["file"]["tmp_name"];

            # store the image
            if (file_exists("upload/" . $student_number.".jpg"))
            {
                move_uploaded_file($_FILES["file"]["tmp_name"],
                    "upload/" . $student_number.".jpg");
                $avatar = "upload/" . $student_number.".jpg";
                return $avatar;
            }
            else
            {
                move_uploaded_file($_FILES["file"]["tmp_name"],
                    "upload/" . $student_number.".jpg");
                $avatar = "upload/" . $student_number.".jpg";
                return $avatar;
            }
        }

    }
    else
    {
        $avatar = "upload/default.jpg";
        return $avatar;
    }
}
?>