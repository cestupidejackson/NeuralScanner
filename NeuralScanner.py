from configparser import ConfigParser
#config.ini file for path 
fileconf = 'config/config.ini'
config = ConfigParser()
config.read(fileconf)
url = config["URL"]
path = url["url"]

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog
import pytesseract
pytesseract.pytesseract.tesseract_cmd = path
import time as t

#Mainwindow 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("NeuralScanner")
        Dialog.resize(548, 285)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 321, 41)) #211
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_new_window) #connect method, openFileChooserWindow
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 401, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 120, 401, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 91, 16))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 160, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 187, 13))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.convert) #connect method, Launch Converter 
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 220, 491, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 250, 201, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NeuralScanner"))
        self.label.setText(_translate("Dialog", "NeuralScanner"))
        self.pushButton.setText(_translate("Dialog", "Suchen"))
        self.label_2.setText(_translate("Dialog", "Image"))
        self.label_3.setText(_translate("Dialog", "Name des PDF\'s"))
        self.label_5.setText(_translate("Dialog", "Umwandlung noch nicht gestartet"))
        self.pushButton_2.setText(_translate("Dialog", "Umwandeln"))
        self.label_4.setText(_translate("Dialog", "Copyright 2022, Varun Vivekanantharasa"))
    #secondWindowInitialisation 
    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.lineEdit.setText(self.w.fileName)    
    #KI PDF-convert 
    def convert(self):
        print("launching")
        self.label_5.setText("self.moin")
        t.sleep(0.5)
        nameimg = self.lineEdit.text()
        namepdf = self.lineEdit_2.text()
        pdf = pytesseract.image_to_pdf_or_hocr(f'{nameimg}', extension='pdf')
        with open(f'{namepdf}.pdf', 'w+b') as f:
            f.write(pdf)  
            self.label_5.setText("Done")   

#secondWindow 
class AnotherWindow(QWidget):
    #openFile
    def __init__(self):
        super().__init__()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Bild auswählen", "","Images (*.png);;Images (*.jpg)", options=options)        
    def strRet(self):
        return self.fileName    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
