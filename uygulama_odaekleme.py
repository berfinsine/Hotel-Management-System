# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uygulama_odaekleme.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1000, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../arka plan.jpg"))
        self.label.setObjectName("label")
        self.lneOdaAciklama = QtWidgets.QLineEdit(self.centralwidget)
        self.lneOdaAciklama.setGeometry(QtCore.QRect(20, 270, 221, 81))
        self.lneOdaAciklama.setObjectName("lneOdaAciklama")
        self.pbGuncelle = QtWidgets.QPushButton(self.centralwidget)
        self.pbGuncelle.setGeometry(QtCore.QRect(237, 390, 111, 27))
        self.pbGuncelle.setObjectName("pbGuncelle")
        self.pbKategori = QtWidgets.QPushButton(self.centralwidget)
        self.pbKategori.setGeometry(QtCore.QRect(550, 40, 201, 27))
        self.pbKategori.setObjectName("pbKategori")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 390, 151, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 90, 701, 231))
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.cmbOdaKategori = QtWidgets.QComboBox(self.centralwidget)
        self.cmbOdaKategori.setGeometry(QtCore.QRect(410, 40, 121, 25))
        self.cmbOdaKategori.setObjectName("cmbOdaKategori")
        self.cmbOdaKategori.addItem("")
        self.cmbOdaKategori.addItem("")
        self.cmbOdaKategori.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 60, 131, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.pbEkle = QtWidgets.QPushButton(self.centralwidget)
        self.pbEkle.setGeometry(QtCore.QRect(20, 390, 88, 27))
        self.pbEkle.setObjectName("pbEkle")
        self.lblOdaAciklama = QtWidgets.QLabel(self.centralwidget)
        self.lblOdaAciklama.setGeometry(QtCore.QRect(20, 230, 131, 35))
        self.lblOdaAciklama.setObjectName("lblOdaAciklama")
        self.lblOdaTipi_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblOdaTipi_2.setGeometry(QtCore.QRect(320, 30, 81, 35))
        self.lblOdaTipi_2.setObjectName("lblOdaTipi_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 60, 71, 161))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblOdaTipi = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblOdaTipi.setObjectName("lblOdaTipi")
        self.verticalLayout.addWidget(self.lblOdaTipi)
        self.lblOdaNo = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblOdaNo.setObjectName("lblOdaNo")
        self.verticalLayout.addWidget(self.lblOdaNo)
        self.lblKisiSayisi = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblKisiSayisi.setObjectName("lblKisiSayisi")
        self.verticalLayout.addWidget(self.lblKisiSayisi)
        self.lblUcret = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblUcret.setObjectName("lblUcret")
        self.verticalLayout.addWidget(self.lblUcret)
        self.pbSil = QtWidgets.QPushButton(self.centralwidget)
        self.pbSil.setGeometry(QtCore.QRect(130, 390, 88, 27))
        self.pbSil.setObjectName("pbSil")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 700, 151, 27))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmbOdaKategori.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbGuncelle.setText(_translate("MainWindow", "Oda Güncelle"))
        self.pbKategori.setText(_translate("MainWindow", "Kategoriye Göre Listele"))
        self.pushButton_4.setText(_translate("MainWindow", "Odaları Listele"))
        self.cmbOdaKategori.setItemText(0, _translate("MainWindow", "Standart"))
        self.cmbOdaKategori.setItemText(1, _translate("MainWindow", "Suit"))
        self.cmbOdaKategori.setItemText(2, _translate("MainWindow", "King"))
        self.pbEkle.setText(_translate("MainWindow", "Oda Ekle"))
        self.lblOdaAciklama.setText(_translate("MainWindow", "Oda Açıklaması"))
        self.lblOdaTipi_2.setText(_translate("MainWindow", "Oda Tipi"))
        self.lblOdaTipi.setText(_translate("MainWindow", "Oda Tipi"))
        self.lblOdaNo.setText(_translate("MainWindow", "Oda No"))
        self.lblKisiSayisi.setText(_translate("MainWindow", "Kişi Sayısı"))
        self.lblUcret.setText(_translate("MainWindow", "Ücret"))
        self.pbSil.setText(_translate("MainWindow", "Oda Sil"))
        self.pushButton.setText(_translate("MainWindow", "Ana Ekrana Dön"))
