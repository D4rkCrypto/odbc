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
    class int NOT NULL,
    student_number VARCHAR(9) PRIMARY KEY NOT NULL,
    sex TEXT NOT NULL,
    hobby TEXT NOT NULL,
    grade float NOT NULL,
    remark TEXT NOT NULL,
    avatar TEXT NOT NULL
);

BEGIN;
INSERT INTO `student` VALUES ('ldy', 'ldy', 1, '123710502', 'male', 'cs', 100.0, '好孩子', 'upload/1123710502.jpg');
INSERT INTO `student` VALUES ('ch', 'ch', 1, '123710518', 'male', 'trip', 90.0, '运动达人', 'upload/1123710518.jpg');
INSERT INTO `student` VALUES ('skyline', 'line', 1, '123710401', 'female', 'cs,economics,trip', 96.0, '女汉子', 'upload/1123710401.jpg');
INSERT INTO `student` VALUES ('sf', 'sf', 1, '123710402', 'male', 'cs,economics,trip', 60.0, '', 'upload/1123710402.jpg');
INSERT INTO `student` VALUES ('歪歪', 'test123', 1, '081510217', 'male', 'cs', 100.0, 'good', 'upload/081510217.jpg');
INSERT INTO `student` VALUES ('小歪歪', 'test', 1615001, '161520109', 'male', 'economics,sleep', 80.0, '测试', 'upload/161520109.jpg');
COMMIT;
