

from PyQt5 import QtCore, QtGui, QtWidgets
from loginteacher import Ui_MainWindow
class Ui_Dialog(object):

    def teacher(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(575, 441)
        Dialog.setStyleSheet("color:forestgreen")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 281, 51))
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:blue")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.teacher)
        self.pushButton.setGeometry(QtCore.QRect(220, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 395, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Tabitha")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:bl")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 370, 541, 61))
        self.graphicsView.setObjectName("graphicsView")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 390, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Varsity")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ruet"))
        self.label.setText(_translate("Dialog", "Rajshahi University Of Engineering and Technology"))
        self.label_2.setText(_translate("Dialog", "Department of CSE"))
        self.pushButton.setText(_translate("Dialog", "Teacher Log-In"))
        self.pushButton_2.setText(_translate("Dialog", "Student Log-In"))
        self.label_4.setText(_translate("Dialog", "Developer: Ansarul(cse14) Tohid(cse14) Mezbah(cse14)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

