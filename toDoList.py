
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QListWidget,QPushButton,QListWidgetItem
from PyQt5.QtCore import Qt
import random
import res


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setObjectName("Form")
        Form.resize(1034, 652)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 25, 500, 391))
        self.label.setStyleSheet("background-image: url(:/images/b.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 130, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: rgba(0, 0, 10, 0.7);\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(50, 190, 481, 211))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("""QListWidget{background:rgba(0,0,10,0.7); border-style:none; color:white;}  QListWidget::item:selected{ outline:none;}  QListWidget::item:!selected{border-radius:5px;}""")
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(520, 60, 260, 330))
        self.label_2.setStyleSheet("background-color:rgb(0,0,15);\n"
"border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(600, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(255,255,255,255);")
        self.label_3.setObjectName("label_3")
        self.gorev_Ekle = QtWidgets.QPushButton(Form,clicked= lambda: self.gorevEkle())
        self.gorev_Ekle.setGeometry(QtCore.QRect(590, 120, 141, 35))
        self.gorev_Ekle.setStyleSheet("QPushButton#gorev_Ekle{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#gorev_Ekle:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#gorev_Ekle:hover{\n"
"background-color:rgba(255,107,107,255)\n"
"}")
        self.gorev_Ekle.setObjectName("gorev_Ekle")
        self.gorev_Sil = QtWidgets.QPushButton(Form,clicked = lambda :self.gorevSil())
        self.gorev_Sil.setGeometry(QtCore.QRect(590, 160, 141, 35))
        self.gorev_Sil.setStyleSheet("QPushButton#gorev_Sil{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#gorev_Sil:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#gorev_Sil:hover{\n"
"background-color:rgba(255,107,107,255)\n"
"}")
        self.gorev_Sil.setObjectName("gorev_Sil")
        self.tek_Gorev_sil = QtWidgets.QPushButton(Form,clicked = lambda :self.tekGorevSil())
        self.tek_Gorev_sil.setGeometry(QtCore.QRect(590, 200, 141, 35))
        self.tek_Gorev_sil.setStyleSheet("QPushButton#tek_Gorev_sil{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#tek_Gorev_sil:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#tek_Gorev_sil:hover{\n"
"background-color:rgba(255,107,107,255)\n"
"}")
        self.tek_Gorev_sil.setObjectName("tek_Gorev_sil")
        self.asc_Sirala = QtWidgets.QPushButton(Form,clicked = lambda :self.ascSirala())
        self.asc_Sirala.setGeometry(QtCore.QRect(590, 240, 141, 35))
        self.asc_Sirala.setStyleSheet("QPushButton#asc_Sirala{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#asc_Sirala:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#asc_Sirala:hover{\n"
"background-color:rgba(255,107,107,255)\n"
"}")
        self.asc_Sirala.setObjectName("asc_Sirala")
        self.desc_Sirala = QtWidgets.QPushButton(Form,clicked = lambda :self.descSirala())
        self.desc_Sirala.setGeometry(QtCore.QRect(590, 280, 141, 35))
        self.desc_Sirala.setStyleSheet("QPushButton#desc_Sirala{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#desc_Sirala:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#desc_Sirala:hover{\n"
"background-color:rgba(255,107,107,255)\n"
"}")
        self.desc_Sirala.setObjectName("desc_Sirala")
        self.rastgele_Sec = QtWidgets.QPushButton(Form,clicked = lambda :self.rastgeleSec())
        self.rastgele_Sec.setGeometry(QtCore.QRect(590, 320, 141, 35))
        self.rastgele_Sec.setStyleSheet("QPushButton#rastgele_Sec{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,255);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#rastgele_Sec:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#rastgele_Sec:hover{\n"
"background-color:rgba(255,107,107,255)\n"
"}")
        self.rastgele_Sec.setObjectName("rastgele_Sec")
        self.lbl_goster = QtWidgets.QLabel(Form)
        self.lbl_goster.setGeometry(QtCore.QRect(150, 60, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_goster.setFont(font)
        self.lbl_goster.setStyleSheet("border:none;")
        self.lbl_goster.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_goster.setText("")
        self.lbl_goster.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_goster.setObjectName("lbl_goster")
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.listWidget.raise_()
        self.label_3.raise_()
        self.gorev_Ekle.raise_()
        self.gorev_Sil.raise_()
        self.tek_Gorev_sil.raise_()
        self.asc_Sirala.raise_()
        self.desc_Sirala.raise_()
        self.rastgele_Sec.raise_()
        self.lbl_goster.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)






    def gorevEkle(self):
            if self.lineEdit.text() !="":
                    item = self.lineEdit.text()
                    self.listWidget.addItem(item)
                    self.lineEdit.setText("")
                    self.lbl_goster.setText("")
            else:
                    self.lbl_goster.setText("Lütfen bir görev giriniz.")

    def tekGorevSil(self):
            secili = self.listWidget.currentRow()
            self.listWidget.takeItem(secili)

    def gorevSil(self):
            self.listWidget.clear()

    def ascSirala(self):
            self.listWidget.setSortingEnabled(True)
            self.listWidget.sortItems(Qt.AscendingOrder)


    def descSirala(self):
            self.listWidget.setSortingEnabled(True)
            self.listWidget.sortItems(Qt.DescendingOrder)

    def rastgeleSec(self):
            index = random.randint(0,self.listWidget.count()-1)
            self.lbl_goster.setText("Seçilen görev: "+self.listWidget.item(index).text())







    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "TO-DO LIST"))
        self.gorev_Ekle.setText(_translate("Form", "Görev Ekle"))
        self.gorev_Sil.setText(_translate("Form", "Tüm Görevleri Sil"))
        self.tek_Gorev_sil.setText(_translate("Form", "Seçili Görevleri Sil"))
        self.asc_Sirala.setText(_translate("Form", "Görevleri Sırala (ASC)"))
        self.desc_Sirala.setText(_translate("Form", "Görevleri Sırala (DESC)"))
        self.rastgele_Sec.setText(_translate("Form", "Rastgele Görev Seç"))


if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec())
