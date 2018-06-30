import sys
import time
import pyodbc
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit

class UndefError(Exception):
    pass

class DBHelper():
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Ansi Driver};SERVER=127.0.0.1;DATABASE=test;UID=root;PWD=test123!;charset=utf8')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER,name VARCHAR(50),gender INTEGER,branch INTEGER,year INTEGER,academic_year INTEGER,address VARCHAR(50),mobile VARCHAR(50))")
        self.c.execute("CREATE TABLE IF NOT EXISTS payments(reciept_no INTEGER,roll INTEGER,fee INTEGER,semester INTEGER,reciept_date VARCHAR(50))")
        self.data = []
        self.list = []

    def addStudent(self, roll, name, gender, branch, year, academic_year, address, mobile):
        try:
            self.c.execute("SELECT * from students WHERE roll=" + str(roll))
            recvdata = self.c.fetchone()
            if recvdata:
                raise Exception
            self.c.execute("INSERT INTO students (roll,name,gender,branch,year,academic_year,address,mobile) VALUES (%d,'%s',%d,%d,%d,%d,'%s','%s')" %
                           (roll, name, gender, branch, year, academic_year, address, mobile))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful',
                                    'Student is added successfully to the database.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')

    def searchStudent(self, roll):
        self.c.execute("SELECT * from students WHERE roll=" + str(roll))
        self.data = self.c.fetchone()
        if not self.data:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find any student with roll no '+str(roll))
            return None
        self.list = []
        for i in range(0, 8):
            self.list.append(self.data[i])
        self.c.close()
        self.conn.close()
        showStudent(self.list)

    def addPayment(self, roll, fee, semester):
        reciept_no = int(time.time())
        date = time.strftime("%b %d %Y %H:%M:%S")
        try:
            self.c.execute("SELECT * from students WHERE roll=" + str(roll))
            self.data = self.c.fetchone()
            if not self.data:
                raise UndefError
            self.c.execute("SELECT * from payments WHERE roll=" + str(roll))
            self.conn.commit()
            if not self.c.fetchone():
                if semester == 1:
                    self.c.execute("SELECT * from payments WHERE roll=" + str(roll) + " AND semester=0")
                    if not self.c.fetchone():
                        QMessageBox.warning(QMessageBox(), 'Error',
                                            'Student with roll no ' + str(roll) +
                                            ' has Odd Semester fee payment due.Pay that first.')
                        return None
                else:
                    self.c.execute("INSERT INTO payments (reciept_no,roll,fee,semester,reciept_date) VALUES (%d,%d,%d,%d,'%s')" %
                                   (reciept_no, roll, fee, semester, date))
                    self.conn.commit()
                QMessageBox.information(QMessageBox(), 'Successful',
                                        'Payment is added successfully to the database.\nReference ID=' +
                                        str(reciept_no))
            else:
                self.c.execute("SELECT * from payments WHERE roll=" + str(roll))
                self.data = self.c.fetchall()
                if len(self.data) == 2:
                    QMessageBox.warning(QMessageBox(), 'Error',
                                        'Student with roll no ' + str(roll) +
                                        ' has already paid both semester fees.')
                elif semester == 1:
                    self.c.execute("SELECT * from payments WHERE roll=" + str(roll)+" AND semester=0")
                    if not self.c.fetchone():
                        QMessageBox.warning(QMessageBox(), 'Error',
                                            'Student with roll no ' + str(roll) + ' has Odd Semester fee payment due.Pay that first.')
                    else:
                        self.c.execute("INSERT INTO payments (reciept_no,roll,fee,semester,reciept_date) VALUES (%d,%d,%d,%d,'%s')" %
                                       (reciept_no, roll, fee, semester, date))
                        self.conn.commit()
                        QMessageBox.information(QMessageBox(), 'Successful',
                                                'Payment is added successfully to the database.\nReference ID=' + str(

                                                    reciept_no))
                elif self.data[0][3] == semester:
                    QMessageBox.warning(QMessageBox(), 'Error',
                                        'Student with roll no ' + str(roll) +
                                        ' has already paid this semester fees.')
                else:
                    self.c.execute("INSERT INTO payments (reciept_no,roll,fee,semester,reciept_date) VALUES (%d,%d,%d,%d,'%s')" %
                                   (reciept_no, roll, fee, semester, date))
                    self.conn.commit()
                    QMessageBox.information(QMessageBox(), 'Successful',
                                            'Payment is added successfully to the database.\nReference ID=' +
                                            str(reciept_no))
        except UndefError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find any student with roll no '+str(roll))
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add payment to the database.')
        self.c.close()
        self.conn.close()

    def searchPayment(self, roll):
        self.c.execute("SELECT * from payments WHERE roll="+str(roll)+" ORDER BY reciept_no DESC")
        self.data = self.c.fetchone()
        if not self.data:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find any student with roll no '+str(roll))
            return None
        self.list = self.data
        self.c.close()
        self.conn.close()
        showPaymentFunction(self.list)


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.userNameLabel = QLabel("Username")
        self.userPassLabel = QLabel("Password")
        self.textName = QLineEdit(self)
        self.textPass = QLineEdit(self)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QGridLayout(self)
        layout.addWidget(self.userNameLabel, 1, 1)
        layout.addWidget(self.userPassLabel, 2, 1)
        layout.addWidget(self.textName, 1, 2)
        layout.addWidget(self.textPass, 2, 2)
        layout.addWidget(self.buttonLogin, 3, 1, 1, 2)
        self.setWindowTitle("Login")

    def handleLogin(self):
        if self.textName.text() == 'admin' and self.textPass.text() == 'admin':
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong username or password')


def showStudent(alist):
    roll = 0
    gender = ""
    branch = ""
    year = ""
    name = ""
    address = ""
    mobile = -1
    academic_year = -1
    roll = alist[0]
    name = alist[1]
    if alist[2] == 0:
        gender = "男"
    else:
        gender = "女"
    if alist[3] == 0:
        branch = "计算机软件"
    elif alist[3] == 1:
        branch = "计算机科学与技术"
    elif alist[3] == 2:
        branch = "信息安全"
    elif alist[3] == 3:
        branch = "软件工程"
    elif alist[3] == 4:
        branch = "物联网工程"
    if alist[4] == 0:
        year = "大一"
    elif alist[4] == 1:
        year = "大二"
    elif alist[4] == 2:
        year = "大三"
    elif alist[4] == 3:
        year = "大四"
    academic_year = alist[5]
    address = alist[6]
    mobile = alist[7]
    table = QTableWidget()
    QTableWidgetItem()
    table.setWindowTitle("Student Details")
    table.setRowCount(8)
    table.setColumnCount(2)
    table.setItem(0, 0, QTableWidgetItem("编号"))
    table.setItem(0, 1, QTableWidgetItem(str(roll)))
    table.setItem(1, 0, QTableWidgetItem("姓名"))
    table.setItem(1, 1, QTableWidgetItem(str(name)))
    table.setItem(2, 0, QTableWidgetItem("性别"))
    table.setItem(2, 1, QTableWidgetItem(str(gender)))
    table.setItem(3, 0, QTableWidgetItem("专业"))
    table.setItem(3, 1, QTableWidgetItem(str(branch)))
    table.setItem(4, 0, QTableWidgetItem("年级"))
    table.setItem(4, 1, QTableWidgetItem(str(year)))
    table.setItem(5, 0, QTableWidgetItem("学年制"))
    table.setItem(5, 1, QTableWidgetItem(str(academic_year)))
    table.setItem(6, 0, QTableWidgetItem("地址"))
    table.setItem(6, 1, QTableWidgetItem(str(address)))
    table.setItem(7, 0, QTableWidgetItem("手机"))
    table.setItem(7, 1, QTableWidgetItem(str(mobile)))
    table.horizontalHeader().setStretchLastSection(True)
    table.show()
    dialog = QDialog()
    dialog.setWindowTitle("Student Details")
    dialog.resize(500, 300)
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(table)
    dialog.exec()

def showPaymentFunction(alist):
    roll = -1
    recipt_no = -1
    fee = -1
    semester = -1
    recipt_date = ""
    recipt_no = alist[0]
    roll = alist[1]
    fee = alist[2]
    if alist[3] == 0:
        semester = "一学期"
    elif alist[3] == 1:
        semester = "一学年"
    recipt_date = alist[4]
    table = QTableWidget()
    QTableWidgetItem()
    table.setWindowTitle("Student Payment Details")
    table.setRowCount(5)
    table.setColumnCount(2)
    table.setItem(0, 0, QTableWidgetItem("Receipt No"))
    table.setItem(0, 1, QTableWidgetItem(str(recipt_no)))
    table.setItem(1, 0, QTableWidgetItem("Roll"))
    table.setItem(1, 1, QTableWidgetItem(str(roll)))
    table.setItem(2, 0, QTableWidgetItem("Total Fee"))
    table.setItem(2, 1, QTableWidgetItem(str(fee)))
    table.setItem(3, 0, QTableWidgetItem("Semester"))
    table.setItem(3, 1, QTableWidgetItem(str(semester)))
    table.setItem(4, 0, QTableWidgetItem("Receipt Date"))
    table.setItem(4, 1, QTableWidgetItem(str(recipt_date)))
    table.horizontalHeader().setStretchLastSection(True)
    table.show()
    dialog = QDialog()
    dialog.setWindowTitle("Student Payment Details Details")
    dialog.resize(500, 300)
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(table)
    dialog.exec()


class AddStudent(QDialog):
    def __init__(self):
        super().__init__()
        self.gender = -1
        self.branch = -1
        self.year = -1
        self.roll = -1
        self.name = ""
        self.address = ""
        self.mobile = ""
        self.academic_year = -1
        self.btnReset = QPushButton("清空", self)
        self.btnAdd = QPushButton("添加", self)
        self.btnReset.setFixedHeight(30)
        self.btnAdd.setFixedHeight(30)
        self.yearCombo = QComboBox(self)
        self.yearCombo.addItem("大一")
        self.yearCombo.addItem("大二")
        self.yearCombo.addItem("大三")
        self.yearCombo.addItem("大四")
        self.genderCombo = QComboBox(self)
        self.genderCombo.addItem("男")
        self.genderCombo.addItem("女")
        self.branchCombo = QComboBox(self)
        self.branchCombo.addItem("计算机软件")
        self.branchCombo.addItem("计算机科学与技术")
        self.branchCombo.addItem("信息安全")
        self.branchCombo.addItem("软件工程")
        self.branchCombo.addItem("物联网工程")
        self.rollLabel = QLabel("编号")
        self.nameLabel = QLabel("姓名")
        self.addressLabel = QLabel("地址")
        self.mobLabel = QLabel("手机")
        self.yearLabel = QLabel("年级")
        self.academicYearLabel = QLabel("学年制")
        self.branchLabel = QLabel("专业")
        self.genderLabel = QLabel("性别")
        self.rollText = QLineEdit(self)
        self.nameText = QLineEdit(self)
        self.addressText = QLineEdit(self)
        self.mobText = QLineEdit(self)
        self.academicYearText = QLineEdit(self)
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.rollLabel, 1, 1)
        self.grid.addWidget(self.nameLabel, 2, 1)
        self.grid.addWidget(self.genderLabel, 3, 1)
        self.grid.addWidget(self.addressLabel, 4, 1)
        self.grid.addWidget(self.mobLabel, 5, 1)
        self.grid.addWidget(self.branchLabel, 6, 1)
        self.grid.addWidget(self.yearLabel, 7, 1)
        self.grid.addWidget(self.academicYearLabel, 8, 1)
        self.grid.addWidget(self.rollText, 1, 2)
        self.grid.addWidget(self.nameText, 2, 2)
        self.grid.addWidget(self.genderCombo, 3, 2)
        self.grid.addWidget(self.addressText, 4, 2)
        self.grid.addWidget(self.mobText, 5, 2)
        self.grid.addWidget(self.branchCombo, 6, 2)
        self.grid.addWidget(self.yearCombo, 7, 2)
        self.grid.addWidget(self.academicYearText, 8, 2)
        self.grid.addWidget(self.btnReset, 9, 1)
        self.grid.addWidget(self.btnAdd, 9, 2)
        self.btnAdd.clicked.connect(self.addStudent)
        self.btnReset.clicked.connect(self.reset)
        self.setLayout(self.grid)
        self.setWindowTitle("Add Student Details")
        self.resize(500, 300)
        self.show()
        self.exec()

    def reset(self):
        self.rollText.setText("")
        self.academicYearText.setText("")
        self.nameText.setText("")
        self.addressText.setText("")
        self.mobText.setText("")

    def addStudent(self):
        self.gender = self.genderCombo.currentIndex()
        self.year = self.yearCombo.currentIndex()
        self.branch = self.branchCombo.currentIndex()
        self.roll = int(self.rollText.text())
        self.name = self.nameText.text()
        self.academic_year = int(self.academicYearText.text())
        self.address = self.addressText.text()
        self.mobile = self.mobText.text()
        dbhelper = DBHelper()
        dbhelper.addStudent(self.roll, self.name, self.gender, self.branch,
                            self.year, self.academic_year, self.address, self.mobile)


class AddPayment(QDialog):
    def __init__(self):
        super().__init__()
        self.reciept_no = -1
        self.roll = -1
        self.fee = -1
        self.semester = -1
        self.date = -1
        self.btnReset = QPushButton("Reset", self)
        self.btnAdd = QPushButton("Add", self)
        self.btnReset.setFixedHeight(30)
        self.btnAdd.setFixedHeight(30)
        self.semesterCombo = QComboBox(self)
        self.semesterCombo.addItem("一学期")
        self.semesterCombo.addItem("一学年")
        self.rollLabel = QLabel("Roll No")
        self.feeLabel = QLabel("Total Fee")
        self.semesterLabel = QLabel("Semester")
        self.rollText = QLineEdit(self)
        self.feeLabelText = QLineEdit(self)
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.rollLabel, 1, 1)
        self.grid.addWidget(self.feeLabel, 2, 1)
        self.grid.addWidget(self.semesterLabel, 3, 1)
        self.grid.addWidget(self.rollText, 1, 2)
        self.grid.addWidget(self.feeLabelText, 2, 2)
        self.grid.addWidget(self.semesterCombo, 3, 2)
        self.grid.addWidget(self.btnReset, 4, 1)
        self.grid.addWidget(self.btnAdd, 4, 2)
        self.btnAdd.clicked.connect(self.addPayment)
        self.btnReset.clicked.connect(self.reset)
        self.setLayout(self.grid)
        self.setWindowTitle("Add Payment Details")
        self.resize(400, 200)
        self.show()
        self.exec()
    def reset(self):
        self.rollText.setText("")
        self.feeLabelText.setText("")

    def addPayment(self):
        self.semester = self.semesterCombo.currentIndex()
        self.roll = int(self.rollText.text())
        self.fee = int(self.feeLabelText.text())
        dbhelper = DBHelper()
        dbhelper.addPayment(self.roll, self.fee, self.semester)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rollToBeSearched = 0
        self.vbox = QVBoxLayout()
        self.text = QLabel("Enter the roll no of the student")
        self.editField = QLineEdit()
        self.btnSearch = QPushButton("Search", self)
        self.btnSearch.clicked.connect(self.showStudent)
        self.vbox.addWidget(self.text)
        self.vbox.addWidget(self.editField)
        self.vbox.addWidget(self.btnSearch)
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Enter Roll No")
        self.dialog.setLayout(self.vbox)

        self.rollForPayment = 0
        self.vboxPayment = QVBoxLayout()
        self.textPayment = QLabel("Enter the roll no of the student")
        self.editFieldPayment = QLineEdit()
        self.btnSearchPayment = QPushButton("Search", self)
        self.btnSearchPayment.clicked.connect(self.showStudentPayment)
        self.vboxPayment.addWidget(self.textPayment)
        self.vboxPayment.addWidget(self.editFieldPayment)
        self.vboxPayment.addWidget(self.btnSearchPayment)
        self.dialogPayment = QDialog()
        self.dialogPayment.setWindowTitle("Enter Roll No")
        self.dialogPayment.setLayout(self.vboxPayment)
        self.btnEnterStudent = QPushButton("Enter Student Details", self)
        self.btnEnterPayment = QPushButton("Enter Payment Details", self)
        self.btnShowStudentDetails = QPushButton("Show Student Details", self)
        self.btnShowPaymentDetails = QPushButton("Show Payment Details", self)

        #picture
        self.picLabel = QLabel(self)
        self.picLabel.resize(150, 150)
        self.picLabel.move(120, 20)
        self.picLabel.setScaledContents(True)
        self.picLabel.setPixmap(QtGui.QPixmap("user.png"))

        self.btnEnterStudent.move(15, 170)
        self.btnEnterStudent.resize(180, 40)
        self.btnEnterStudentFont = self.btnEnterStudent.font()
        self.btnEnterStudentFont.setPointSize(13)
        self.btnEnterStudent.setFont(self.btnEnterStudentFont)
        self.btnEnterStudent.clicked.connect(self.enterstudent)

        self.btnEnterPayment.move(205, 170)
        self.btnEnterPayment.resize(180, 40)
        self.btnEnterPaymentFont = self.btnEnterStudent.font()
        self.btnEnterPaymentFont.setPointSize(13)
        self.btnEnterPayment.setFont(self.btnEnterPaymentFont)
        self.btnEnterPayment.clicked.connect(self.enterpayment)

        self.btnShowStudentDetails.move(15, 220)
        self.btnShowStudentDetails.resize(180, 40)
        self.btnShowStudentDetailsFont = self.btnEnterStudent.font()
        self.btnShowStudentDetailsFont.setPointSize(13)
        self.btnShowStudentDetails.setFont(self.btnShowStudentDetailsFont)
        self.btnShowStudentDetails.clicked.connect(self.showStudentDialog)

        self.btnShowPaymentDetails.move(205, 220)
        self.btnShowPaymentDetails.resize(180, 40)
        self.btnShowPaymentDetailsFont = self.btnEnterStudent.font()
        self.btnShowPaymentDetailsFont.setPointSize(13)
        self.btnShowPaymentDetails.setFont(self.btnShowPaymentDetailsFont)
        self.btnShowPaymentDetails.clicked.connect(self.showStudentPaymentDialog)

        self.resize(400, 280)
        self.setWindowTitle("Student Database Management System")

    def enterstudent(self):
        AddStudent()
    def enterpayment(self):
        AddPayment()
    def showStudentDialog(self):
        self.dialog.exec()
    def showStudentPaymentDialog(self):
        self.dialogPayment.exec()
    def showStudent(self):
        if self.editField.text() is "":
            QMessageBox.warning(QMessageBox(), 'Error',
                                'You must give the roll number to show the results for.')
            return None
        showstudent = DBHelper()
        showstudent.searchStudent(int(self.editField.text()))
    def showStudentPayment(self):
        if self.editFieldPayment.text() is "":
            QMessageBox.warning(QMessageBox(), 'Error',
                                'You must give the roll number to show the results for.')
            return None
        showstudent = DBHelper()
        showstudent.searchPayment(int(self.editFieldPayment.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = Window()
        window.show()
    sys.exit(app.exec_())
