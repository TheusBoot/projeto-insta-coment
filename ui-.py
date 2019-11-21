# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'principal.ui',
# licensing of 'principal.ui' applies.
#
# Created: Thu Nov 21 14:22:29 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!
 
from PySide2 import QtCore, QtGui, QtWidgets
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 20, 501, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.user_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.user_edit.setObjectName("user_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_edit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.senha_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.senha_edit.setInputMask("")
        self.senha_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_edit.setObjectName("senha_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.senha_edit)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 360, 501, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_ok.setObjectName("btn_ok")
        self.verticalLayout.addWidget(self.btn_ok)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 140, 501, 161))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.hashtag_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.hashtag_edit.setObjectName("hashtag_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hashtag_edit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comente_edit = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.comente_edit.setObjectName("comente_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comente_edit)
        MainWindow.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Autogram", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "USUÁRIO: ", None, -1))
        self.user_edit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Digite seu usuário", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "SENHA: ", None, -1))
        self.senha_edit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Digite sua senha", None, -1))
        self.btn_ok.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", " HASHTAGS: ", None, -1))
        self.hashtag_edit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Hashtags chaves", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "COMENTÁRIOS", None, -1))
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
