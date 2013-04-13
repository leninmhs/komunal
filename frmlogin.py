# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frmlogin.ui'
#
# Created: Tue May 29 23:06:18 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmLogin(object):
    def setupUi(self, frmLogin):
        frmLogin.setObjectName(_fromUtf8("frmLogin"))
        frmLogin.resize(410, 381)
        frmLogin.setWindowTitle(QtGui.QApplication.translate("frmLogin", "Ingresar a Komunal", None, QtGui.QApplication.UnicodeUTF8))
        self.frame = QtGui.QFrame(frmLogin)
        self.frame.setGeometry(QtCore.QRect(10, 110, 391, 241))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.txtUsuario = QtGui.QLineEdit(self.frame)
        self.txtUsuario.setGeometry(QtCore.QRect(30, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setToolTip(QtGui.QApplication.translate("frmLogin", "Ingrese el usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        self.btnLoginAceptar = QtGui.QPushButton(self.frame)
        self.btnLoginAceptar.setGeometry(QtCore.QRect(30, 200, 97, 27))
        self.btnLoginAceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLoginAceptar.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}"))
        self.btnLoginAceptar.setText(QtGui.QApplication.translate("frmLogin", "Acceder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoginAceptar.setObjectName(_fromUtf8("btnLoginAceptar"))
        self.txtClave = QtGui.QLineEdit(self.frame)
        self.txtClave.setGeometry(QtCore.QRect(30, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtClave.setFont(font)
        self.txtClave.setToolTip(QtGui.QApplication.translate("frmLogin", "Ingrese su contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.txtClave.setInputMask(_fromUtf8(""))
        self.txtClave.setText(_fromUtf8(""))
        self.txtClave.setEchoMode(QtGui.QLineEdit.Password)
        self.txtClave.setObjectName(_fromUtf8("txtClave"))
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 180, 361, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 121, 20))
        self.label_2.setText(QtGui.QApplication.translate("frmLogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">Contraseña</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 60, 67, 17))
        self.label.setText(QtGui.QApplication.translate("frmLogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600;\">Usuario</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(1, 0, 389, 21))
        self.frame_2.setToolTip(QtGui.QApplication.translate("frmLogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Acceder al Sistema</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_2.setStyleSheet(_fromUtf8("border: none;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #a6a6a6, stop: 0.08 #7f7f7f,\n"
"stop: 0.39999 #717171, stop: 0.4 #626262,\n"
"stop: 0.9 #4c4c4c, stop: 1 #333333);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(100, -10, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("frmLogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Liberation Mono\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:16pt; font-weight:600; color:#55aa00; vertical-align:sub;\">Acceder al Sistema Komunal</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.candado = QtGui.QLabel(self.frame)
        self.candado.setEnabled(True)
        self.candado.setGeometry(QtCore.QRect(270, 60, 101, 121))
        self.candado.setText(_fromUtf8(""))
        self.candado.setPixmap(QtGui.QPixmap(_fromUtf8("img/candado.jpg")))
        self.candado.setObjectName(_fromUtf8("candado"))
        self.lblError = QtGui.QLabel(self.frame)
        self.lblError.setGeometry(QtCore.QRect(40, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.lblError.setFont(font)
        self.lblError.setText(QtGui.QApplication.translate("frmLogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblError.setObjectName(_fromUtf8("lblError"))
        self.btnRegistroLogin = QtGui.QPushButton(frmLogin)
        self.btnRegistroLogin.setGeometry(QtCore.QRect(290, 350, 111, 21))
        self.btnRegistroLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegistroLogin.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}"))
        self.btnRegistroLogin.setText(QtGui.QApplication.translate("frmLogin", "Registrarse", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRegistroLogin.setObjectName(_fromUtf8("btnRegistroLogin"))
        self.label_5 = QtGui.QLabel(frmLogin)
        self.label_5.setGeometry(QtCore.QRect(-10, 0, 401, 121))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("img/komunal-logo-beta.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)
        frmLogin.setTabOrder(self.txtUsuario, self.txtClave)
        frmLogin.setTabOrder(self.txtClave, self.btnLoginAceptar)
        frmLogin.setTabOrder(self.btnLoginAceptar, self.btnRegistroLogin)

    def retranslateUi(self, frmLogin):
        pass

