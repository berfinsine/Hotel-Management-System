# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uygulama_giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(0, 800))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 800))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 1001, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../arka plan.jpg"))
        self.label.setObjectName("label")
        self.PbMisafirkayit = QtWidgets.QPushButton(self.centralwidget)
        self.PbMisafirkayit.setGeometry(QtCore.QRect(24, 610, 91, 24))
        self.PbMisafirkayit.setObjectName("PbMisafirkayit")
        self.PbOdaduzenleme = QtWidgets.QPushButton(self.centralwidget)
        self.PbOdaduzenleme.setGeometry(QtCore.QRect(150, 610, 121, 24))
        self.PbOdaduzenleme.setObjectName("PbOdaduzenleme")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 610, 101, 27))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PbMisafirkayit.setText(_translate("MainWindow", "Misafir Kayıt"))
        self.PbOdaduzenleme.setText(_translate("MainWindow", "Oda Düzenleme"))
        self.pushButton.setText(_translate("MainWindow", "Rezervasyon"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
