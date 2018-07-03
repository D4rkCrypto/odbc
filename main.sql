DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`
(
    user_name TEXT NOT NULL,
    password TEXT NOT NULL
);

BEGIN;
INSERT INTO `admin` VALUES ('root', 'root');
COMMIT;

DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`
(
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    class VARCHAR(7) NOT NULL,
    student_number VARCHAR(9) PRIMARY KEY NOT NULL,
    sex TEXT NOT NULL,
    hobby TEXT NOT NULL,
    grade float NOT NULL,
    remark TEXT NOT NULL,
    avatar TEXT NOT NULL
);

BEGIN;
INSERT INTO `student` VALUES ('小轩', 'xiaoxuan', '1234567', '123710502', 'male', '编程,购物', 100.0, '好孩子', 'upload/123710502.jpg');
INSERT INTO `student` VALUES ('学弟', 'xuedi', '1234567', '123710518', 'male', '旅游', 90.0, '运动达人', 'upload/123710518.jpg');
INSERT INTO `student` VALUES ('skyline', 'line', '1234567', '123710401', 'female', '编程,旅游,运动', 96.0, '女汉子', 'upload/123710401.jpg');
INSERT INTO `student` VALUES ('sf', 'sf', '1234567', '123710402', 'male', '运动,睡觉', 60.0, '', 'upload/123710402.jpg');
INSERT INTO `student` VALUES ('歪歪', 'test', '1615001', '081510217', 'male', '睡觉', 100.0, 'good', 'upload/081510217.jpg');
INSERT INTO `student` VALUES ('小歪歪', 'test', '1615001', '161520109', 'male', '', 80.0, '测试', 'upload/161520109.jpg');
COMMIT;
