<?php
include 'config.php';
$id = $_REQUEST['id'];
$result = $db->query("select * from student WHERE student_number='$id';");
if(!$result) {
    echo "<script>alert(\"数据库错误\");
                location.href=\"index.html\";</script>";
    return;
}
else{
    $item = $result->fetch();
}
?>
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>学生主页</title>
    <link href="css/foundation.min.css" rel="stylesheet"/>
    <link href="css/custom.css" rel="stylesheet" />
</head>
<body>
<nav class="top-bar" data-topbar role="navigation">
    <ul class="title-area">
        <li class="name">
            <h1><a href="index.html">主页</a></h1>
        </li>
    </ul>
</nav>
<header>
    <div class="row">
        <div class="large-12 columns">
            <h2>学生主页</h2>
            <h4>可重新填写姓名，密码等进行更新操作</h4>
        </div>
    </div>
</header>
<div class="row">
    <form class="large-4 large-offset-4" action="update_stu.php" method="post" enctype="multipart/form-data">
        <label>姓名</label>
        <input type="text" name="name" value="<?php echo $item['name'];?>" required />
        <label>密码</label>
        <input type="password" name="password" value="<?php echo $item['password'];?>" required />
        <label>确认密码</label>
        <input type="password" name="confirm_pwd" value="<?php echo $item['password'];?>" required />
        <label>班级</label>
        <input type="text" name="class" value="<?php echo $item['class'];?>" required />
        <label>学号</label>
        <input type="text" name="std_number" value="<?php echo $item['student_number'];?>" readonly />
        <label>性别</label>
        <input type="text" name="sex" value="<?php echo $item['sex']?>" readonly />
        <label>爱好</label>
        <?php
            $hobby = explode(',', $item['hobby']);
        ?>
        <input id="coding" type="checkbox" name="internet[]" <?php if(in_array("编程", $hobby)){echo "checked";}?>/>
        <label for="coding">编程</label>
        <input id="sports" type="checkbox" name="internet[]" <?php if(in_array("运动", $hobby)){echo "checked";}?>/>
        <label for="sports">运动</label><br>
        <input id="trip" type="checkbox" name="internet[]" <?php if(in_array("旅游", $hobby)){echo "checked";}?>/>
        <label for="trip">旅游</label>
        <input id="sleep" type="checkbox" name="internet[]" <?php if(in_array("睡觉", $hobby)){echo "checked";}?>/>
        <label for="sleep">睡觉</label><br>
        <input id="shopping" type="checkbox" name="internet[]" <?php if(in_array("购物", $hobby)){echo "checked";}?>/>
        <label for="shopping">购物</label>
        <input id="other" type="checkbox" name="internet[]" <?php if(in_array("其他", $hobby)){echo "checked";}?>/>
        <label for="other">其他</label><br>
        <label>头像</label>
        <img class="th" src="<?php echo $item['avatar'];?>" /><br><br>
        <label>上传</label>
        <input type="file" name="file">
        <br>
        <label>成绩</label>
        <input type="number" name="grades" min="0" max="100" value="<?php echo $item['grade'];?>" readonly required="required">
        <label>备注</label>
        <textarea name="remark"><?php echo $item['remark'];?></textarea>
        <br>
        <br>
        <input class="small radius button left" type="submit" value="更新">
    </form>
</div>

</body>
</html>