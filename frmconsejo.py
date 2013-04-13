# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frmconsejo.ui'
#
# Created: Wed Jun 20 23:49:49 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(899, 796)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Registro Consejo Comunal", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnGuardarConsejo = QtGui.QPushButton(self.centralwidget)
        self.btnGuardarConsejo.setGeometry(QtCore.QRect(790, 120, 97, 27))
        self.btnGuardarConsejo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuardarConsejo.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnGuardarConsejo.setText(QtGui.QApplication.translate("MainWindow", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGuardarConsejo.setObjectName(_fromUtf8("btnGuardarConsejo"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 0, 391, 31))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; color:#00007f;\">Solicitud de Registro Consejo Comunal</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 170, 97, 27))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 0, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #fff;\n"
"background: #73B65A;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #000;\n"
"background-color: rgb(247, 255, 153);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
""))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Cerrar Censo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(780, 280, 111, 27))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Generar Planilla", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 731, 281))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 721, 331))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.groupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 211, 31))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:600;\">Nombre del Consejo Comunal *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtNombreConsejo = QtGui.QLineEdit(self.groupBox)
        self.txtNombreConsejo.setGeometry(QtCore.QRect(10, 30, 451, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.txtNombreConsejo.setFont(font)
        self.txtNombreConsejo.setStyleSheet(_fromUtf8(""))
        self.txtNombreConsejo.setObjectName(_fromUtf8("txtNombreConsejo"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 61, 31))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:600; color:#000000;\">Estado *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(240, 60, 81, 31))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:600; color:#000000;\">Municipio *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtMunicipio = QtGui.QLineEdit(self.groupBox)
        self.txtMunicipio.setGeometry(QtCore.QRect(240, 90, 221, 27))
        self.txtMunicipio.setObjectName(_fromUtf8("txtMunicipio"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(490, 60, 81, 31))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:600; color:#000000;\">Parroquia *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtParroquia = QtGui.QLineEdit(self.groupBox)
        self.txtParroquia.setGeometry(QtCore.QRect(490, 90, 221, 27))
        self.txtParroquia.setObjectName(_fromUtf8("txtParroquia"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 120, 231, 31))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:600; color:#000000;\">Sector *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.txtSector = QtGui.QLineEdit(self.groupBox)
        self.txtSector.setGeometry(QtCore.QRect(10, 150, 701, 27))
        self.txtSector.setObjectName(_fromUtf8("txtSector"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:600; color:#000000;\">Dirección*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textDireccionConsejo = QtGui.QTextEdit(self.groupBox)
        self.textDireccionConsejo.setGeometry(QtCore.QRect(10, 210, 701, 61))
        self.textDireccionConsejo.setObjectName(_fromUtf8("textDireccionConsejo"))
        self.lblTipoConsejo = QtGui.QLabel(self.groupBox)
        self.lblTipoConsejo.setGeometry(QtCore.QRect(490, 0, 231, 31))
        self.lblTipoConsejo.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:600; color:#000000;\">Tipo de Consejo Comunal *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipoConsejo.setObjectName(_fromUtf8("lblTipoConsejo"))
        self.cmbTipoConsejo = QtGui.QComboBox(self.groupBox)
        self.cmbTipoConsejo.setGeometry(QtCore.QRect(490, 30, 221, 27))
        self.cmbTipoConsejo.setObjectName(_fromUtf8("cmbTipoConsejo"))
        self.cmbTipoConsejo.addItem(_fromUtf8(""))
        self.cmbTipoConsejo.setItemText(0, QtGui.QApplication.translate("MainWindow", "Urbana", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoConsejo.addItem(_fromUtf8(""))
        self.cmbTipoConsejo.setItemText(1, QtGui.QApplication.translate("MainWindow", "Indigena", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoConsejo.addItem(_fromUtf8(""))
        self.cmbTipoConsejo.setItemText(2, QtGui.QApplication.translate("MainWindow", "Rural", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado = QtGui.QComboBox(self.groupBox)
        self.cmbEstado.setGeometry(QtCore.QRect(10, 90, 211, 27))
        self.cmbEstado.setObjectName(_fromUtf8("cmbEstado"))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(0, QtGui.QApplication.translate("MainWindow", "Distrito Capital", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(1, QtGui.QApplication.translate("MainWindow", "Amazonas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(2, QtGui.QApplication.translate("MainWindow", "Anzoategui", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(3, QtGui.QApplication.translate("MainWindow", "Apure", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(4, QtGui.QApplication.translate("MainWindow", "Aragua", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(5, QtGui.QApplication.translate("MainWindow", "Barinas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(6, QtGui.QApplication.translate("MainWindow", "Bolivar", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(7, QtGui.QApplication.translate("MainWindow", "Carabobo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(8, QtGui.QApplication.translate("MainWindow", "Cojedes", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(9, QtGui.QApplication.translate("MainWindow", "Delta Amacuro", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(10, QtGui.QApplication.translate("MainWindow", "Falcon", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(11, QtGui.QApplication.translate("MainWindow", "Guarico", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(12, QtGui.QApplication.translate("MainWindow", "Lara", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(13, QtGui.QApplication.translate("MainWindow", "Merida", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(14, QtGui.QApplication.translate("MainWindow", "Miranda", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(15, QtGui.QApplication.translate("MainWindow", "Monagas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(16, QtGui.QApplication.translate("MainWindow", "Nueva Esparta", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(17, QtGui.QApplication.translate("MainWindow", "Portuguesa", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(18, QtGui.QApplication.translate("MainWindow", "Sucre", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(19, QtGui.QApplication.translate("MainWindow", "Tachira", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(20, QtGui.QApplication.translate("MainWindow", "Trujillo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(21, QtGui.QApplication.translate("MainWindow", "Yaracuy", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(22, QtGui.QApplication.translate("MainWindow", "Zulia", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstado.addItem(_fromUtf8(""))
        self.cmbEstado.setItemText(23, QtGui.QApplication.translate("MainWindow", "Vargas", None, QtGui.QApplication.UnicodeUTF8))
        self.lblErrorNombreConsejo = QtGui.QLabel(self.groupBox)
        self.lblErrorNombreConsejo.setGeometry(QtCore.QRect(210, 10, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorNombreConsejo.setFont(font)
        self.lblErrorNombreConsejo.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorNombreConsejo.setText(_fromUtf8(""))
        self.lblErrorNombreConsejo.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorNombreConsejo.setObjectName(_fromUtf8("lblErrorNombreConsejo"))
        self.lblErrorMunicipio = QtGui.QLabel(self.groupBox)
        self.lblErrorMunicipio.setGeometry(QtCore.QRect(320, 70, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorMunicipio.setFont(font)
        self.lblErrorMunicipio.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorMunicipio.setText(_fromUtf8(""))
        self.lblErrorMunicipio.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorMunicipio.setObjectName(_fromUtf8("lblErrorMunicipio"))
        self.lblErrorParroquia = QtGui.QLabel(self.groupBox)
        self.lblErrorParroquia.setGeometry(QtCore.QRect(570, 70, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorParroquia.setFont(font)
        self.lblErrorParroquia.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorParroquia.setText(_fromUtf8(""))
        self.lblErrorParroquia.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorParroquia.setObjectName(_fromUtf8("lblErrorParroquia"))
        self.lblErrorSector = QtGui.QLabel(self.groupBox)
        self.lblErrorSector.setGeometry(QtCore.QRect(70, 130, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorSector.setFont(font)
        self.lblErrorSector.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorSector.setText(_fromUtf8(""))
        self.lblErrorSector.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorSector.setObjectName(_fromUtf8("lblErrorSector"))
        self.lblErrorDireccionConsejo = QtGui.QLabel(self.groupBox)
        self.lblErrorDireccionConsejo.setGeometry(QtCore.QRect(90, 190, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorDireccionConsejo.setFont(font)
        self.lblErrorDireccionConsejo.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorDireccionConsejo.setText(_fromUtf8(""))
        self.lblErrorDireccionConsejo.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorDireccionConsejo.setObjectName(_fromUtf8("lblErrorDireccionConsejo"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 360, 731, 211))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Nombre*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.txtNombre = QtGui.QLineEdit(self.frame_2)
        self.txtNombre.setGeometry(QtCore.QRect(10, 30, 231, 27))
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(270, 0, 71, 31))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Apellido*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.txtApellido = QtGui.QLineEdit(self.frame_2)
        self.txtApellido.setGeometry(QtCore.QRect(270, 30, 231, 27))
        self.txtApellido.setObjectName(_fromUtf8("txtApellido"))
        self.txtCedula = QtGui.QLineEdit(self.frame_2)
        self.txtCedula.setGeometry(QtCore.QRect(530, 30, 181, 27))
        self.txtCedula.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txtCedula.setObjectName(_fromUtf8("txtCedula"))
        self.label_12 = QtGui.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(530, 0, 61, 31))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Cédula*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 71, 31))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Telefono*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(270, 60, 231, 31))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:600; color:#000000;\">Telefono 2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(530, 60, 51, 31))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:600; color:#000000;\">Correo</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.txtTelefono = QtGui.QLineEdit(self.frame_2)
        self.txtTelefono.setGeometry(QtCore.QRect(10, 90, 231, 27))
        self.txtTelefono.setObjectName(_fromUtf8("txtTelefono"))
        self.txtTelefono2 = QtGui.QLineEdit(self.frame_2)
        self.txtTelefono2.setGeometry(QtCore.QRect(270, 90, 231, 27))
        self.txtTelefono2.setObjectName(_fromUtf8("txtTelefono2"))
        self.txtCorreo = QtGui.QLineEdit(self.frame_2)
        self.txtCorreo.setGeometry(QtCore.QRect(530, 90, 181, 27))
        self.txtCorreo.setObjectName(_fromUtf8("txtCorreo"))
        self.label_11 = QtGui.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 81, 31))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Dirección*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.textDireccionPersona = QtGui.QTextEdit(self.frame_2)
        self.textDireccionPersona.setGeometry(QtCore.QRect(10, 150, 701, 51))
        self.textDireccionPersona.setObjectName(_fromUtf8("textDireccionPersona"))
        self.lblErrorVApellido = QtGui.QLabel(self.frame_2)
        self.lblErrorVApellido.setGeometry(QtCore.QRect(330, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorVApellido.setFont(font)
        self.lblErrorVApellido.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorVApellido.setText(_fromUtf8(""))
        self.lblErrorVApellido.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorVApellido.setObjectName(_fromUtf8("lblErrorVApellido"))
        self.lblErrorVCedula = QtGui.QLabel(self.frame_2)
        self.lblErrorVCedula.setGeometry(QtCore.QRect(580, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorVCedula.setFont(font)
        self.lblErrorVCedula.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorVCedula.setText(_fromUtf8(""))
        self.lblErrorVCedula.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorVCedula.setObjectName(_fromUtf8("lblErrorVCedula"))
        self.lblErrorVTlf = QtGui.QLabel(self.frame_2)
        self.lblErrorVTlf.setGeometry(QtCore.QRect(80, 70, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorVTlf.setFont(font)
        self.lblErrorVTlf.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorVTlf.setText(_fromUtf8(""))
        self.lblErrorVTlf.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorVTlf.setObjectName(_fromUtf8("lblErrorVTlf"))
        self.lblErrorVDireccion = QtGui.QLabel(self.frame_2)
        self.lblErrorVDireccion.setGeometry(QtCore.QRect(80, 130, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorVDireccion.setFont(font)
        self.lblErrorVDireccion.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorVDireccion.setText(_fromUtf8(""))
        self.lblErrorVDireccion.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorVDireccion.setObjectName(_fromUtf8("lblErrorVDireccion"))
        self.lblErrorVNombre = QtGui.QLabel(self.frame_2)
        self.lblErrorVNombre.setGeometry(QtCore.QRect(70, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorVNombre.setFont(font)
        self.lblErrorVNombre.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorVNombre.setText(_fromUtf8(""))
        self.lblErrorVNombre.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorVNombre.setObjectName(_fromUtf8("lblErrorVNombre"))
        self.lblErrorVCorreo = QtGui.QLabel(self.frame_2)
        self.lblErrorVCorreo.setGeometry(QtCore.QRect(580, 70, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorVCorreo.setFont(font)
        self.lblErrorVCorreo.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorVCorreo.setText(_fromUtf8(""))
        self.lblErrorVCorreo.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorVCorreo.setObjectName(_fromUtf8("lblErrorVCorreo"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(270, 580, 301, 21))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; color:#00007f;\">Datos de la cuenta de Usuario</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 600, 731, 141))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.usuario_4 = QtGui.QLabel(self.frame_3)
        self.usuario_4.setGeometry(QtCore.QRect(10, 0, 171, 31))
        self.usuario_4.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Nombre Completo *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario_4.setObjectName(_fromUtf8("usuario_4"))
        self.txtNombreCompleto = QtGui.QLineEdit(self.frame_3)
        self.txtNombreCompleto.setGeometry(QtCore.QRect(10, 30, 301, 27))
        self.txtNombreCompleto.setObjectName(_fromUtf8("txtNombreCompleto"))
        self.usuario_5 = QtGui.QLabel(self.frame_3)
        self.usuario_5.setGeometry(QtCore.QRect(330, 0, 61, 31))
        self.usuario_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Cédula *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario_5.setObjectName(_fromUtf8("usuario_5"))
        self.txtCedulaUsuario = QtGui.QLineEdit(self.frame_3)
        self.txtCedulaUsuario.setGeometry(QtCore.QRect(330, 30, 141, 27))
        self.txtCedulaUsuario.setObjectName(_fromUtf8("txtCedulaUsuario"))
        self.usuario_6 = QtGui.QLabel(self.frame_3)
        self.usuario_6.setGeometry(QtCore.QRect(490, 0, 111, 31))
        self.usuario_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:600; color:#000000;\">Correo</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario_6.setObjectName(_fromUtf8("usuario_6"))
        self.txtCorreoUsuario = QtGui.QLineEdit(self.frame_3)
        self.txtCorreoUsuario.setGeometry(QtCore.QRect(490, 30, 221, 27))
        self.txtCorreoUsuario.setObjectName(_fromUtf8("txtCorreoUsuario"))
        self.usuario = QtGui.QLabel(self.frame_3)
        self.usuario.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.usuario.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Usuario *</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario.setObjectName(_fromUtf8("usuario"))
        self.usuario_2 = QtGui.QLabel(self.frame_3)
        self.usuario_2.setGeometry(QtCore.QRect(260, 70, 81, 31))
        self.usuario_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Contraseña*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario_2.setObjectName(_fromUtf8("usuario_2"))
        self.usuario_3 = QtGui.QLabel(self.frame_3)
        self.usuario_3.setGeometry(QtCore.QRect(470, 70, 131, 31))
        self.usuario_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Repetir Contraseña*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.usuario_3.setObjectName(_fromUtf8("usuario_3"))
        self.txtUsuario = QtGui.QLineEdit(self.frame_3)
        self.txtUsuario.setGeometry(QtCore.QRect(10, 100, 181, 27))
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        self.txtClave = QtGui.QLineEdit(self.frame_3)
        self.txtClave.setGeometry(QtCore.QRect(260, 100, 171, 27))
        self.txtClave.setToolTip(QtGui.QApplication.translate("MainWindow", "Contraseña que tendra el usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.txtClave.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.txtClave.setEchoMode(QtGui.QLineEdit.Password)
        self.txtClave.setObjectName(_fromUtf8("txtClave"))
        self.lblErrorNombreUsuario = QtGui.QLabel(self.frame_3)
        self.lblErrorNombreUsuario.setGeometry(QtCore.QRect(150, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorNombreUsuario.setFont(font)
        self.lblErrorNombreUsuario.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorNombreUsuario.setText(_fromUtf8(""))
        self.lblErrorNombreUsuario.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorNombreUsuario.setObjectName(_fromUtf8("lblErrorNombreUsuario"))
        self.txtClave2 = QtGui.QLineEdit(self.frame_3)
        self.txtClave2.setGeometry(QtCore.QRect(500, 100, 171, 27))
        self.txtClave2.setEchoMode(QtGui.QLineEdit.Password)
        self.txtClave2.setObjectName(_fromUtf8("txtClave2"))
        self.lblErrorClavesIguales = QtGui.QLabel(self.frame_3)
        self.lblErrorClavesIguales.setGeometry(QtCore.QRect(270, 120, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorClavesIguales.setFont(font)
        self.lblErrorClavesIguales.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorClavesIguales.setText(_fromUtf8(""))
        self.lblErrorClavesIguales.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorClavesIguales.setObjectName(_fromUtf8("lblErrorClavesIguales"))
        self.lblErrorCedulaUsuario = QtGui.QLabel(self.frame_3)
        self.lblErrorCedulaUsuario.setGeometry(QtCore.QRect(380, 10, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorCedulaUsuario.setFont(font)
        self.lblErrorCedulaUsuario.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorCedulaUsuario.setText(_fromUtf8(""))
        self.lblErrorCedulaUsuario.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorCedulaUsuario.setObjectName(_fromUtf8("lblErrorCedulaUsuario"))
        self.lblErrorUsuario = QtGui.QLabel(self.frame_3)
        self.lblErrorUsuario.setGeometry(QtCore.QRect(70, 80, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorUsuario.setFont(font)
        self.lblErrorUsuario.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorUsuario.setText(_fromUtf8(""))
        self.lblErrorUsuario.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorUsuario.setObjectName(_fromUtf8("lblErrorUsuario"))
        self.lblErrorClave = QtGui.QLabel(self.frame_3)
        self.lblErrorClave.setGeometry(QtCore.QRect(340, 80, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorClave.setFont(font)
        self.lblErrorClave.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorClave.setText(_fromUtf8(""))
        self.lblErrorClave.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorClave.setObjectName(_fromUtf8("lblErrorClave"))
        self.lblErrorClave2 = QtGui.QLabel(self.frame_3)
        self.lblErrorClave2.setGeometry(QtCore.QRect(610, 80, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorClave2.setFont(font)
        self.lblErrorClave2.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorClave2.setText(_fromUtf8(""))
        self.lblErrorClave2.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorClave2.setObjectName(_fromUtf8("lblErrorClave2"))
        self.lblErrorCorreoUsuario = QtGui.QLabel(self.frame_3)
        self.lblErrorCorreoUsuario.setGeometry(QtCore.QRect(540, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorCorreoUsuario.setFont(font)
        self.lblErrorCorreoUsuario.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorCorreoUsuario.setText(_fromUtf8(""))
        self.lblErrorCorreoUsuario.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorCorreoUsuario.setObjectName(_fromUtf8("lblErrorCorreoUsuario"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(770, 260, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(770, 320, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(760, 50, 20, 731))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 171, 21))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; color:#00007f;\">Persona Contacto</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lblNotificacionConsejo = QtGui.QLabel(self.centralwidget)
        self.lblNotificacionConsejo.setGeometry(QtCore.QRect(20, 0, 741, 41))
        self.lblNotificacionConsejo.setStyleSheet(_fromUtf8("border: 1px solid Yellow;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #FFFF80, stop: 0.08 #FAFFD8,\n"
"stop: 0.39999 #FEFFE5, stop: 0.4 #FEFFE5,\n"
"stop: 0.9 #FAFFD8, stop: 1 #fff);\n"
"\n"
""))
        self.lblNotificacionConsejo.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">El consejo comunal fue registrado exitosamente :D</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Ingrese al sistema con el usuario y constraseña suministrado</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotificacionConsejo.setObjectName(_fromUtf8("lblNotificacionConsejo"))
        self.btnModificarConsejo = QtGui.QPushButton(self.centralwidget)
        self.btnModificarConsejo.setGeometry(QtCore.QRect(790, 220, 97, 27))
        self.btnModificarConsejo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarConsejo.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnModificarConsejo.setText(QtGui.QApplication.translate("MainWindow", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarConsejo.setObjectName(_fromUtf8("btnModificarConsejo"))
        self.btnSalirFrmConsejo = QtGui.QPushButton(self.centralwidget)
        self.btnSalirFrmConsejo.setGeometry(QtCore.QRect(780, 700, 97, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSalirFrmConsejo.setFont(font)
        self.btnSalirFrmConsejo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalirFrmConsejo.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
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
"}\n"
""))
        self.btnSalirFrmConsejo.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSalirFrmConsejo.setObjectName(_fromUtf8("btnSalirFrmConsejo"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtNombreConsejo.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtMunicipio.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtParroquia.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtSector.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textDireccionConsejo.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtNombre.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtApellido.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtCedula.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtTelefono.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtTelefono2.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtCorreo.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textDireccionPersona.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtNombreCompleto.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtCedulaUsuario.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtCorreoUsuario.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtUsuario.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtClave.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtClave2.clear)
        QtCore.QObject.connect(self.btnSalirFrmConsejo, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtNombreConsejo, self.cmbTipoConsejo)
        MainWindow.setTabOrder(self.cmbTipoConsejo, self.cmbEstado)
        MainWindow.setTabOrder(self.cmbEstado, self.txtMunicipio)
        MainWindow.setTabOrder(self.txtMunicipio, self.txtParroquia)
        MainWindow.setTabOrder(self.txtParroquia, self.txtSector)
        MainWindow.setTabOrder(self.txtSector, self.textDireccionConsejo)
        MainWindow.setTabOrder(self.textDireccionConsejo, self.txtNombre)
        MainWindow.setTabOrder(self.txtNombre, self.txtApellido)
        MainWindow.setTabOrder(self.txtApellido, self.txtCedula)
        MainWindow.setTabOrder(self.txtCedula, self.txtTelefono)
        MainWindow.setTabOrder(self.txtTelefono, self.txtTelefono2)
        MainWindow.setTabOrder(self.txtTelefono2, self.txtCorreo)
        MainWindow.setTabOrder(self.txtCorreo, self.textDireccionPersona)
        MainWindow.setTabOrder(self.textDireccionPersona, self.txtNombreCompleto)
        MainWindow.setTabOrder(self.txtNombreCompleto, self.txtCedulaUsuario)
        MainWindow.setTabOrder(self.txtCedulaUsuario, self.txtCorreoUsuario)
        MainWindow.setTabOrder(self.txtCorreoUsuario, self.txtUsuario)
        MainWindow.setTabOrder(self.txtUsuario, self.txtClave)
        MainWindow.setTabOrder(self.txtClave, self.txtClave2)
        MainWindow.setTabOrder(self.txtClave2, self.btnGuardarConsejo)
        MainWindow.setTabOrder(self.btnGuardarConsejo, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_4)

    def retranslateUi(self, MainWindow):
        pass

