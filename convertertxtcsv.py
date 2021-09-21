import sys
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
import itertools
import time
import smtplib
from email.message import EmailMessage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importbtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.browsefiles())
        self.importbtn.setGeometry(QtCore.QRect(610, 30, 91, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.importbtn.setFont(font)
        self.importbtn.setObjectName("importbtn")
        self.pathlbl = QtWidgets.QLineEdit(self.centralwidget)
        self.pathlbl.setGeometry(QtCore.QRect(20, 30, 581, 31))
        self.pathlbl.setObjectName("pathlbl")
        self.mail_lbl = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_lbl.setGeometry(QtCore.QRect(20, 80, 311, 31))
        self.mail_lbl.setObjectName("mail_lbl")
        self.sendbtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.sendmsg())
        self.sendbtn.setGeometry(QtCore.QRect(330, 80, 81, 31))
        self.sendbtn.setObjectName("sendbtn")
        self.convertbtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.convert())
        self.convertbtn.setGeometry(QtCore.QRect(610, 80, 91, 31))
        self.convertbtn.setObjectName("convertbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "txtTOcsv"))
        self.importbtn.setText(_translate("MainWindow", "Import .txt"))
        self.pathlbl.setPlaceholderText(_translate("MainWindow", "FILEPATH"))
        self.mail_lbl.setPlaceholderText(_translate("MainWindow", " Send your .csv to e-mail"))
        self.sendbtn.setText(_translate("MainWindow", "Send to e-mail"))
        self.convertbtn.setText(_translate("MainWindow", "Convert to .csv"))

    def browsefiles(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', filter='*.txt')
        try:
            self.pathlbl.setText(fname[0])
        except: 
            self.pathlbl.setText("Must be .txt file!")

    def convert(self):
        path = self.pathlbl.text()
        #documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
        try:
            with open(path, 'r') as txtfile:
                stripped = (line.strip() for line in txtfile)
                lines = (line for line in stripped if line)
                grouped = zip(*[lines] * 3)
                with open('converter.csv', 'w') as output:
                    writer = csv.writer(output)
                    writer.writerow(('Col1', 'Col2'))
                    writer.writerows(grouped)
        finally:
            self.pathlbl.setText("File saved!")


    def sendmsg(self):

        sender_email = "example@gmail.com"
        sender_password = pass
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)
        print("Login successful")
        mailadr = self.mail_lbl.text()
        email_body_info = ("Hello\n\nYour .csv file is in the attachments.\n\n\n\n\nRegards")
        server.sendmail(sender_email,mailadr,email_body_info)
        print("Message sent")
        self.pathlbl.setText("FILE SENT TO E-MAIL")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
