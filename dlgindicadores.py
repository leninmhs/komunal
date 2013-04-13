# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dlgindicadores.ui'
#
# Created: Thu Jun 21 02:06:53 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgIndicadores(object):
    def setupUi(self, DlgIndicadores):
        DlgIndicadores.setObjectName(_fromUtf8("DlgIndicadores"))
        DlgIndicadores.resize(808, 565)
        self.tabWidget_2 = QtGui.QTabWidget(DlgIndicadores)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 771, 511))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(60, 20, 211, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lblMayor60 = QtGui.QLabel(self.tab_3)
        self.lblMayor60.setGeometry(QtCore.QRect(290, 20, 261, 16))
        self.lblMayor60.setObjectName(_fromUtf8("lblMayor60"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lblNino = QtGui.QLabel(self.tab_3)
        self.lblNino.setGeometry(QtCore.QRect(290, 70, 261, 16))
        self.lblNino.setObjectName(_fromUtf8("lblNino"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 191, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblPersonasComunidad = QtGui.QLabel(self.tab_3)
        self.lblPersonasComunidad.setGeometry(QtCore.QRect(290, 120, 261, 16))
        self.lblPersonasComunidad.setObjectName(_fromUtf8("lblPersonasComunidad"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 201, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(60, 220, 201, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lblSexoFemenino = QtGui.QLabel(self.tab_3)
        self.lblSexoFemenino.setGeometry(QtCore.QRect(290, 220, 261, 16))
        self.lblSexoFemenino.setObjectName(_fromUtf8("lblSexoFemenino"))
        self.lblSexoMasculino = QtGui.QLabel(self.tab_3)
        self.lblSexoMasculino.setGeometry(QtCore.QRect(290, 170, 261, 16))
        self.lblSexoMasculino.setObjectName(_fromUtf8("lblSexoMasculino"))
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(60, 270, 221, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(60, 320, 171, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lblAlfabetizada = QtGui.QLabel(self.tab_3)
        self.lblAlfabetizada.setGeometry(QtCore.QRect(290, 320, 261, 16))
        self.lblAlfabetizada.setObjectName(_fromUtf8("lblAlfabetizada"))
        self.line = QtGui.QFrame(self.tab_3)
        self.line.setGeometry(QtCore.QRect(60, 150, 501, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(60, 200, 501, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(60, 250, 501, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_5 = QtGui.QFrame(self.tab_3)
        self.line_5.setGeometry(QtCore.QRect(60, 300, 501, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.tab_3)
        self.line_6.setGeometry(QtCore.QRect(60, 360, 501, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.tab_3)
        self.line_7.setGeometry(QtCore.QRect(60, 100, 501, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.tab_3)
        self.line_8.setGeometry(QtCore.QRect(60, 50, 501, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.frame = QtGui.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(50, 380, 511, 41))
        self.frame.setStyleSheet(_fromUtf8("alternate-background-color: rgb(170, 170, 255);\n"
"background-color: rgb(247, 255, 153);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lblTotalPersonas = QtGui.QLabel(self.frame)
        self.lblTotalPersonas.setGeometry(QtCore.QRect(240, 10, 261, 16))
        self.lblTotalPersonas.setObjectName(_fromUtf8("lblTotalPersonas"))
        self.labelalfabetizada = QtGui.QLabel(self.tab_3)
        self.labelalfabetizada.setGeometry(QtCore.QRect(60, 330, 261, 41))
        self.labelalfabetizada.setObjectName(_fromUtf8("labelalfabetizada"))
        self.lblCantAdolecentes = QtGui.QLabel(self.tab_3)
        self.lblCantAdolecentes.setGeometry(QtCore.QRect(290, 270, 261, 16))
        self.lblCantAdolecentes.setObjectName(_fromUtf8("lblCantAdolecentes"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        self.btnCerrarIndicadores = QtGui.QPushButton(DlgIndicadores)
        self.btnCerrarIndicadores.setGeometry(QtCore.QRect(680, 530, 97, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCerrarIndicadores.setFont(font)
        self.btnCerrarIndicadores.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarIndicadores.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
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
        self.btnCerrarIndicadores.setObjectName(_fromUtf8("btnCerrarIndicadores"))
        self.btnGenerarPDF = QtGui.QPushButton(DlgIndicadores)
        self.btnGenerarPDF.setGeometry(QtCore.QRect(536, 530, 131, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnGenerarPDF.setFont(font)
        self.btnGenerarPDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenerarPDF.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
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
        self.btnGenerarPDF.setObjectName(_fromUtf8("btnGenerarPDF"))

        self.retranslateUi(DlgIndicadores)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QObject.connect(self.btnCerrarIndicadores, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgIndicadores.close)
        QtCore.QMetaObject.connectSlotsByName(DlgIndicadores)

    def retranslateUi(self, DlgIndicadores):
        DlgIndicadores.setWindowTitle(QtGui.QApplication.translate("DlgIndicadores", "Komunal - Indicadores", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Personas Mayores de 60 Años</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMayor60.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#3f3f3f;\">9</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Niños entre 3 y 12 Años</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNino.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#4f4f4f;\">TextLabel</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Personas de la comunidad</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPersonasComunidad.setText(QtGui.QApplication.translate("DlgIndicadores", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Personas del Sexo Masculino</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Personas del Sexo Femenino</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSexoFemenino.setText(QtGui.QApplication.translate("DlgIndicadores", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSexoMasculino.setText(QtGui.QApplication.translate("DlgIndicadores", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Adolecentes (entre 13 y 17 años)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Personas Alfabetizadas</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAlfabetizada.setText(QtGui.QApplication.translate("DlgIndicadores", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Total de Personas</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTotalPersonas.setText(QtGui.QApplication.translate("DlgIndicadores", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelalfabetizada.setText(QtGui.QApplication.translate("DlgIndicadores", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">personas mayores de 7 años sin nivel de instruccion</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCantAdolecentes.setText(QtGui.QApplication.translate("DlgIndicadores", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtGui.QApplication.translate("DlgIndicadores", "Indicadores", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("DlgIndicadores", "Estadísticas", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QtGui.QApplication.translate("DlgIndicadores", "Reportes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QtGui.QApplication.translate("DlgIndicadores", "Encuestas", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCerrarIndicadores.setText(QtGui.QApplication.translate("DlgIndicadores", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGenerarPDF.setText(QtGui.QApplication.translate("DlgIndicadores", "Imprimir en PDF", None, QtGui.QApplication.UnicodeUTF8))

