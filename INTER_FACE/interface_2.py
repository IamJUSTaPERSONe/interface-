from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import  sys


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("1login.ui", self)
        self.joun.clicked.connect(self.login_clicked)

        self.password.setEchoMode(QtWidgets.QLineEdit.Password) #Скрытие пароля 1
        self.cr_new_acc.clicked.connect(self.gonewacc)

    def login_clicked(self):
        login = self.login.text()
        password = self.password.text()
        print(login, password)

    def gonewacc(self):
        self.acc = CreateNewAcc()
        self.acc.show()

class CreateNewAcc(QDialog):
    def __init__(self):
        super(CreateNewAcc, self).__init__()
        uic.loadUi('2login.ui', self)
        self.joun2.clicked.connect(self.createacc_function)

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ret_urn.clicked.connect(self.returnMe)


    def createacc_function(self):
        login = self.login.text()
        if self.password.text() == self.password_2.text():
            password = self.password.text()
            print("Successful registration!!")
        else: print("Not correct.\nPlease try arain")

    def returnMe(self):
        self.ret=Login()
        self.ret.show()

app = QApplication(sys.argv)
win = Login()
win.setFixedWidth(600)
win.setFixedHeight(450)
win.show()
sys.exit(app.exec_())
