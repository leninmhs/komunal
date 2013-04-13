# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dlgbienvenida.ui'
#
# Created: Thu May 24 22:54:58 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgBienvenida(object):
    def setupUi(self, DlgBienvenida):
        DlgBienvenida.setObjectName(_fromUtf8("DlgBienvenida"))
        DlgBienvenida.resize(488, 286)
        DlgBienvenida.setWindowTitle(QtGui.QApplication.translate("DlgBienvenida", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        DlgBienvenida.setStyleSheet(_fromUtf8("background: white"))
        self.label = QtGui.QLabel(DlgBienvenida)
        self.label.setGeometry(QtCore.QRect(10, 0, 255, 28))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("DlgBienvenida", "Bienvenidos a Komunal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(DlgBienvenida)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 470, 111))
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setHtml(QtGui.QApplication.translate("DlgBienvenida", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">Komunal, tu sistema de gestión de consejos comunales. Registra a los integrantes de tu comunidad, llena el censo socioeconomico.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.layoutWidget = QtGui.QWidget(DlgBienvenida)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 230, 441, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnCancel = QtGui.QPushButton(self.layoutWidget)
        self.btnCancel.setText(QtGui.QApplication.translate("DlgBienvenida", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnContinuar = QtGui.QCommandLinkButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnContinuar.setFont(font)
        self.btnContinuar.setText(QtGui.QApplication.translate("DlgBienvenida", "Continuar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnContinuar.setObjectName(_fromUtf8("btnContinuar"))
        self.horizontalLayout.addWidget(self.btnContinuar)
        self.btnContinuar2 = QtGui.QCommandLinkButton(self.layoutWidget)
        self.btnContinuar2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnContinuar2.setFont(font)
        self.btnContinuar2.setText(QtGui.QApplication.translate("DlgBienvenida", "Continuar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnContinuar2.setObjectName(_fromUtf8("btnContinuar2"))
        self.horizontalLayout.addWidget(self.btnContinuar2)
        self.textBrowser_3 = QtGui.QTextBrowser(DlgBienvenida)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 80, 470, 121))
        self.textBrowser_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_3.setHtml(QtGui.QApplication.translate("DlgBienvenida", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Una vez creado el consejo comunal el censo es iniciado automaticamente, tenga en cuenta que la proxima vez que abra este sistema necesitara los datos de acceso que creara a continuación, no sea descuidado con ellos.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Disfrute su sistema Komunal.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_2 = QtGui.QTextBrowser(DlgBienvenida)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 160, 481, 61))
        self.textBrowser_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("DlgBienvenida", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">A continuación para poder iniciar el censo socioeconómico de tu comunidad deberás llenar los datos de conformación del  consejo comunal, así como crear tu usuario y contraseña para acceder al sistema en lo sucesivo.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))

        self.retranslateUi(DlgBienvenida)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgBienvenida.close)
        QtCore.QObject.connect(self.btnContinuar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.hide)
        QtCore.QObject.connect(self.btnContinuar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.hide)
        QtCore.QObject.connect(self.btnContinuar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser_2.hide)
        QtCore.QObject.connect(self.btnContinuar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnContinuar.hide)
        QtCore.QObject.connect(self.btnContinuar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnContinuar2.show)
        QtCore.QMetaObject.connectSlotsByName(DlgBienvenida)

    def retranslateUi(self, DlgBienvenida):
        pass

