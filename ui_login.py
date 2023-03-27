from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import res_rc_login
import sys
import pymysql

connection = pymysql.connect(
     host = "localhost",
     user="root",
     password="feyzullah0348",
     database="dbshoppingordersystem"
)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 519)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 501))
        self.label.setStyleSheet("border-radius:10px;\n"
"background-image: url(:/images/tumblr_2309aa1f6ac3fe5e00aea2da0660d1f4_1f56ae57_640.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(45, 130, 231, 71))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 230, 211, 31))
        self.lineEdit.setStyleSheet("border-radius:5px;\n"
"background-color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"border-left: 2px solid rgba(255,255,255,255);\n"
"border-top: 2px solid rgba(255,255,255,255);\n"
"border-right: 2px solid rgba(255,255,255,255);\n"
"color:rgba(255,255,255,255);\n"
"text-align:center;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 270, 211, 31))
        self.lineEdit_2.setStyleSheet("border-radius:5px;\n"
"background-color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"border-left: 2px solid rgba(255,255,255,255);\n"
"border-top: 2px solid rgba(255,255,255,255);\n"
"border-right: 2px solid rgba(255,255,255,255);\n"
"color:rgba(255,255,255,255);\n"
"text-align:center;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 360, 101, 31))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"border-radius:10px;\n"
"color:white;\n"
"border:none;\n"
"border-left: 2px solid rgba(255,255,255,255);\n"
"border-right: 2px solid rgba(255,255,255,255);\n"
"border-top: 2px solid rgba(255,255,255,255);\n"
"border-bottom: 2px solid rgba(255,255,255,255);\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgb(20, 61, 61)\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"image: url(:/images/arrow-right.svg);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 360, 101, 31))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"border-radius:10px;\n"
"color:white;\n"
"border:none;\n"
"border-left: 2px solid rgba(255,255,255,255);\n"
"border-right: 2px solid rgba(255,255,255,255);\n"
"border-top: 2px solid rgba(255,255,255,255);\n"
"border-bottom: 2px solid rgba(255,255,255,255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"background-color:rgb(20, 61, 61)\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"image: url(:/images/arrow-right.svg);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 320, 201, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(33, 235, 21, 21))
        self.label_4.setStyleSheet("background-image: url(:/images/user.svg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(33, 275, 21, 21))
        self.label_5.setStyleSheet("background-image: url(:/images/key.svg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 30, 21, 21))
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton_3.setStyleSheet("background-color:rgb(172, 0, 0);\n"
"color:black;\n"
"border-radius:10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">L O G I N</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">_____________________</span></p></body></html>"))
        self.lineEdit.setText(_translate("Form", "E-Mail"))
        self.lineEdit_2.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "L O G I N"))
        self.pushButton_2.setText(_translate("Form", "R E G I S T E R"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;\">Forgot your e-mail or password?</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "X"))

    def exit(self):
         exit()
    
if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())