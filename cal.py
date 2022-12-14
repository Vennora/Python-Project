# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
        
class Ui_MainWindow(object): 
      
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget") 
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 10, 421, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.bth_zero = QtWidgets.QPushButton(self.centralwidget)
        self.bth_zero.setGeometry(QtCore.QRect(0, 320, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_zero.setFont(font)
        self.bth_zero.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_zero.setObjectName("bth_zero")
        self.bth_equal = QtWidgets.QPushButton(self.centralwidget)
        self.bth_equal.setGeometry(QtCore.QRect(150, 320, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_equal.setFont(font)
        self.bth_equal.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.bth_equal.setObjectName("bth_equal")
        self.bth_one = QtWidgets.QPushButton(self.centralwidget)
        self.bth_one.setGeometry(QtCore.QRect(0, 240, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_one.setFont(font)
        self.bth_one.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_one.setObjectName("bth_one")
        self.bth_two = QtWidgets.QPushButton(self.centralwidget)
        self.bth_two.setGeometry(QtCore.QRect(80, 240, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_two.setFont(font)
        self.bth_two.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_two.setObjectName("bth_two")
        self.bth_three = QtWidgets.QPushButton(self.centralwidget)
        self.bth_three.setGeometry(QtCore.QRect(160, 240, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_three.setFont(font)
        self.bth_three.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_three.setObjectName("bth_three")
        self.bth_four = QtWidgets.QPushButton(self.centralwidget)
        self.bth_four.setGeometry(QtCore.QRect(0, 160, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_four.setFont(font)
        self.bth_four.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_four.setObjectName("bth_four")
        self.bth_six = QtWidgets.QPushButton(self.centralwidget)
        self.bth_six.setGeometry(QtCore.QRect(160, 160, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_six.setFont(font)
        self.bth_six.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_six.setObjectName("bth_six")
        self.bth_fifth = QtWidgets.QPushButton(self.centralwidget)
        self.bth_fifth.setGeometry(QtCore.QRect(80, 160, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_fifth.setFont(font)
        self.bth_fifth.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_fifth.setObjectName("bth_fifth")
        self.bth_seven = QtWidgets.QPushButton(self.centralwidget)
        self.bth_seven.setGeometry(QtCore.QRect(0, 80, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_seven.setFont(font)
        self.bth_seven.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_seven.setObjectName("bth_seven")
        self.bth_nine = QtWidgets.QPushButton(self.centralwidget)
        self.bth_nine.setGeometry(QtCore.QRect(160, 80, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_nine.setFont(font)
        self.bth_nine.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_nine.setObjectName("bth_nine")
        self.bth_eight = QtWidgets.QPushButton(self.centralwidget)
        self.bth_eight.setGeometry(QtCore.QRect(80, 80, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_eight.setFont(font)
        self.bth_eight.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.bth_eight.setObjectName("bth_eight")
        self.bth_minus = QtWidgets.QPushButton(self.centralwidget)
        self.bth_minus.setGeometry(QtCore.QRect(300, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_minus.setFont(font)
        self.bth_minus.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.bth_minus.setObjectName("bth_minus")
        self.bth_plus = QtWidgets.QPushButton(self.centralwidget)
        self.bth_plus.setGeometry(QtCore.QRect(240, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_plus.setFont(font)
        self.bth_plus.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.bth_plus.setObjectName("bth_plus")
        self.bth_delit = QtWidgets.QPushButton(self.centralwidget)
        self.bth_delit.setGeometry(QtCore.QRect(240, 200, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_delit.setFont(font)
        self.bth_delit.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.bth_delit.setObjectName("bth_delit")
        self.bth_umnoj = QtWidgets.QPushButton(self.centralwidget)
        self.bth_umnoj.setGeometry(QtCore.QRect(240, 260, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_umnoj.setFont(font)
        self.bth_umnoj.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.bth_umnoj.setObjectName("bth_umnoj")
        self.bth_procent = QtWidgets.QPushButton(self.centralwidget)
        self.bth_procent.setGeometry(QtCore.QRect(300, 200, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_procent.setFont(font)
        self.bth_procent.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.bth_procent.setObjectName("bth_procent")
        self.bth_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.bth_cancel.setGeometry(QtCore.QRect(300, 260, 61, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_cancel.setFont(font)
        self.bth_cancel.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.bth_cancel.setObjectName("bth_cancel")
        self.bth_sin = QtWidgets.QPushButton(self.centralwidget)
        self.bth_sin.setGeometry(QtCore.QRect(240, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_sin.setFont(font)
        self.bth_sin.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"")
        self.bth_sin.setObjectName("bth_sin")
        self.bth_cos = QtWidgets.QPushButton(self.centralwidget)
        self.bth_cos.setGeometry(QtCore.QRect(300, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_cos.setFont(font)
        self.bth_cos.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"")
        self.bth_cos.setObjectName("bth_cos")
        self.bth_tag = QtWidgets.QPushButton(self.centralwidget)
        self.bth_tag.setGeometry(QtCore.QRect(360, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_tag.setFont(font)
        self.bth_tag.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"")
        self.bth_tag.setObjectName("bth_tag")
        self.bth_ctg = QtWidgets.QPushButton(self.centralwidget)
        self.bth_ctg.setGeometry(QtCore.QRect(360, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_ctg.setFont(font)
        self.bth_ctg.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"")
        self.bth_ctg.setObjectName("bth_ctg")
        self.bth_skob_one = QtWidgets.QPushButton(self.centralwidget)
        self.bth_skob_one.setGeometry(QtCore.QRect(360, 200, 60, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_skob_one.setFont(font)
        self.bth_skob_one.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.bth_skob_one.setObjectName("bth_skob_one")
        self.bth_skob_two = QtWidgets.QPushButton(self.centralwidget)
        self.bth_skob_two.setGeometry(QtCore.QRect(360, 300, 60, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bth_skob_two.setFont(font)
        self.bth_skob_two.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.bth_skob_two.setObjectName("bth_skob_two")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.addFunctions()
        
    def addFunctions(self):
        
        self.bth_zero.clicked.connect(lambda: self.writeNumber(self.bth_zero.text()))
        self.bth_one.clicked.connect(lambda: self.writeNumber(self.bth_one.text()))
        self.bth_two.clicked.connect(lambda: self.writeNumber(self.bth_two.text()))
        self.bth_three.clicked.connect(lambda: self.writeNumber(self.bth_three.text()))
        self.bth_four.clicked.connect(lambda: self.writeNumber(self.bth_four.text()))
        self.bth_fifth.clicked.connect(lambda: self.writeNumber(self.bth_fifth.text()))
        self.bth_six.clicked.connect(lambda: self.writeNumber(self.bth_six.text()))
        self.bth_seven.clicked.connect(lambda: self.writeNumber(self.bth_seven.text()))
        self.bth_eight.clicked.connect(lambda: self.writeNumber(self.bth_eight.text()))
        self.bth_nine.clicked.connect(lambda: self.writeNumber(self.bth_nine.text()))

        self.bth_plus.clicked.connect(lambda: self.writeNumber(self.bth_plus.text()))
        self.bth_minus.clicked.connect(lambda: self.writeNumber(self.bth_minus.text()))
        self.bth_delit.clicked.connect(lambda: self.writeNumber(self.bth_delit.text()))
        self.bth_umnoj.clicked.connect(lambda: self.writeNumber(self.bth_umnoj.text())) 
        self.bth_procent.clicked.connect(lambda: self.writeNumber(self.bth_procent.text()))

        self.bth_cancel.clicked.connect(lambda: self.actionClear())
       
        self.bth_sin.clicked.connect(lambda: self.writeNumber(self.bth_sin.text()))
        self.bth_cos.clicked.connect(lambda: self.writeNumber(self.bth_cos.text()))
        self.bth_tag.clicked.connect(lambda: self.writeNumber(self.bth_tag.text()))
        self.bth_ctg.clicked.connect(lambda: self.writeNumber(self.bth_ctg.text()))
        self.bth_skob_one.clicked.connect(lambda: self.writeNumber(self.bth_skob_one.text()))
        self.bth_skob_two.clicked.connect(lambda: self.writeNumber(self.bth_skob_two.text()))       

        self.bth_equal.clicked.connect(self.results)
        
        error3 = QMessageBox()
        error3.setWindowTitle("????????????????????")
        error3.setText("?????????? ???????????????????? ???????? ??????????????????, ????????????????????,"
        " ?????????????? ?????????????????? ???????????????????????????????????? ??????????????, ?????????????????? ????????????."
        "\n?????????? ?????????????????? ctg(x), ???????????????????????????? ???????????????? 1/tan(x)")

        error3.setIcon(QMessageBox.Warning) 
        error3.setStandardButtons(QMessageBox.Ok) 

        error3.setDefaultButton(QMessageBox.Ok) 

        error3.exec_()         
        self.isEqual =  False
        
    def actionClear(self):
        self.label_result.setText("0")
        
    def writeNumber(self, number):
        if (self.label_result.text() == "0") or (self.isEqual): 
            self.label_result.setText(number)
            self.isEqual = False        
        else:
            self.label_result.setText(self.label_result.text() + number)
    
    def results(self):
        if not self.isEqual: 
            
            try:
                res = eval(self.label_result.text())    
                self.label_result.setText(str(res))
                
            except ZeroDivisionError: 
                error1 = QMessageBox()
                error1.setWindowTitle("????????????")
                error1.setText("???? 0 ???????????? ????????????!")
    
                error1.setIcon(QMessageBox.Warning) 
                error1.setStandardButtons(QMessageBox.Reset | QMessageBox.Cancel | QMessageBox.Ok) 
    
                error1.setDefaultButton(QMessageBox.Ok) 
    
                error1.buttonClicked.connect(self.popupAction)
                error1.exec_()
     
            self.isEqual = True          
            
            if (self.label_result.text() == "666"):
                img = Image.open(r'C:\Users\79629\Desktop\????????????\666.jpg')
                img.show()
               
            if (self.label_result.text() == "777"):
                img2 = Image.open(r'C:\Users\79629\Desktop\????????????\777.jpg')
                img2.show()
               
            if (self.label_result.text() == "9"):
                img3 = Image.open(r'C:\Users\79629\Desktop\????????????\9.png')
                img3.show()                
                       
            if (self.label_result.text() == "73"):
                img4 = Image.open(r'C:\Users\79629\Desktop\????????????\73.jpg')
                img4.show()                
                
            if (self.label_result.text() == "23"):
                img5 = Image.open(r'C:\Users\79629\Desktop\????????????\23_23.jpg')
                img5.show()                 
 
            if (self.label_result.text() == "6174"):
                img6 = Image.open(r'C:\Users\79629\Desktop\????????????\6174.jpg')
                img6.show()                
                
            if (self.label_result.text() == "11"):
                img7 = Image.open(r'C:\Users\79629\Desktop\????????????\11.jpg')
                img6.show()                
                
            if (self.label_result.text() == "250"):
                img6 = Image.open(r'C:\Users\79629\Desktop\????????????\250.png')
                img6.show()                 
            
        else:
            error = QMessageBox()
            error.setWindowTitle("????????????")
            error.setText("???????????? ?????? ???????????????? ?????????????????? ????????????????????")

            error.setIcon(QMessageBox.Warning) 
            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Cancel | QMessageBox.Ok) 

            error.setDefaultButton(QMessageBox.Ok) 
            error.setInformativeText("?????? ???????? ???????????????? ???? ??????????????????")
            error.setDetailedText("?????????????? ???????????? ?????? ????????????????????")

            error.buttonClicked.connect(self.popupAction)
            error.exec_()

    def popupAction(self, btn):
        if btn.text() == "Ok":
            print("Print ok")

        elif btn.text() == "Reset":
            self.label_result.setText("") 
            self.isEqual = False        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.bth_zero.setText(_translate("MainWindow", "0"))
        self.bth_equal.setText(_translate("MainWindow", "="))
        self.bth_one.setText(_translate("MainWindow", "1"))
        self.bth_two.setText(_translate("MainWindow", "2"))
        self.bth_three.setText(_translate("MainWindow", "3"))
        self.bth_four.setText(_translate("MainWindow", "4"))
        self.bth_six.setText(_translate("MainWindow", "6"))
        self.bth_fifth.setText(_translate("MainWindow", "5"))
        self.bth_seven.setText(_translate("MainWindow", "7"))
        self.bth_nine.setText(_translate("MainWindow", "9"))
        self.bth_eight.setText(_translate("MainWindow", "8"))
        self.bth_minus.setText(_translate("MainWindow", "-"))
        self.bth_plus.setText(_translate("MainWindow", "+"))
        self.bth_delit.setText(_translate("MainWindow", "/"))
        self.bth_umnoj.setText(_translate("MainWindow", "*"))
        self.bth_procent.setText(_translate("MainWindow", "%"))
        self.bth_cancel.setText(_translate("MainWindow", "??"))
        self.bth_sin.setText(_translate("MainWindow", "sin"))
        self.bth_cos.setText(_translate("MainWindow", "cos"))
        self.bth_tag.setText(_translate("MainWindow", "tan"))
        self.bth_ctg.setText(_translate("MainWindow", "ctg"))
        self.bth_skob_one.setText(_translate("MainWindow", "("))
        self.bth_skob_two.setText(_translate("MainWindow", ")"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
