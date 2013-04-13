# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frmfamilias.ui'
#
# Created: Sun Jun 24 15:17:40 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Censo_socioeconomico(object):
    def setupUi(self, Censo_socioeconomico):
        Censo_socioeconomico.setObjectName(_fromUtf8("Censo_socioeconomico"))
        Censo_socioeconomico.setEnabled(True)
        Censo_socioeconomico.resize(986, 724)
        Censo_socioeconomico.setWindowTitle(QtGui.QApplication.translate("Censo_socioeconomico", "Komunal - Censo Socio-Económico", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../img/icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Censo_socioeconomico.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Censo_socioeconomico)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblNombreConsejo = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblNombreConsejo.setFont(font)
        self.lblNombreConsejo.setStyleSheet(_fromUtf8("background: #E6EAEF"))
        self.lblNombreConsejo.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">Consejo Comunal: </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombreConsejo.setObjectName(_fromUtf8("lblNombreConsejo"))
        self.gridLayout_3.addWidget(self.lblNombreConsejo, 0, 0, 1, 1)
        self.lblUsuarioAutenticado = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblUsuarioAutenticado.setFont(font)
        self.lblUsuarioAutenticado.setStyleSheet(_fromUtf8("background: #E6EAEF"))
        self.lblUsuarioAutenticado.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">Usuario: </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUsuarioAutenticado.setObjectName(_fromUtf8("lblUsuarioAutenticado"))
        self.gridLayout_3.addWidget(self.lblUsuarioAutenticado, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(1600000, 720))
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px solid #C2C7CB;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     left: 5px; /* move to the right by 5px */\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 4px;\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 2px; /* make non-selected tabs look smaller */\n"
" }\n"
"\n"
" /* make use of negative margins for overlapping tabs */\n"
" QTabBar::tab:selected {\n"
"     /* expand/overlap to the left and right by 4px */\n"
"     margin-left: -4px;\n"
"     margin-right: -4px;\n"
" }\n"
"\n"
" QTabBar::tab:first:selected {\n"
"     margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
" }\n"
"\n"
" QTabBar::tab:last:selected {\n"
"     margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
" }\n"
"\n"
" QTabBar::tab:only-one {\n"
"     margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
" }"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Listado_familia = QtGui.QWidget()
        self.Listado_familia.setObjectName(_fromUtf8("Listado_familia"))
        self.tableWidget = QtGui.QTableWidget(self.Listado_familia)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 821, 501))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Id", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Cédula", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Sexo", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Edad", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Cant", None, QtGui.QApplication.UnicodeUTF8))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.frame = QtGui.QFrame(self.Listado_familia)
        self.frame.setGeometry(QtCore.QRect(10, 550, 821, 51))
        self.frame.setStyleSheet(_fromUtf8("border: none;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #a6a6a6, stop: 0.08 #7f7f7f,\n"
"stop: 0.39999 #717171, stop: 0.4 #626262,\n"
"stop: 0.9 #4c4c4c, stop: 1 #333333);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btnPlanillaFamilia = QtGui.QPushButton(self.frame)
        self.btnPlanillaFamilia.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnPlanillaFamilia.setFont(font)
        self.btnPlanillaFamilia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPlanillaFamilia.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnPlanillaFamilia.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Generar Planilla", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlanillaFamilia.setObjectName(_fromUtf8("btnPlanillaFamilia"))
        self.btnBorrarFamilia = QtGui.QPushButton(self.frame)
        self.btnBorrarFamilia.setGeometry(QtCore.QRect(160, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnBorrarFamilia.setFont(font)
        self.btnBorrarFamilia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBorrarFamilia.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnBorrarFamilia.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Eliminar Familia", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBorrarFamilia.setObjectName(_fromUtf8("btnBorrarFamilia"))
        self.btnModificarFamilia = QtGui.QPushButton(self.frame)
        self.btnModificarFamilia.setGeometry(QtCore.QRect(310, 10, 112, 32))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btnModificarFamilia.setFont(font)
        self.btnModificarFamilia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarFamilia.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 10;\n"
"padding: 0px;\n"
"font-size: 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 100px;\n"
"max-width: 100px;\n"
"min-height: 30px;\n"
"max-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
""))
        self.btnModificarFamilia.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Modificar Familia", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarFamilia.setObjectName(_fromUtf8("btnModificarFamilia"))
        self.btnSalirKomunal = QtGui.QPushButton(self.frame)
        self.btnSalirKomunal.setGeometry(QtCore.QRect(700, 10, 97, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSalirKomunal.setFont(font)
        self.btnSalirKomunal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalirKomunal.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnSalirKomunal.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSalirKomunal.setObjectName(_fromUtf8("btnSalirKomunal"))
        self.lblTotalFamilias = QtGui.QLabel(self.Listado_familia)
        self.lblTotalFamilias.setGeometry(QtCore.QRect(10, 530, 821, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTotalFamilias.setFont(font)
        self.lblTotalFamilias.setStyleSheet(_fromUtf8("background: #E6EAEF"))
        self.lblTotalFamilias.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Total de Registros Encontrados:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTotalFamilias.setObjectName(_fromUtf8("lblTotalFamilias"))
        self.tabWidget.addTab(self.Listado_familia, _fromUtf8(""))
        self.Datos_Familia = QtGui.QWidget()
        self.Datos_Familia.setObjectName(_fromUtf8("Datos_Familia"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Datos_Familia)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget1 = QtGui.QTabWidget(self.Datos_Familia)
        palette = QtGui.QPalette()
        self.tabWidget1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget1.setFont(font)
        self.tabWidget1.setObjectName(_fromUtf8("tabWidget1"))
        self.jefe_familia = QtGui.QWidget()
        self.jefe_familia.setObjectName(_fromUtf8("jefe_familia"))
        self.frame_3 = QtGui.QFrame(self.jefe_familia)
        self.frame_3.setGeometry(QtCore.QRect(50, 80, 741, 281))
        self.frame_3.setStyleSheet(_fromUtf8(""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.Sexo_jefe = QtGui.QLabel(self.frame_3)
        self.Sexo_jefe.setGeometry(QtCore.QRect(290, 80, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Sexo_jefe.setFont(font)
        self.Sexo_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Sexo *", None, QtGui.QApplication.UnicodeUTF8))
        self.Sexo_jefe.setObjectName(_fromUtf8("Sexo_jefe"))
        self.Ingreso_jefe = QtGui.QLabel(self.frame_3)
        self.Ingreso_jefe.setGeometry(QtCore.QRect(290, 150, 171, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Ingreso_jefe.setFont(font)
        self.Ingreso_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Ingresos Mensuales *", None, QtGui.QApplication.UnicodeUTF8))
        self.Ingreso_jefe.setObjectName(_fromUtf8("Ingreso_jefe"))
        self.cmbLugarNacimientoJefe = QtGui.QLineEdit(self.frame_3)
        self.cmbLugarNacimientoJefe.setGeometry(QtCore.QRect(20, 230, 221, 27))
        self.cmbLugarNacimientoJefe.setObjectName(_fromUtf8("cmbLugarNacimientoJefe"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(540, 10, 71, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Cédula *", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmbNacionalidadJefe = QtGui.QComboBox(self.frame_3)
        self.cmbNacionalidadJefe.setGeometry(QtCore.QRect(20, 100, 141, 27))
        self.cmbNacionalidadJefe.setObjectName(_fromUtf8("cmbNacionalidadJefe"))
        self.cmbNacionalidadJefe.addItem(_fromUtf8(""))
        self.cmbNacionalidadJefe.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Venezolano", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbNacionalidadJefe.addItem(_fromUtf8(""))
        self.cmbNacionalidadJefe.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Extranjero", None, QtGui.QApplication.UnicodeUTF8))
        self.txtApellidojefe = QtGui.QLineEdit(self.frame_3)
        self.txtApellidojefe.setGeometry(QtCore.QRect(290, 30, 221, 27))
        self.txtApellidojefe.setObjectName(_fromUtf8("txtApellidojefe"))
        self.cmbEdoCivilJefe = QtGui.QComboBox(self.frame_3)
        self.cmbEdoCivilJefe.setGeometry(QtCore.QRect(540, 100, 161, 27))
        self.cmbEdoCivilJefe.setObjectName(_fromUtf8("cmbEdoCivilJefe"))
        self.cmbEdoCivilJefe.addItem(_fromUtf8(""))
        self.cmbEdoCivilJefe.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilJefe.addItem(_fromUtf8(""))
        self.cmbEdoCivilJefe.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilJefe.addItem(_fromUtf8(""))
        self.cmbEdoCivilJefe.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilJefe.addItem(_fromUtf8(""))
        self.cmbEdoCivilJefe.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorciado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilJefe.addItem(_fromUtf8(""))
        self.cmbEdoCivilJefe.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyugue", None, QtGui.QApplication.UnicodeUTF8))
        self.Fecha_Nacimiento = QtGui.QLabel(self.frame_3)
        self.Fecha_Nacimiento.setGeometry(QtCore.QRect(290, 210, 161, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Fecha_Nacimiento.setFont(font)
        self.Fecha_Nacimiento.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Fecha de Nacimiento *", None, QtGui.QApplication.UnicodeUTF8))
        self.Fecha_Nacimiento.setObjectName(_fromUtf8("Fecha_Nacimiento"))
        self.txtNombrejefe = QtGui.QLineEdit(self.frame_3)
        self.txtNombrejefe.setGeometry(QtCore.QRect(20, 30, 221, 27))
        self.txtNombrejefe.setObjectName(_fromUtf8("txtNombrejefe"))
        self.Nombre_jefe = QtGui.QLabel(self.frame_3)
        self.Nombre_jefe.setGeometry(QtCore.QRect(20, 10, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Nombre_jefe.setFont(font)
        self.Nombre_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Nombres *", None, QtGui.QApplication.UnicodeUTF8))
        self.Nombre_jefe.setObjectName(_fromUtf8("Nombre_jefe"))
        self.txtCedulaJefe = QtGui.QLineEdit(self.frame_3)
        self.txtCedulaJefe.setGeometry(QtCore.QRect(540, 30, 181, 27))
        self.txtCedulaJefe.setObjectName(_fromUtf8("txtCedulaJefe"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(540, 80, 101, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Estado Civil *", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtIngresoJefe = QtGui.QLineEdit(self.frame_3)
        self.txtIngresoJefe.setGeometry(QtCore.QRect(290, 170, 171, 27))
        self.txtIngresoJefe.setObjectName(_fromUtf8("txtIngresoJefe"))
        self.Nacionalidad_jefe = QtGui.QLabel(self.frame_3)
        self.Nacionalidad_jefe.setGeometry(QtCore.QRect(20, 80, 111, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Nacionalidad_jefe.setFont(font)
        self.Nacionalidad_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Nacionalidad *", None, QtGui.QApplication.UnicodeUTF8))
        self.Nacionalidad_jefe.setObjectName(_fromUtf8("Nacionalidad_jefe"))
        self.Ocupacion_jefe = QtGui.QLabel(self.frame_3)
        self.Ocupacion_jefe.setGeometry(QtCore.QRect(20, 150, 121, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Ocupacion_jefe.setFont(font)
        self.Ocupacion_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Ocupación *", None, QtGui.QApplication.UnicodeUTF8))
        self.Ocupacion_jefe.setObjectName(_fromUtf8("Ocupacion_jefe"))
        self.Lugar_nacimiento_jefe = QtGui.QLabel(self.frame_3)
        self.Lugar_nacimiento_jefe.setGeometry(QtCore.QRect(20, 210, 171, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Lugar_nacimiento_jefe.setFont(font)
        self.Lugar_nacimiento_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Lugar de Nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.Lugar_nacimiento_jefe.setObjectName(_fromUtf8("Lugar_nacimiento_jefe"))
        self.cmbGradoInstruccion = QtGui.QComboBox(self.frame_3)
        self.cmbGradoInstruccion.setGeometry(QtCore.QRect(540, 170, 181, 27))
        self.cmbGradoInstruccion.setObjectName(_fromUtf8("cmbGradoInstruccion"))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "N/P", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGradoInstruccion.addItem(_fromUtf8(""))
        self.cmbGradoInstruccion.setItemText(8, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.Grado_Instruccion = QtGui.QLabel(self.frame_3)
        self.Grado_Instruccion.setGeometry(QtCore.QRect(540, 150, 161, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Grado_Instruccion.setFont(font)
        self.Grado_Instruccion.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Grado de Instrucción*", None, QtGui.QApplication.UnicodeUTF8))
        self.Grado_Instruccion.setObjectName(_fromUtf8("Grado_Instruccion"))
        self.Apellido_jefe = QtGui.QLabel(self.frame_3)
        self.Apellido_jefe.setGeometry(QtCore.QRect(290, 10, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Apellido_jefe.setFont(font)
        self.Apellido_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Apellidos *", None, QtGui.QApplication.UnicodeUTF8))
        self.Apellido_jefe.setObjectName(_fromUtf8("Apellido_jefe"))
        self.txtOcupacionJefe = QtGui.QLineEdit(self.frame_3)
        self.txtOcupacionJefe.setGeometry(QtCore.QRect(20, 170, 221, 27))
        self.txtOcupacionJefe.setObjectName(_fromUtf8("txtOcupacionJefe"))
        self.cmbSexoJefe = QtGui.QComboBox(self.frame_3)
        self.cmbSexoJefe.setGeometry(QtCore.QRect(290, 100, 121, 27))
        self.cmbSexoJefe.setObjectName(_fromUtf8("cmbSexoJefe"))
        self.cmbSexoJefe.addItem(_fromUtf8(""))
        self.cmbSexoJefe.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Masculino", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoJefe.addItem(_fromUtf8(""))
        self.cmbSexoJefe.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Femenino", None, QtGui.QApplication.UnicodeUTF8))
        self.txtFechaNacJefe = QtGui.QDateEdit(self.frame_3)
        self.txtFechaNacJefe.setGeometry(QtCore.QRect(290, 230, 171, 31))
        self.txtFechaNacJefe.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.txtFechaNacJefe.setDisplayFormat(QtGui.QApplication.translate("Censo_socioeconomico", "dd-MM-yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.txtFechaNacJefe.setCalendarPopup(True)
        self.txtFechaNacJefe.setObjectName(_fromUtf8("txtFechaNacJefe"))
        self.lblErrorNombreJefe = QtGui.QLabel(self.frame_3)
        self.lblErrorNombreJefe.setGeometry(QtCore.QRect(110, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorNombreJefe.setFont(font)
        self.lblErrorNombreJefe.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorNombreJefe.setText(_fromUtf8(""))
        self.lblErrorNombreJefe.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorNombreJefe.setObjectName(_fromUtf8("lblErrorNombreJefe"))
        self.lblErrorApellidoJefe = QtGui.QLabel(self.frame_3)
        self.lblErrorApellidoJefe.setGeometry(QtCore.QRect(380, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorApellidoJefe.setFont(font)
        self.lblErrorApellidoJefe.setStyleSheet(_fromUtf8("color: red;"))
        self.lblErrorApellidoJefe.setText(_fromUtf8(""))
        self.lblErrorApellidoJefe.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorApellidoJefe.setObjectName(_fromUtf8("lblErrorApellidoJefe"))
        self.lblErrorCedulaJefe = QtGui.QLabel(self.frame_3)
        self.lblErrorCedulaJefe.setGeometry(QtCore.QRect(620, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorCedulaJefe.setFont(font)
        self.lblErrorCedulaJefe.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorCedulaJefe.setText(_fromUtf8(""))
        self.lblErrorCedulaJefe.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorCedulaJefe.setObjectName(_fromUtf8("lblErrorCedulaJefe"))
        self.lblErrorOcupacionJefe = QtGui.QLabel(self.frame_3)
        self.lblErrorOcupacionJefe.setGeometry(QtCore.QRect(110, 150, 131, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorOcupacionJefe.setFont(font)
        self.lblErrorOcupacionJefe.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorOcupacionJefe.setText(_fromUtf8(""))
        self.lblErrorOcupacionJefe.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorOcupacionJefe.setObjectName(_fromUtf8("lblErrorOcupacionJefe"))
        self.lblErrorFechaJefe = QtGui.QLabel(self.frame_3)
        self.lblErrorFechaJefe.setGeometry(QtCore.QRect(290, 260, 161, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorFechaJefe.setFont(font)
        self.lblErrorFechaJefe.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorFechaJefe.setText(_fromUtf8(""))
        self.lblErrorFechaJefe.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorFechaJefe.setObjectName(_fromUtf8("lblErrorFechaJefe"))
        self.lblErrorIngresosJefe = QtGui.QLabel(self.frame_3)
        self.lblErrorIngresosJefe.setGeometry(QtCore.QRect(290, 130, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblErrorIngresosJefe.setFont(font)
        self.lblErrorIngresosJefe.setStyleSheet(_fromUtf8("color: red;\n"
"font: 11pt \"Ubuntu\";\n"
"font: italic 11pt \"Ubuntu\";"))
        self.lblErrorIngresosJefe.setText(_fromUtf8(""))
        self.lblErrorIngresosJefe.setTextFormat(QtCore.Qt.RichText)
        self.lblErrorIngresosJefe.setObjectName(_fromUtf8("lblErrorIngresosJefe"))
        self.lblNotificacionJefeFamilia = QtGui.QLabel(self.jefe_familia)
        self.lblNotificacionJefeFamilia.setGeometry(QtCore.QRect(50, 20, 741, 31))
        self.lblNotificacionJefeFamilia.setStyleSheet(_fromUtf8("border: 1px solid Yellow;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #FFFF80, stop: 0.08 #FAFFD8,\n"
"stop: 0.39999 #FEFFE5, stop: 0.4 #FEFFE5,\n"
"stop: 0.9 #FAFFD8, stop: 1 #fff);\n"
"\n"
""))
        self.lblNotificacionJefeFamilia.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotificacionJefeFamilia.setObjectName(_fromUtf8("lblNotificacionJefeFamilia"))
        self.Limpiar_datos_jefe = QtGui.QPushButton(self.jefe_familia)
        self.Limpiar_datos_jefe.setGeometry(QtCore.QRect(840, 140, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Limpiar_datos_jefe.setFont(font)
        self.Limpiar_datos_jefe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Limpiar_datos_jefe.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.Limpiar_datos_jefe.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.Limpiar_datos_jefe.setObjectName(_fromUtf8("Limpiar_datos_jefe"))
        self.btnGuardarJefeFamilia = QtGui.QPushButton(self.jefe_familia)
        self.btnGuardarJefeFamilia.setGeometry(QtCore.QRect(840, 90, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardarJefeFamilia.setFont(font)
        self.btnGuardarJefeFamilia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuardarJefeFamilia.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnGuardarJefeFamilia.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGuardarJefeFamilia.setObjectName(_fromUtf8("btnGuardarJefeFamilia"))
        self.btnModificarJefeFamilia = QtGui.QPushButton(self.jefe_familia)
        self.btnModificarJefeFamilia.setEnabled(True)
        self.btnModificarJefeFamilia.setGeometry(QtCore.QRect(840, 190, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModificarJefeFamilia.setFont(font)
        self.btnModificarJefeFamilia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarJefeFamilia.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnModificarJefeFamilia.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarJefeFamilia.setObjectName(_fromUtf8("btnModificarJefeFamilia"))
        self.line = QtGui.QFrame(self.jefe_familia)
        self.line.setGeometry(QtCore.QRect(820, 90, 16, 251))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tabWidget1.addTab(self.jefe_familia, _fromUtf8(""))
        self.intgrantes = QtGui.QWidget()
        self.intgrantes.setObjectName(_fromUtf8("intgrantes"))
        self.gridLayout_12 = QtGui.QGridLayout(self.intgrantes)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 0, 7, 1, 1)
        self.label_12 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_5.addWidget(self.label_12, 1, 2, 1, 1)
        self.label_53 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Cédulas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.gridLayout_5.addWidget(self.label_53, 1, 3, 1, 1)
        self.label_13 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Parentesco", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_5.addWidget(self.label_13, 1, 4, 1, 1)
        self.label_14 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Fecha Nac", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 1, 5, 1, 1)
        self.label_15 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Estado Civil", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_5.addWidget(self.label_15, 1, 7, 1, 1)
        self.label_16 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Grado de Instrucción", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 1, 8, 1, 1)
        self.label_17 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Ocupación", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_5.addWidget(self.label_17, 1, 9, 1, 1)
        self.label_18 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Ingreso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_5.addWidget(self.label_18, 1, 10, 1, 1)
        self.lblNombreF1 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF1.setObjectName(_fromUtf8("lblNombreF1"))
        self.gridLayout_5.addWidget(self.lblNombreF1, 2, 1, 1, 1)
        self.lblApellidoF1 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF1.setObjectName(_fromUtf8("lblApellidoF1"))
        self.gridLayout_5.addWidget(self.lblApellidoF1, 2, 2, 1, 1)
        self.lblCedulaF1 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF1.setObjectName(_fromUtf8("lblCedulaF1"))
        self.gridLayout_5.addWidget(self.lblCedulaF1, 2, 3, 1, 1)
        self.lblParentescoF1 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF1.setObjectName(_fromUtf8("lblParentescoF1"))
        self.gridLayout_5.addWidget(self.lblParentescoF1, 2, 4, 1, 1)
        self.cmbEdoCivilF1 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF1.setObjectName(_fromUtf8("cmbEdoCivilF1"))
        self.cmbEdoCivilF1.addItem(_fromUtf8(""))
        self.cmbEdoCivilF1.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF1.addItem(_fromUtf8(""))
        self.cmbEdoCivilF1.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF1.addItem(_fromUtf8(""))
        self.cmbEdoCivilF1.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF1.addItem(_fromUtf8(""))
        self.cmbEdoCivilF1.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF1.addItem(_fromUtf8(""))
        self.cmbEdoCivilF1.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF1, 2, 7, 1, 1)
        self.cmbInstruccionF1 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF1.setObjectName(_fromUtf8("cmbInstruccionF1"))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "N/P", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF1.addItem(_fromUtf8(""))
        self.cmbInstruccionF1.setItemText(8, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF1, 2, 8, 1, 1)
        self.lblOcupacionF1 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF1.setObjectName(_fromUtf8("lblOcupacionF1"))
        self.gridLayout_5.addWidget(self.lblOcupacionF1, 2, 9, 1, 1)
        self.lblIngresoF1 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF1.setObjectName(_fromUtf8("lblIngresoF1"))
        self.gridLayout_5.addWidget(self.lblIngresoF1, 2, 10, 1, 1)
        self.lblNombreF2 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF2.setObjectName(_fromUtf8("lblNombreF2"))
        self.gridLayout_5.addWidget(self.lblNombreF2, 3, 1, 1, 1)
        self.lblApellidoF2 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF2.setObjectName(_fromUtf8("lblApellidoF2"))
        self.gridLayout_5.addWidget(self.lblApellidoF2, 3, 2, 1, 1)
        self.lblCedulaF2 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF2.setObjectName(_fromUtf8("lblCedulaF2"))
        self.gridLayout_5.addWidget(self.lblCedulaF2, 3, 3, 1, 1)
        self.lblParentescoF2 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF2.setObjectName(_fromUtf8("lblParentescoF2"))
        self.gridLayout_5.addWidget(self.lblParentescoF2, 3, 4, 1, 1)
        self.cmbEdoCivilF2 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF2.setObjectName(_fromUtf8("cmbEdoCivilF2"))
        self.cmbEdoCivilF2.addItem(_fromUtf8(""))
        self.cmbEdoCivilF2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF2.addItem(_fromUtf8(""))
        self.cmbEdoCivilF2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF2.addItem(_fromUtf8(""))
        self.cmbEdoCivilF2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF2.addItem(_fromUtf8(""))
        self.cmbEdoCivilF2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF2.addItem(_fromUtf8(""))
        self.cmbEdoCivilF2.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF2, 3, 7, 1, 1)
        self.cmbInstruccionF2 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF2.setObjectName(_fromUtf8("cmbInstruccionF2"))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF2.addItem(_fromUtf8(""))
        self.cmbInstruccionF2.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF2, 3, 8, 1, 1)
        self.lblOcupacionF2 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF2.setObjectName(_fromUtf8("lblOcupacionF2"))
        self.gridLayout_5.addWidget(self.lblOcupacionF2, 3, 9, 1, 1)
        self.lblIngresoF2 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF2.setObjectName(_fromUtf8("lblIngresoF2"))
        self.gridLayout_5.addWidget(self.lblIngresoF2, 3, 10, 1, 1)
        self.lblNombreF3 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF3.setObjectName(_fromUtf8("lblNombreF3"))
        self.gridLayout_5.addWidget(self.lblNombreF3, 4, 1, 1, 1)
        self.lblApellidoF3 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF3.setObjectName(_fromUtf8("lblApellidoF3"))
        self.gridLayout_5.addWidget(self.lblApellidoF3, 4, 2, 1, 1)
        self.lblCedulaF3 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF3.setObjectName(_fromUtf8("lblCedulaF3"))
        self.gridLayout_5.addWidget(self.lblCedulaF3, 4, 3, 1, 1)
        self.lblParentescoF3 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF3.setObjectName(_fromUtf8("lblParentescoF3"))
        self.gridLayout_5.addWidget(self.lblParentescoF3, 4, 4, 1, 1)
        self.cmbEdoCivilF3 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF3.setObjectName(_fromUtf8("cmbEdoCivilF3"))
        self.cmbEdoCivilF3.addItem(_fromUtf8(""))
        self.cmbEdoCivilF3.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF3.addItem(_fromUtf8(""))
        self.cmbEdoCivilF3.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF3.addItem(_fromUtf8(""))
        self.cmbEdoCivilF3.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF3.addItem(_fromUtf8(""))
        self.cmbEdoCivilF3.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF3.addItem(_fromUtf8(""))
        self.cmbEdoCivilF3.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF3, 4, 7, 1, 1)
        self.cmbInstruccionF3 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF3.setObjectName(_fromUtf8("cmbInstruccionF3"))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF3.addItem(_fromUtf8(""))
        self.cmbInstruccionF3.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF3, 4, 8, 1, 1)
        self.lblOcupacionF3 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF3.setObjectName(_fromUtf8("lblOcupacionF3"))
        self.gridLayout_5.addWidget(self.lblOcupacionF3, 4, 9, 1, 1)
        self.lblIngresoF3 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF3.setObjectName(_fromUtf8("lblIngresoF3"))
        self.gridLayout_5.addWidget(self.lblIngresoF3, 4, 10, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(13, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 5, 0, 1, 1)
        self.lblNombreF4 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF4.setObjectName(_fromUtf8("lblNombreF4"))
        self.gridLayout_5.addWidget(self.lblNombreF4, 5, 1, 1, 1)
        self.lblApellidoF4 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF4.setObjectName(_fromUtf8("lblApellidoF4"))
        self.gridLayout_5.addWidget(self.lblApellidoF4, 5, 2, 1, 1)
        self.lblCedulaF4 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF4.setObjectName(_fromUtf8("lblCedulaF4"))
        self.gridLayout_5.addWidget(self.lblCedulaF4, 5, 3, 1, 1)
        self.lblParentescoF4 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF4.setObjectName(_fromUtf8("lblParentescoF4"))
        self.gridLayout_5.addWidget(self.lblParentescoF4, 5, 4, 1, 1)
        self.cmbEdoCivilF4 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF4.setObjectName(_fromUtf8("cmbEdoCivilF4"))
        self.cmbEdoCivilF4.addItem(_fromUtf8(""))
        self.cmbEdoCivilF4.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF4.addItem(_fromUtf8(""))
        self.cmbEdoCivilF4.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF4.addItem(_fromUtf8(""))
        self.cmbEdoCivilF4.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF4.addItem(_fromUtf8(""))
        self.cmbEdoCivilF4.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF4.addItem(_fromUtf8(""))
        self.cmbEdoCivilF4.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF4, 5, 7, 1, 1)
        self.cmbInstruccionF4 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF4.setObjectName(_fromUtf8("cmbInstruccionF4"))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF4.addItem(_fromUtf8(""))
        self.cmbInstruccionF4.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF4, 5, 8, 1, 1)
        self.lblOcupacionF4 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF4.setObjectName(_fromUtf8("lblOcupacionF4"))
        self.gridLayout_5.addWidget(self.lblOcupacionF4, 5, 9, 1, 1)
        self.lblIngresoF4 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF4.setObjectName(_fromUtf8("lblIngresoF4"))
        self.gridLayout_5.addWidget(self.lblIngresoF4, 5, 10, 1, 1)
        self.lblNombreF5 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF5.setObjectName(_fromUtf8("lblNombreF5"))
        self.gridLayout_5.addWidget(self.lblNombreF5, 6, 1, 1, 1)
        self.lblApellidoF5 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF5.setObjectName(_fromUtf8("lblApellidoF5"))
        self.gridLayout_5.addWidget(self.lblApellidoF5, 6, 2, 1, 1)
        self.lblCedulaF5 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF5.setObjectName(_fromUtf8("lblCedulaF5"))
        self.gridLayout_5.addWidget(self.lblCedulaF5, 6, 3, 1, 1)
        self.lblParentescoF5 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF5.setObjectName(_fromUtf8("lblParentescoF5"))
        self.gridLayout_5.addWidget(self.lblParentescoF5, 6, 4, 1, 1)
        self.cmbEdoCivilF5 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF5.setObjectName(_fromUtf8("cmbEdoCivilF5"))
        self.cmbEdoCivilF5.addItem(_fromUtf8(""))
        self.cmbEdoCivilF5.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF5.addItem(_fromUtf8(""))
        self.cmbEdoCivilF5.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF5.addItem(_fromUtf8(""))
        self.cmbEdoCivilF5.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF5.addItem(_fromUtf8(""))
        self.cmbEdoCivilF5.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF5.addItem(_fromUtf8(""))
        self.cmbEdoCivilF5.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF5, 6, 7, 1, 1)
        self.cmbInstruccionF5 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF5.setObjectName(_fromUtf8("cmbInstruccionF5"))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF5.addItem(_fromUtf8(""))
        self.cmbInstruccionF5.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF5, 6, 8, 1, 1)
        self.lblOcupacionF5 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF5.setObjectName(_fromUtf8("lblOcupacionF5"))
        self.gridLayout_5.addWidget(self.lblOcupacionF5, 6, 9, 1, 1)
        self.lblIngresoF5 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF5.setObjectName(_fromUtf8("lblIngresoF5"))
        self.gridLayout_5.addWidget(self.lblIngresoF5, 6, 10, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(13, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 6, 11, 1, 1)
        self.lblNombreF6 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF6.setObjectName(_fromUtf8("lblNombreF6"))
        self.gridLayout_5.addWidget(self.lblNombreF6, 7, 1, 1, 1)
        self.lblApellidoF6 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF6.setObjectName(_fromUtf8("lblApellidoF6"))
        self.gridLayout_5.addWidget(self.lblApellidoF6, 7, 2, 1, 1)
        self.lblCedulaF6 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF6.setObjectName(_fromUtf8("lblCedulaF6"))
        self.gridLayout_5.addWidget(self.lblCedulaF6, 7, 3, 1, 1)
        self.lblParentescoF6 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF6.setObjectName(_fromUtf8("lblParentescoF6"))
        self.gridLayout_5.addWidget(self.lblParentescoF6, 7, 4, 1, 1)
        self.cmbEdoCivilF6 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF6.setObjectName(_fromUtf8("cmbEdoCivilF6"))
        self.cmbEdoCivilF6.addItem(_fromUtf8(""))
        self.cmbEdoCivilF6.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF6.addItem(_fromUtf8(""))
        self.cmbEdoCivilF6.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF6.addItem(_fromUtf8(""))
        self.cmbEdoCivilF6.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF6.addItem(_fromUtf8(""))
        self.cmbEdoCivilF6.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF6.addItem(_fromUtf8(""))
        self.cmbEdoCivilF6.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF6, 7, 7, 1, 1)
        self.cmbInstruccionF6 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF6.setObjectName(_fromUtf8("cmbInstruccionF6"))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF6.addItem(_fromUtf8(""))
        self.cmbInstruccionF6.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF6, 7, 8, 1, 1)
        self.lblOcupacionF6 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF6.setObjectName(_fromUtf8("lblOcupacionF6"))
        self.gridLayout_5.addWidget(self.lblOcupacionF6, 7, 9, 1, 1)
        self.lblIngresoF6 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF6.setObjectName(_fromUtf8("lblIngresoF6"))
        self.gridLayout_5.addWidget(self.lblIngresoF6, 7, 10, 1, 1)
        self.lblNombreF7 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF7.setObjectName(_fromUtf8("lblNombreF7"))
        self.gridLayout_5.addWidget(self.lblNombreF7, 8, 1, 1, 1)
        self.lblApellidoF7 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF7.setObjectName(_fromUtf8("lblApellidoF7"))
        self.gridLayout_5.addWidget(self.lblApellidoF7, 8, 2, 1, 1)
        self.lblCedulaF7 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF7.setObjectName(_fromUtf8("lblCedulaF7"))
        self.gridLayout_5.addWidget(self.lblCedulaF7, 8, 3, 1, 1)
        self.lblParentescoF7 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF7.setObjectName(_fromUtf8("lblParentescoF7"))
        self.gridLayout_5.addWidget(self.lblParentescoF7, 8, 4, 1, 1)
        self.cmbEdoCivilF7 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF7.setObjectName(_fromUtf8("cmbEdoCivilF7"))
        self.cmbEdoCivilF7.addItem(_fromUtf8(""))
        self.cmbEdoCivilF7.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF7.addItem(_fromUtf8(""))
        self.cmbEdoCivilF7.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF7.addItem(_fromUtf8(""))
        self.cmbEdoCivilF7.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF7.addItem(_fromUtf8(""))
        self.cmbEdoCivilF7.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF7.addItem(_fromUtf8(""))
        self.cmbEdoCivilF7.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF7, 8, 7, 1, 1)
        self.cmbInstruccionF7 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF7.setObjectName(_fromUtf8("cmbInstruccionF7"))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF7.addItem(_fromUtf8(""))
        self.cmbInstruccionF7.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF7, 8, 8, 1, 1)
        self.lblOcupacionF7 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF7.setObjectName(_fromUtf8("lblOcupacionF7"))
        self.gridLayout_5.addWidget(self.lblOcupacionF7, 8, 9, 1, 1)
        self.lblIngresoF7 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF7.setObjectName(_fromUtf8("lblIngresoF7"))
        self.gridLayout_5.addWidget(self.lblIngresoF7, 8, 10, 1, 1)
        self.lblNombreF8 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF8.setObjectName(_fromUtf8("lblNombreF8"))
        self.gridLayout_5.addWidget(self.lblNombreF8, 9, 1, 1, 1)
        self.lblApellidoF8 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF8.setObjectName(_fromUtf8("lblApellidoF8"))
        self.gridLayout_5.addWidget(self.lblApellidoF8, 9, 2, 1, 1)
        self.lblCedulaF8 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF8.setObjectName(_fromUtf8("lblCedulaF8"))
        self.gridLayout_5.addWidget(self.lblCedulaF8, 9, 3, 1, 1)
        self.lblParentescoF8 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF8.setObjectName(_fromUtf8("lblParentescoF8"))
        self.gridLayout_5.addWidget(self.lblParentescoF8, 9, 4, 1, 1)
        self.cmbEdoCivilF8 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF8.setObjectName(_fromUtf8("cmbEdoCivilF8"))
        self.cmbEdoCivilF8.addItem(_fromUtf8(""))
        self.cmbEdoCivilF8.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF8.addItem(_fromUtf8(""))
        self.cmbEdoCivilF8.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF8.addItem(_fromUtf8(""))
        self.cmbEdoCivilF8.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF8.addItem(_fromUtf8(""))
        self.cmbEdoCivilF8.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF8.addItem(_fromUtf8(""))
        self.cmbEdoCivilF8.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF8, 9, 7, 1, 1)
        self.cmbInstruccionF8 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF8.setObjectName(_fromUtf8("cmbInstruccionF8"))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF8.addItem(_fromUtf8(""))
        self.cmbInstruccionF8.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF8, 9, 8, 1, 1)
        self.lblOcupacionF8 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF8.setObjectName(_fromUtf8("lblOcupacionF8"))
        self.gridLayout_5.addWidget(self.lblOcupacionF8, 9, 9, 1, 1)
        self.lblIngresoF8 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF8.setObjectName(_fromUtf8("lblIngresoF8"))
        self.gridLayout_5.addWidget(self.lblIngresoF8, 9, 10, 1, 1)
        self.lblNombreF9 = QtGui.QLineEdit(self.intgrantes)
        self.lblNombreF9.setObjectName(_fromUtf8("lblNombreF9"))
        self.gridLayout_5.addWidget(self.lblNombreF9, 10, 1, 1, 1)
        self.lblApellidoF9 = QtGui.QLineEdit(self.intgrantes)
        self.lblApellidoF9.setObjectName(_fromUtf8("lblApellidoF9"))
        self.gridLayout_5.addWidget(self.lblApellidoF9, 10, 2, 1, 1)
        self.lblCedulaF9 = QtGui.QLineEdit(self.intgrantes)
        self.lblCedulaF9.setObjectName(_fromUtf8("lblCedulaF9"))
        self.gridLayout_5.addWidget(self.lblCedulaF9, 10, 3, 1, 1)
        self.lblParentescoF9 = QtGui.QLineEdit(self.intgrantes)
        self.lblParentescoF9.setObjectName(_fromUtf8("lblParentescoF9"))
        self.gridLayout_5.addWidget(self.lblParentescoF9, 10, 4, 1, 1)
        self.cmbEdoCivilF9 = QtGui.QComboBox(self.intgrantes)
        self.cmbEdoCivilF9.setObjectName(_fromUtf8("cmbEdoCivilF9"))
        self.cmbEdoCivilF9.addItem(_fromUtf8(""))
        self.cmbEdoCivilF9.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Soltero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF9.addItem(_fromUtf8(""))
        self.cmbEdoCivilF9.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Casado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF9.addItem(_fromUtf8(""))
        self.cmbEdoCivilF9.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Viudo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF9.addItem(_fromUtf8(""))
        self.cmbEdoCivilF9.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Divorsiado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEdoCivilF9.addItem(_fromUtf8(""))
        self.cmbEdoCivilF9.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Conyuge", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbEdoCivilF9, 10, 7, 1, 1)
        self.cmbInstruccionF9 = QtGui.QComboBox(self.intgrantes)
        self.cmbInstruccionF9.setObjectName(_fromUtf8("cmbInstruccionF9"))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bachiller", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Basica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Tecnico Medio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "T.S.U.", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Licenciatura", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "Ingeniero", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "Doctorado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbInstruccionF9.addItem(_fromUtf8(""))
        self.cmbInstruccionF9.setItemText(7, QtGui.QApplication.translate("Censo_socioeconomico", "Magister", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbInstruccionF9, 10, 8, 1, 1)
        self.lblOcupacionF9 = QtGui.QLineEdit(self.intgrantes)
        self.lblOcupacionF9.setObjectName(_fromUtf8("lblOcupacionF9"))
        self.gridLayout_5.addWidget(self.lblOcupacionF9, 10, 9, 1, 1)
        self.lblIngresoF9 = QtGui.QLineEdit(self.intgrantes)
        self.lblIngresoF9.setObjectName(_fromUtf8("lblIngresoF9"))
        self.gridLayout_5.addWidget(self.lblIngresoF9, 10, 10, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 11, 7, 1, 1)
        self.label_11 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_5.addWidget(self.label_11, 1, 1, 1, 1)
        self.lblFechaF1 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF1.setDisplayFormat(QtGui.QApplication.translate("Censo_socioeconomico", "dd-MM-yy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFechaF1.setCalendarPopup(True)
        self.lblFechaF1.setObjectName(_fromUtf8("lblFechaF1"))
        self.gridLayout_5.addWidget(self.lblFechaF1, 2, 5, 1, 1)
        self.lblFechaF2 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF2.setDisplayFormat(QtGui.QApplication.translate("Censo_socioeconomico", "dd-MM-yy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFechaF2.setCalendarPopup(True)
        self.lblFechaF2.setObjectName(_fromUtf8("lblFechaF2"))
        self.gridLayout_5.addWidget(self.lblFechaF2, 3, 5, 1, 1)
        self.lblFechaF3 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF3.setDisplayFormat(QtGui.QApplication.translate("Censo_socioeconomico", "dd-MM-yy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFechaF3.setCalendarPopup(True)
        self.lblFechaF3.setObjectName(_fromUtf8("lblFechaF3"))
        self.gridLayout_5.addWidget(self.lblFechaF3, 4, 5, 1, 1)
        self.lblFechaF4 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF4.setCalendarPopup(True)
        self.lblFechaF4.setObjectName(_fromUtf8("lblFechaF4"))
        self.gridLayout_5.addWidget(self.lblFechaF4, 5, 5, 1, 1)
        self.lblFechaF5 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF5.setCalendarPopup(True)
        self.lblFechaF5.setObjectName(_fromUtf8("lblFechaF5"))
        self.gridLayout_5.addWidget(self.lblFechaF5, 6, 5, 1, 1)
        self.lblFechaF6 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF6.setCalendarPopup(True)
        self.lblFechaF6.setObjectName(_fromUtf8("lblFechaF6"))
        self.gridLayout_5.addWidget(self.lblFechaF6, 7, 5, 1, 1)
        self.lblFechaF7 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF7.setCalendarPopup(True)
        self.lblFechaF7.setObjectName(_fromUtf8("lblFechaF7"))
        self.gridLayout_5.addWidget(self.lblFechaF7, 8, 5, 1, 1)
        self.lblFechaF8 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF8.setCalendarPopup(True)
        self.lblFechaF8.setObjectName(_fromUtf8("lblFechaF8"))
        self.gridLayout_5.addWidget(self.lblFechaF8, 9, 5, 1, 1)
        self.lblFechaF9 = QtGui.QDateEdit(self.intgrantes)
        self.lblFechaF9.setCalendarPopup(True)
        self.lblFechaF9.setObjectName(_fromUtf8("lblFechaF9"))
        self.gridLayout_5.addWidget(self.lblFechaF9, 10, 5, 1, 1)
        self.cmbSexoF1 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF1.setObjectName(_fromUtf8("cmbSexoF1"))
        self.cmbSexoF1.addItem(_fromUtf8(""))
        self.cmbSexoF1.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF1.addItem(_fromUtf8(""))
        self.cmbSexoF1.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF1, 2, 6, 1, 1)
        self.cmbSexoF2 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF2.setObjectName(_fromUtf8("cmbSexoF2"))
        self.cmbSexoF2.addItem(_fromUtf8(""))
        self.cmbSexoF2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF2.addItem(_fromUtf8(""))
        self.cmbSexoF2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF2, 3, 6, 1, 1)
        self.cmbSexoF3 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF3.setObjectName(_fromUtf8("cmbSexoF3"))
        self.cmbSexoF3.addItem(_fromUtf8(""))
        self.cmbSexoF3.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF3.addItem(_fromUtf8(""))
        self.cmbSexoF3.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF3, 4, 6, 1, 1)
        self.cmbSexoF4 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF4.setObjectName(_fromUtf8("cmbSexoF4"))
        self.cmbSexoF4.addItem(_fromUtf8(""))
        self.cmbSexoF4.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF4.addItem(_fromUtf8(""))
        self.cmbSexoF4.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF4, 5, 6, 1, 1)
        self.cmbSexoF5 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF5.setObjectName(_fromUtf8("cmbSexoF5"))
        self.cmbSexoF5.addItem(_fromUtf8(""))
        self.cmbSexoF5.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF5.addItem(_fromUtf8(""))
        self.cmbSexoF5.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF5, 6, 6, 1, 1)
        self.cmbSexoF6 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF6.setObjectName(_fromUtf8("cmbSexoF6"))
        self.cmbSexoF6.addItem(_fromUtf8(""))
        self.cmbSexoF6.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF6.addItem(_fromUtf8(""))
        self.cmbSexoF6.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF6, 7, 6, 1, 1)
        self.cmbSexoF7 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF7.setObjectName(_fromUtf8("cmbSexoF7"))
        self.cmbSexoF7.addItem(_fromUtf8(""))
        self.cmbSexoF7.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF7.addItem(_fromUtf8(""))
        self.cmbSexoF7.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF7, 8, 6, 1, 1)
        self.cmbSexoF8 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF8.setObjectName(_fromUtf8("cmbSexoF8"))
        self.cmbSexoF8.addItem(_fromUtf8(""))
        self.cmbSexoF8.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF8.addItem(_fromUtf8(""))
        self.cmbSexoF8.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF8, 9, 6, 1, 1)
        self.cmbSexoF9 = QtGui.QComboBox(self.intgrantes)
        self.cmbSexoF9.setObjectName(_fromUtf8("cmbSexoF9"))
        self.cmbSexoF9.addItem(_fromUtf8(""))
        self.cmbSexoF9.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSexoF9.addItem(_fromUtf8(""))
        self.cmbSexoF9.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5.addWidget(self.cmbSexoF9, 10, 6, 1, 1)
        self.label_3 = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Sexo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 1, 6, 1, 1)
        self.btnLimpiarGFamiliar = QtGui.QPushButton(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnLimpiarGFamiliar.setFont(font)
        self.btnLimpiarGFamiliar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLimpiarGFamiliar.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnLimpiarGFamiliar.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLimpiarGFamiliar.setObjectName(_fromUtf8("btnLimpiarGFamiliar"))
        self.gridLayout_5.addWidget(self.btnLimpiarGFamiliar, 11, 6, 1, 1)
        self.btnGuardarMiembros = QtGui.QPushButton(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardarMiembros.setFont(font)
        self.btnGuardarMiembros.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuardarMiembros.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnGuardarMiembros.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGuardarMiembros.setObjectName(_fromUtf8("btnGuardarMiembros"))
        self.gridLayout_5.addWidget(self.btnGuardarMiembros, 11, 5, 1, 1)
        self.btnModificarMiembros = QtGui.QPushButton(self.intgrantes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModificarMiembros.setFont(font)
        self.btnModificarMiembros.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarMiembros.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnModificarMiembros.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarMiembros.setObjectName(_fromUtf8("btnModificarMiembros"))
        self.gridLayout_5.addWidget(self.btnModificarMiembros, 11, 4, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.lblNotificacionGrupoFamiliar = QtGui.QLabel(self.intgrantes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblNotificacionGrupoFamiliar.setFont(font)
        self.lblNotificacionGrupoFamiliar.setStyleSheet(_fromUtf8("border: 1px solid Yellow;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #FFFF80, stop: 0.08 #FAFFD8,\n"
"stop: 0.39999 #FEFFE5, stop: 0.4 #FEFFE5,\n"
"stop: 0.9 #FAFFD8, stop: 1 #fff);\n"
"\n"
""))
        self.lblNotificacionGrupoFamiliar.setText(_fromUtf8(""))
        self.lblNotificacionGrupoFamiliar.setObjectName(_fromUtf8("lblNotificacionGrupoFamiliar"))
        self.gridLayout_12.addWidget(self.lblNotificacionGrupoFamiliar, 0, 0, 1, 1)
        self.tabWidget1.addTab(self.intgrantes, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Datos_Familia, _fromUtf8(""))
        self.Vivienda = QtGui.QWidget()
        self.Vivienda.setObjectName(_fromUtf8("Vivienda"))
        self.label_20 = QtGui.QLabel(self.Vivienda)
        self.label_20.setGeometry(QtCore.QRect(20, 10, 641, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Caracteristica de la Vivienda", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.layoutWidget = QtGui.QWidget(self.Vivienda)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_9 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_9.setMargin(0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.btnGuardarVivienda = QtGui.QPushButton(self.Vivienda)
        self.btnGuardarVivienda.setGeometry(QtCore.QRect(180, 470, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardarVivienda.setFont(font)
        self.btnGuardarVivienda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuardarVivienda.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnGuardarVivienda.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGuardarVivienda.setObjectName(_fromUtf8("btnGuardarVivienda"))
        self.btnLimpiarVivienda = QtGui.QPushButton(self.Vivienda)
        self.btnLimpiarVivienda.setGeometry(QtCore.QRect(410, 470, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnLimpiarVivienda.setFont(font)
        self.btnLimpiarVivienda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLimpiarVivienda.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnLimpiarVivienda.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLimpiarVivienda.setObjectName(_fromUtf8("btnLimpiarVivienda"))
        self.btnModificarVivienda = QtGui.QPushButton(self.Vivienda)
        self.btnModificarVivienda.setEnabled(True)
        self.btnModificarVivienda.setGeometry(QtCore.QRect(670, 470, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModificarVivienda.setFont(font)
        self.btnModificarVivienda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarVivienda.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnModificarVivienda.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarVivienda.setObjectName(_fromUtf8("btnModificarVivienda"))
        self.lblNotificacionVivienda = QtGui.QLabel(self.Vivienda)
        self.lblNotificacionVivienda.setGeometry(QtCore.QRect(20, 40, 871, 41))
        self.lblNotificacionVivienda.setStyleSheet(_fromUtf8("border: 1px solid Yellow;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #FFFF80, stop: 0.08 #FAFFD8,\n"
"stop: 0.39999 #FEFFE5, stop: 0.4 #FEFFE5,\n"
"stop: 0.9 #FAFFD8, stop: 1 #fff);\n"
"\n"
""))
        self.lblNotificacionVivienda.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotificacionVivienda.setObjectName(_fromUtf8("lblNotificacionVivienda"))
        self.frame_2 = QtGui.QFrame(self.Vivienda)
        self.frame_2.setGeometry(QtCore.QRect(20, 90, 881, 321))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.cmbTipoVivienda = QtGui.QComboBox(self.frame_2)
        self.cmbTipoVivienda.setGeometry(QtCore.QRect(10, 30, 144, 27))
        self.cmbTipoVivienda.setObjectName(_fromUtf8("cmbTipoVivienda"))
        self.cmbTipoVivienda.addItem(_fromUtf8(""))
        self.cmbTipoVivienda.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Casa", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoVivienda.addItem(_fromUtf8(""))
        self.cmbTipoVivienda.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Apartamento", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoVivienda.addItem(_fromUtf8(""))
        self.cmbTipoVivienda.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Rancho", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoVivienda.addItem(_fromUtf8(""))
        self.cmbTipoVivienda.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Quinta", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTipoVivienda.addItem(_fromUtf8(""))
        self.cmbTipoVivienda.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "Otra", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25 = QtGui.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(650, 10, 281, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Materiales de la Pared", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.cmbTenencia = QtGui.QComboBox(self.frame_2)
        self.cmbTenencia.setGeometry(QtCore.QRect(440, 30, 144, 27))
        self.cmbTenencia.setObjectName(_fromUtf8("cmbTenencia"))
        self.cmbTenencia.addItem(_fromUtf8(""))
        self.cmbTenencia.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Propia", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTenencia.addItem(_fromUtf8(""))
        self.cmbTenencia.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Alquilado", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTenencia.addItem(_fromUtf8(""))
        self.cmbTenencia.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Opcion a compra", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTenencia.addItem(_fromUtf8(""))
        self.cmbTenencia.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otra", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21 = QtGui.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 141, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Tipo de Vivienda", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(220, 10, 291, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Estado de la Vivienda", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(440, 10, 221, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Tenencia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.cmbEstadoVivienda = QtGui.QComboBox(self.frame_2)
        self.cmbEstadoVivienda.setGeometry(QtCore.QRect(220, 30, 161, 27))
        self.cmbEstadoVivienda.setObjectName(_fromUtf8("cmbEstadoVivienda"))
        self.cmbEstadoVivienda.addItem(_fromUtf8(""))
        self.cmbEstadoVivienda.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bueno", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstadoVivienda.addItem(_fromUtf8(""))
        self.cmbEstadoVivienda.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Regular", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstadoVivienda.addItem(_fromUtf8(""))
        self.cmbEstadoVivienda.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Malo", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbEstadoVivienda.addItem(_fromUtf8(""))
        self.cmbEstadoVivienda.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otro", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPared = QtGui.QComboBox(self.frame_2)
        self.cmbMaterialPared.setGeometry(QtCore.QRect(650, 30, 220, 27))
        self.cmbMaterialPared.setObjectName(_fromUtf8("cmbMaterialPared"))
        self.cmbMaterialPared.addItem(_fromUtf8(""))
        self.cmbMaterialPared.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bloque Friso, Bloque Sin Friso", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPared.addItem(_fromUtf8(""))
        self.cmbMaterialPared.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Bahareque, Cana, Palma", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPared.addItem(_fromUtf8(""))
        self.cmbMaterialPared.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Ladrillo, Zinc", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPared.addItem(_fromUtf8(""))
        self.cmbMaterialPared.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otro", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPiso = QtGui.QComboBox(self.frame_2)
        self.cmbMaterialPiso.setGeometry(QtCore.QRect(10, 100, 141, 27))
        self.cmbMaterialPiso.setObjectName(_fromUtf8("cmbMaterialPiso"))
        self.cmbMaterialPiso.addItem(_fromUtf8(""))
        self.cmbMaterialPiso.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Cemento", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPiso.addItem(_fromUtf8(""))
        self.cmbMaterialPiso.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Granito", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPiso.addItem(_fromUtf8(""))
        self.cmbMaterialPiso.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Ceramica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialPiso.addItem(_fromUtf8(""))
        self.cmbMaterialPiso.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28 = QtGui.QLabel(self.frame_2)
        self.label_28.setGeometry(QtCore.QRect(440, 80, 281, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Uso de la vivienda", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.cmbMaterialTecho = QtGui.QComboBox(self.frame_2)
        self.cmbMaterialTecho.setGeometry(QtCore.QRect(220, 100, 161, 27))
        self.cmbMaterialTecho.setObjectName(_fromUtf8("cmbMaterialTecho"))
        self.cmbMaterialTecho.addItem(_fromUtf8(""))
        self.cmbMaterialTecho.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Platabanda", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialTecho.addItem(_fromUtf8(""))
        self.cmbMaterialTecho.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Tejas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialTecho.addItem(_fromUtf8(""))
        self.cmbMaterialTecho.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Abesto", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMaterialTecho.addItem(_fromUtf8(""))
        self.cmbMaterialTecho.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otro", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbUsoVivienda = QtGui.QComboBox(self.frame_2)
        self.cmbUsoVivienda.setGeometry(QtCore.QRect(440, 100, 141, 27))
        self.cmbUsoVivienda.setObjectName(_fromUtf8("cmbUsoVivienda"))
        self.cmbUsoVivienda.addItem(_fromUtf8(""))
        self.cmbUsoVivienda.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Familiar", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbUsoVivienda.addItem(_fromUtf8(""))
        self.cmbUsoVivienda.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Comercial", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbUsoVivienda.addItem(_fromUtf8(""))
        self.cmbUsoVivienda.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Familiar Comercial", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbUsoVivienda.addItem(_fromUtf8(""))
        self.cmbUsoVivienda.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24 = QtGui.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(10, 80, 261, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Materiales del Piso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_27 = QtGui.QLabel(self.frame_2)
        self.label_27.setGeometry(QtCore.QRect(650, 80, 281, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Indique N° de espacios", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_26 = QtGui.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(220, 80, 291, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Materiales del techo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.layoutWidget1 = QtGui.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(650, 110, 200, 128))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_32 = QtGui.QLabel(self.layoutWidget1)
        self.label_32.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Baños", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_6.addWidget(self.label_32, 2, 1, 1, 1)
        self.cmbCocina = QtGui.QComboBox(self.layoutWidget1)
        self.cmbCocina.setObjectName(_fromUtf8("cmbCocina"))
        self.cmbCocina.addItem(_fromUtf8(""))
        self.cmbCocina.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCocina.addItem(_fromUtf8(""))
        self.cmbCocina.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCocina.addItem(_fromUtf8(""))
        self.cmbCocina.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCocina.addItem(_fromUtf8(""))
        self.cmbCocina.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCocina.addItem(_fromUtf8(""))
        self.cmbCocina.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCocina.addItem(_fromUtf8(""))
        self.cmbCocina.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbCocina.addItem(_fromUtf8(""))
        self.cmbCocina.setItemText(6, QtGui.QApplication.translate("Censo_socioeconomico", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_6.addWidget(self.cmbCocina, 3, 2, 1, 1)
        self.label_30 = QtGui.QLabel(self.layoutWidget1)
        self.label_30.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Habitaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_6.addWidget(self.label_30, 0, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.layoutWidget1)
        self.label_33.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Cocina", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_6.addWidget(self.label_33, 3, 1, 1, 1)
        self.cmbBanos = QtGui.QComboBox(self.layoutWidget1)
        self.cmbBanos.setObjectName(_fromUtf8("cmbBanos"))
        self.cmbBanos.addItem(_fromUtf8(""))
        self.cmbBanos.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBanos.addItem(_fromUtf8(""))
        self.cmbBanos.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBanos.addItem(_fromUtf8(""))
        self.cmbBanos.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBanos.addItem(_fromUtf8(""))
        self.cmbBanos.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBanos.addItem(_fromUtf8(""))
        self.cmbBanos.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbBanos.addItem(_fromUtf8(""))
        self.cmbBanos.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_6.addWidget(self.cmbBanos, 2, 2, 1, 1)
        self.cmbSalaComedor = QtGui.QComboBox(self.layoutWidget1)
        self.cmbSalaComedor.setObjectName(_fromUtf8("cmbSalaComedor"))
        self.cmbSalaComedor.addItem(_fromUtf8(""))
        self.cmbSalaComedor.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSalaComedor.addItem(_fromUtf8(""))
        self.cmbSalaComedor.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSalaComedor.addItem(_fromUtf8(""))
        self.cmbSalaComedor.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSalaComedor.addItem(_fromUtf8(""))
        self.cmbSalaComedor.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSalaComedor.addItem(_fromUtf8(""))
        self.cmbSalaComedor.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSalaComedor.addItem(_fromUtf8(""))
        self.cmbSalaComedor.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_6.addWidget(self.cmbSalaComedor, 1, 2, 1, 1)
        self.label_31 = QtGui.QLabel(self.layoutWidget1)
        self.label_31.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Sala, Comedor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_6.addWidget(self.label_31, 1, 1, 1, 1)
        self.cmbHabitaciones = QtGui.QComboBox(self.layoutWidget1)
        self.cmbHabitaciones.setObjectName(_fromUtf8("cmbHabitaciones"))
        self.cmbHabitaciones.addItem(_fromUtf8(""))
        self.cmbHabitaciones.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbHabitaciones.addItem(_fromUtf8(""))
        self.cmbHabitaciones.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbHabitaciones.addItem(_fromUtf8(""))
        self.cmbHabitaciones.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbHabitaciones.addItem(_fromUtf8(""))
        self.cmbHabitaciones.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbHabitaciones.addItem(_fromUtf8(""))
        self.cmbHabitaciones.setItemText(4, QtGui.QApplication.translate("Censo_socioeconomico", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbHabitaciones.addItem(_fromUtf8(""))
        self.cmbHabitaciones.setItemText(5, QtGui.QApplication.translate("Censo_socioeconomico", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_6.addWidget(self.cmbHabitaciones, 0, 2, 1, 1)
        self.chkJardineria = QtGui.QCheckBox(self.frame_2)
        self.chkJardineria.setGeometry(QtCore.QRect(390, 290, 101, 22))
        self.chkJardineria.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Jardineria", None, QtGui.QApplication.UnicodeUTF8))
        self.chkJardineria.setObjectName(_fromUtf8("chkJardineria"))
        self.chkTecho = QtGui.QCheckBox(self.frame_2)
        self.chkTecho.setGeometry(QtCore.QRect(390, 170, 111, 22))
        self.chkTecho.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Techo", None, QtGui.QApplication.UnicodeUTF8))
        self.chkTecho.setObjectName(_fromUtf8("chkTecho"))
        self.chkPared = QtGui.QCheckBox(self.frame_2)
        self.chkPared.setGeometry(QtCore.QRect(390, 210, 111, 22))
        self.chkPared.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Pared", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPared.setObjectName(_fromUtf8("chkPared"))
        self.chkAmpliar = QtGui.QCheckBox(self.frame_2)
        self.chkAmpliar.setGeometry(QtCore.QRect(390, 250, 111, 22))
        self.chkAmpliar.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Ampliar", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAmpliar.setObjectName(_fromUtf8("chkAmpliar"))
        self.chkCocina = QtGui.QCheckBox(self.frame_2)
        self.chkCocina.setGeometry(QtCore.QRect(390, 270, 101, 22))
        self.chkCocina.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Cocina", None, QtGui.QApplication.UnicodeUTF8))
        self.chkCocina.setObjectName(_fromUtf8("chkCocina"))
        self.chkFriso = QtGui.QCheckBox(self.frame_2)
        self.chkFriso.setGeometry(QtCore.QRect(390, 150, 131, 22))
        self.chkFriso.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Friso", None, QtGui.QApplication.UnicodeUTF8))
        self.chkFriso.setObjectName(_fromUtf8("chkFriso"))
        self.chkPintura = QtGui.QCheckBox(self.frame_2)
        self.chkPintura.setGeometry(QtCore.QRect(390, 230, 111, 22))
        self.chkPintura.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Pintura", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPintura.setObjectName(_fromUtf8("chkPintura"))
        self.chkPiso = QtGui.QCheckBox(self.frame_2)
        self.chkPiso.setGeometry(QtCore.QRect(390, 190, 111, 22))
        self.chkPiso.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Piso", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPiso.setObjectName(_fromUtf8("chkPiso"))
        self.label_34 = QtGui.QLabel(self.frame_2)
        self.label_34.setGeometry(QtCore.QRect(10, 150, 321, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Que le gustaria Mejorar de su Vivienda:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.line_5 = QtGui.QFrame(self.frame_2)
        self.line_5.setGeometry(QtCore.QRect(630, 110, 21, 131))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.frame_2)
        self.line_6.setGeometry(QtCore.QRect(490, 150, 20, 161))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_2 = QtGui.QFrame(self.Vivienda)
        self.line_2.setGeometry(QtCore.QRect(90, 440, 741, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget.addTab(self.Vivienda, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame_7 = QtGui.QFrame(self.tab)
        self.frame_7.setGeometry(QtCore.QRect(40, 70, 761, 141))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.label_6 = QtGui.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 601, 17))
        self.label_6.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600;\">¿Poseen los niños de su grupo familiar todas las vacunas ?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.rbtNoTiene = QtGui.QRadioButton(self.frame_7)
        self.rbtNoTiene.setGeometry(QtCore.QRect(130, 40, 261, 22))
        self.rbtNoTiene.setText(QtGui.QApplication.translate("Censo_socioeconomico", "No tienen las vacunas completas", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtNoTiene.setChecked(True)
        self.rbtNoTiene.setObjectName(_fromUtf8("rbtNoTiene"))
        self.rbtSiTienen = QtGui.QRadioButton(self.frame_7)
        self.rbtSiTienen.setGeometry(QtCore.QRect(130, 70, 291, 22))
        self.rbtSiTienen.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Si tienen todas su vacunas", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtSiTienen.setObjectName(_fromUtf8("rbtSiTienen"))
        self.chbAll_ninos = QtGui.QCheckBox(self.frame_7)
        self.chbAll_ninos.setEnabled(False)
        self.chbAll_ninos.setGeometry(QtCore.QRect(430, 70, 191, 22))
        self.chbAll_ninos.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Todos los niños", None, QtGui.QApplication.UnicodeUTF8))
        self.chbAll_ninos.setChecked(True)
        self.chbAll_ninos.setObjectName(_fromUtf8("chbAll_ninos"))
        self.chbMenoresSeis = QtGui.QCheckBox(self.frame_7)
        self.chbMenoresSeis.setEnabled(False)
        self.chbMenoresSeis.setGeometry(QtCore.QRect(430, 100, 201, 22))
        self.chbMenoresSeis.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Menores de 6 años", None, QtGui.QApplication.UnicodeUTF8))
        self.chbMenoresSeis.setObjectName(_fromUtf8("chbMenoresSeis"))
        self.line_4 = QtGui.QFrame(self.frame_7)
        self.line_4.setGeometry(QtCore.QRect(410, 60, 3, 61))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.lblNotificacionSalud = QtGui.QLabel(self.tab)
        self.lblNotificacionSalud.setGeometry(QtCore.QRect(40, 10, 761, 31))
        self.lblNotificacionSalud.setStyleSheet(_fromUtf8("border: 1px solid Yellow;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #FFFF80, stop: 0.08 #FAFFD8,\n"
"stop: 0.39999 #FEFFE5, stop: 0.4 #FEFFE5,\n"
"stop: 0.9 #FAFFD8, stop: 1 #fff);\n"
"\n"
""))
        self.lblNotificacionSalud.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotificacionSalud.setObjectName(_fromUtf8("lblNotificacionSalud"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(300, 40, 311, 21))
        self.label_8.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; color:#00007f;\">Información de Vacunas</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.frame_8 = QtGui.QFrame(self.tab)
        self.frame_8.setEnabled(False)
        self.frame_8.setGeometry(QtCore.QRect(40, 220, 761, 211))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.label_9 = QtGui.QLabel(self.frame_8)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 601, 17))
        self.label_9.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600;\">De ser afirmativa su respuesta, indique que vacunas tienen:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.checkBox_44 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_44.setGeometry(QtCore.QRect(352, 66, 112, 22))
        self.checkBox_44.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Leucemia", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_44.setObjectName(_fromUtf8("checkBox_44"))
        self.checkBox_31 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_31.setGeometry(QtCore.QRect(470, 122, 237, 22))
        self.checkBox_31.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Alcoholismo", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_31.setObjectName(_fromUtf8("checkBox_31"))
        self.checkBox_46 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_46.setGeometry(QtCore.QRect(11, 150, 209, 22))
        self.checkBox_46.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Enfermedades resperatorias", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_46.setObjectName(_fromUtf8("checkBox_46"))
        self.checkBox_47 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_47.setGeometry(QtCore.QRect(470, 94, 237, 22))
        self.checkBox_47.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Diabetes", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_47.setObjectName(_fromUtf8("checkBox_47"))
        self.checkBox_48 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_48.setGeometry(QtCore.QRect(470, 66, 237, 22))
        self.checkBox_48.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Asma", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_48.setObjectName(_fromUtf8("checkBox_48"))
        self.checkBox_49 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_49.setGeometry(QtCore.QRect(352, 38, 112, 22))
        self.checkBox_49.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Cáncer", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_49.setObjectName(_fromUtf8("checkBox_49"))
        self.checkBox_50 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_50.setGeometry(QtCore.QRect(226, 66, 120, 22))
        self.checkBox_50.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Tensión Alta", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_50.setObjectName(_fromUtf8("checkBox_50"))
        self.checkBox_51 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_51.setGeometry(QtCore.QRect(470, 38, 237, 22))
        self.checkBox_51.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Sustancias sicotropicas (Drogas)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_51.setObjectName(_fromUtf8("checkBox_51"))
        self.checkBox_52 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_52.setGeometry(QtCore.QRect(11, 38, 209, 22))
        self.checkBox_52.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Desnutrición ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_52.setObjectName(_fromUtf8("checkBox_52"))
        self.checkBox_53 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_53.setGeometry(QtCore.QRect(11, 94, 209, 22))
        self.checkBox_53.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Deficultades de aprendizaje", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_53.setObjectName(_fromUtf8("checkBox_53"))
        self.checkBox_54 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_54.setGeometry(QtCore.QRect(226, 178, 120, 22))
        self.checkBox_54.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Alergias", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_54.setObjectName(_fromUtf8("checkBox_54"))
        self.checkBox_55 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_55.setGeometry(QtCore.QRect(352, 178, 112, 22))
        self.checkBox_55.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Covulciones", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_55.setObjectName(_fromUtf8("checkBox_55"))
        self.checkBox_56 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_56.setGeometry(QtCore.QRect(11, 66, 209, 22))
        self.checkBox_56.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Sindrome de Down", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_56.setObjectName(_fromUtf8("checkBox_56"))
        self.checkBox_57 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_57.setGeometry(QtCore.QRect(226, 122, 120, 22))
        self.checkBox_57.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Hernias", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_57.setObjectName(_fromUtf8("checkBox_57"))
        self.checkBox_58 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_58.setGeometry(QtCore.QRect(352, 150, 112, 22))
        self.checkBox_58.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Discapasidad", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_58.setObjectName(_fromUtf8("checkBox_58"))
        self.checkBox_59 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_59.setGeometry(QtCore.QRect(226, 150, 120, 22))
        self.checkBox_59.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Parasitosis", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_59.setObjectName(_fromUtf8("checkBox_59"))
        self.checkBox_60 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_60.setGeometry(QtCore.QRect(226, 38, 120, 22))
        self.checkBox_60.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Meningitis", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_60.setObjectName(_fromUtf8("checkBox_60"))
        self.checkBox_61 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_61.setGeometry(QtCore.QRect(11, 178, 209, 22))
        self.checkBox_61.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Infartos", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_61.setObjectName(_fromUtf8("checkBox_61"))
        self.checkBox_62 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_62.setGeometry(QtCore.QRect(11, 122, 209, 22))
        self.checkBox_62.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Paralisis infantil", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_62.setObjectName(_fromUtf8("checkBox_62"))
        self.checkBox_63 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_63.setGeometry(QtCore.QRect(352, 122, 112, 22))
        self.checkBox_63.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Epilesia", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_63.setObjectName(_fromUtf8("checkBox_63"))
        self.checkBox_64 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_64.setGeometry(QtCore.QRect(226, 94, 120, 22))
        self.checkBox_64.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Labio Leporino", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_64.setObjectName(_fromUtf8("checkBox_64"))
        self.checkBox_65 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_65.setGeometry(QtCore.QRect(352, 94, 112, 22))
        self.checkBox_65.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Hipertesión", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_65.setObjectName(_fromUtf8("checkBox_65"))
        self.checkBox_66 = QtGui.QCheckBox(self.frame_8)
        self.checkBox_66.setGeometry(QtCore.QRect(470, 150, 237, 22))
        self.checkBox_66.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Otras", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_66.setObjectName(_fromUtf8("checkBox_66"))
        self.frame_9 = QtGui.QFrame(self.tab)
        self.frame_9.setGeometry(QtCore.QRect(40, 440, 761, 111))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.label_10 = QtGui.QLabel(self.frame_9)
        self.label_10.setGeometry(QtCore.QRect(60, 10, 601, 17))
        self.label_10.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600;\">Algún miembro del grupo familiar requiere intervención quirurgica</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.rbtSiOperacion = QtGui.QRadioButton(self.frame_9)
        self.rbtSiOperacion.setGeometry(QtCore.QRect(30, 50, 105, 22))
        self.rbtSiOperacion.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Si", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtSiOperacion.setObjectName(_fromUtf8("rbtSiOperacion"))
        self.rbtNoOperacion = QtGui.QRadioButton(self.frame_9)
        self.rbtNoOperacion.setGeometry(QtCore.QRect(30, 80, 105, 22))
        self.rbtNoOperacion.setText(QtGui.QApplication.translate("Censo_socioeconomico", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtNoOperacion.setChecked(True)
        self.rbtNoOperacion.setObjectName(_fromUtf8("rbtNoOperacion"))
        self.txtCuantos = QtGui.QLineEdit(self.frame_9)
        self.txtCuantos.setEnabled(False)
        self.txtCuantos.setGeometry(QtCore.QRect(180, 50, 51, 27))
        self.txtCuantos.setObjectName(_fromUtf8("txtCuantos"))
        self.label_38 = QtGui.QLabel(self.frame_9)
        self.label_38.setGeometry(QtCore.QRect(110, 50, 59, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_38.setFont(font)
        self.label_38.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Cuantos</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(self.frame_9)
        self.label_39.setGeometry(QtCore.QRect(270, 50, 161, 17))
        self.label_39.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Tipo de Operación</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.txtTipoOperacion = QtGui.QLineEdit(self.frame_9)
        self.txtTipoOperacion.setEnabled(False)
        self.txtTipoOperacion.setGeometry(QtCore.QRect(410, 50, 331, 27))
        self.txtTipoOperacion.setObjectName(_fromUtf8("txtTipoOperacion"))
        self.frame_10 = QtGui.QFrame(self.tab)
        self.frame_10.setGeometry(QtCore.QRect(40, 560, 761, 41))
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.label_40 = QtGui.QLabel(self.frame_10)
        self.label_40.setGeometry(QtCore.QRect(20, 10, 331, 17))
        self.label_40.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:8pt; font-weight:600;\">¿Existe en el grupo familiar alguna persona con discapacidad?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.rbtSiDiscapacidad = QtGui.QRadioButton(self.frame_10)
        self.rbtSiDiscapacidad.setGeometry(QtCore.QRect(360, 10, 105, 22))
        self.rbtSiDiscapacidad.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Si", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtSiDiscapacidad.setObjectName(_fromUtf8("rbtSiDiscapacidad"))
        self.rbtNoDiscapacidad = QtGui.QRadioButton(self.frame_10)
        self.rbtNoDiscapacidad.setGeometry(QtCore.QRect(470, 10, 105, 22))
        self.rbtNoDiscapacidad.setText(QtGui.QApplication.translate("Censo_socioeconomico", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.rbtNoDiscapacidad.setChecked(True)
        self.rbtNoDiscapacidad.setObjectName(_fromUtf8("rbtNoDiscapacidad"))
        self.line_11 = QtGui.QFrame(self.tab)
        self.line_11.setGeometry(QtCore.QRect(830, 80, 20, 581))
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.btnModificarSalud_2 = QtGui.QPushButton(self.tab)
        self.btnModificarSalud_2.setEnabled(True)
        self.btnModificarSalud_2.setGeometry(QtCore.QRect(870, 180, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModificarSalud_2.setFont(font)
        self.btnModificarSalud_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarSalud_2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnModificarSalud_2.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarSalud_2.setObjectName(_fromUtf8("btnModificarSalud_2"))
        self.btnLimpiarSalud_2 = QtGui.QPushButton(self.tab)
        self.btnLimpiarSalud_2.setGeometry(QtCore.QRect(870, 80, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnLimpiarSalud_2.setFont(font)
        self.btnLimpiarSalud_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLimpiarSalud_2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnLimpiarSalud_2.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLimpiarSalud_2.setObjectName(_fromUtf8("btnLimpiarSalud_2"))
        self.btnGuardarSalud_2 = QtGui.QPushButton(self.tab)
        self.btnGuardarSalud_2.setGeometry(QtCore.QRect(870, 130, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardarSalud_2.setFont(font)
        self.btnGuardarSalud_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuardarSalud_2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnGuardarSalud_2.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGuardarSalud_2.setObjectName(_fromUtf8("btnGuardarSalud_2"))
        self.line_12 = QtGui.QFrame(self.tab)
        self.line_12.setGeometry(QtCore.QRect(850, 230, 121, 20))
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.bienestar = QtGui.QWidget()
        self.bienestar.setObjectName(_fromUtf8("bienestar"))
        self.label_7 = QtGui.QLabel(self.bienestar)
        self.label_7.setGeometry(QtCore.QRect(390, 50, 171, 21))
        self.label_7.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; color:#00007f;\">Servicios Básicos</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.layoutWidget_4 = QtGui.QWidget(self.bienestar)
        self.layoutWidget_4.setGeometry(QtCore.QRect(30, 80, 395, 207))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.gridLayout_29 = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout_29.setMargin(0)
        self.gridLayout_29.setObjectName(_fromUtf8("gridLayout_29"))
        self.label_54 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Aguas Blancas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.gridLayout_29.addWidget(self.label_54, 0, 1, 1, 1)
        self.cmbAguasBlancas_2 = QtGui.QComboBox(self.layoutWidget_4)
        self.cmbAguasBlancas_2.setObjectName(_fromUtf8("cmbAguasBlancas_2"))
        self.cmbAguasBlancas_2.addItem(_fromUtf8(""))
        self.cmbAguasBlancas_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Acueducto", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAguasBlancas_2.addItem(_fromUtf8(""))
        self.cmbAguasBlancas_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Pila Publica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAguasBlancas_2.addItem(_fromUtf8(""))
        self.cmbAguasBlancas_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Camion Sisterna", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAguasBlancas_2.addItem(_fromUtf8(""))
        self.cmbAguasBlancas_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_29.addWidget(self.cmbAguasBlancas_2, 0, 2, 1, 1)
        self.label_55 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Aguas Servidas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.gridLayout_29.addWidget(self.label_55, 1, 1, 1, 1)
        self.cmbAguasServidas_2 = QtGui.QComboBox(self.layoutWidget_4)
        self.cmbAguasServidas_2.setObjectName(_fromUtf8("cmbAguasServidas_2"))
        self.cmbAguasServidas_2.addItem(_fromUtf8(""))
        self.cmbAguasServidas_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Cloacas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAguasServidas_2.addItem(_fromUtf8(""))
        self.cmbAguasServidas_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Letrinas", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAguasServidas_2.addItem(_fromUtf8(""))
        self.cmbAguasServidas_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Pozo Septico", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAguasServidas_2.addItem(_fromUtf8(""))
        self.cmbAguasServidas_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_29.addWidget(self.cmbAguasServidas_2, 1, 2, 1, 1)
        self.label_56 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Gas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.gridLayout_29.addWidget(self.label_56, 2, 1, 1, 1)
        self.cmbGas_2 = QtGui.QComboBox(self.layoutWidget_4)
        self.cmbGas_2.setObjectName(_fromUtf8("cmbGas_2"))
        self.cmbGas_2.addItem(_fromUtf8(""))
        self.cmbGas_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Bombona ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGas_2.addItem(_fromUtf8(""))
        self.cmbGas_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Tuberia", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGas_2.addItem(_fromUtf8(""))
        self.cmbGas_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "No Posee", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbGas_2.addItem(_fromUtf8(""))
        self.cmbGas_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_29.addWidget(self.cmbGas_2, 2, 2, 1, 1)
        self.label_57 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Sistema Eléctrico", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.gridLayout_29.addWidget(self.label_57, 3, 1, 1, 1)
        self.cmbSistemaElectrico_2 = QtGui.QComboBox(self.layoutWidget_4)
        self.cmbSistemaElectrico_2.setObjectName(_fromUtf8("cmbSistemaElectrico_2"))
        self.cmbSistemaElectrico_2.addItem(_fromUtf8(""))
        self.cmbSistemaElectrico_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Electrificado Publico", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSistemaElectrico_2.addItem(_fromUtf8(""))
        self.cmbSistemaElectrico_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Planta Electrica", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSistemaElectrico_2.addItem(_fromUtf8(""))
        self.cmbSistemaElectrico_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Medidor", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbSistemaElectrico_2.addItem(_fromUtf8(""))
        self.cmbSistemaElectrico_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_29.addWidget(self.cmbSistemaElectrico_2, 3, 2, 1, 1)
        self.label_58 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Recolección de Basura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.gridLayout_29.addWidget(self.label_58, 4, 1, 1, 1)
        self.cmbRecoleccionBasura_2 = QtGui.QComboBox(self.layoutWidget_4)
        self.cmbRecoleccionBasura_2.setObjectName(_fromUtf8("cmbRecoleccionBasura_2"))
        self.cmbRecoleccionBasura_2.addItem(_fromUtf8(""))
        self.cmbRecoleccionBasura_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Aseo Urbano", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRecoleccionBasura_2.addItem(_fromUtf8(""))
        self.cmbRecoleccionBasura_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Container", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRecoleccionBasura_2.addItem(_fromUtf8(""))
        self.cmbRecoleccionBasura_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Camion", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbRecoleccionBasura_2.addItem(_fromUtf8(""))
        self.cmbRecoleccionBasura_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_29.addWidget(self.cmbRecoleccionBasura_2, 4, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem5, 2, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_29.addItem(spacerItem6, 5, 1, 1, 1)
        self.line_7 = QtGui.QFrame(self.bienestar)
        self.line_7.setGeometry(QtCore.QRect(450, 100, 20, 171))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.label_59 = QtGui.QLabel(self.bienestar)
        self.label_59.setGeometry(QtCore.QRect(482, 130, 172, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Transporte", None, QtGui.QApplication.UnicodeUTF8))
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.cmbTelefonia_2 = QtGui.QComboBox(self.bienestar)
        self.cmbTelefonia_2.setGeometry(QtCore.QRect(720, 97, 111, 27))
        self.cmbTelefonia_2.setObjectName(_fromUtf8("cmbTelefonia_2"))
        self.cmbTelefonia_2.addItem(_fromUtf8(""))
        self.cmbTelefonia_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Domiciliaria", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTelefonia_2.addItem(_fromUtf8(""))
        self.cmbTelefonia_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "No Posee", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTelefonia_2.addItem(_fromUtf8(""))
        self.cmbTelefonia_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Prepago", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTelefonia_2.addItem(_fromUtf8(""))
        self.cmbTelefonia_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMecanismosInformacion_2 = QtGui.QComboBox(self.bienestar)
        self.cmbMecanismosInformacion_2.setGeometry(QtCore.QRect(720, 163, 111, 27))
        self.cmbMecanismosInformacion_2.setObjectName(_fromUtf8("cmbMecanismosInformacion_2"))
        self.cmbMecanismosInformacion_2.addItem(_fromUtf8(""))
        self.cmbMecanismosInformacion_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Television", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMecanismosInformacion_2.addItem(_fromUtf8(""))
        self.cmbMecanismosInformacion_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Internet", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMecanismosInformacion_2.addItem(_fromUtf8(""))
        self.cmbMecanismosInformacion_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Radio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbMecanismosInformacion_2.addItem(_fromUtf8(""))
        self.cmbMecanismosInformacion_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Prensa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60 = QtGui.QLabel(self.bienestar)
        self.label_60.setGeometry(QtCore.QRect(482, 97, 172, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Telefonía", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.label_61 = QtGui.QLabel(self.bienestar)
        self.label_61.setGeometry(QtCore.QRect(482, 163, 241, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Mecanismo de información", None, QtGui.QApplication.UnicodeUTF8))
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.cmbTransporte_2 = QtGui.QComboBox(self.bienestar)
        self.cmbTransporte_2.setGeometry(QtCore.QRect(720, 130, 111, 27))
        self.cmbTransporte_2.setObjectName(_fromUtf8("cmbTransporte_2"))
        self.cmbTransporte_2.addItem(_fromUtf8(""))
        self.cmbTransporte_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "Publico", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTransporte_2.addItem(_fromUtf8(""))
        self.cmbTransporte_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Propio", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTransporte_2.addItem(_fromUtf8(""))
        self.cmbTransporte_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Taxi", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTransporte_2.addItem(_fromUtf8(""))
        self.cmbTransporte_2.setItemText(3, QtGui.QApplication.translate("Censo_socioeconomico", "Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62 = QtGui.QLabel(self.bienestar)
        self.label_62.setGeometry(QtCore.QRect(30, 290, 819, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Ṕarticipación Comunitaria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.layoutWidget_5 = QtGui.QWidget(self.bienestar)
        self.layoutWidget_5.setGeometry(QtCore.QRect(30, 310, 891, 124))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.gridLayout_30 = QtGui.QGridLayout(self.layoutWidget_5)
        self.gridLayout_30.setMargin(0)
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        self.label_63 = QtGui.QLabel(self.layoutWidget_5)
        self.label_63.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Existe organización comunitarios", None, QtGui.QApplication.UnicodeUTF8))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.gridLayout_30.addWidget(self.label_63, 0, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem7, 1, 0, 1, 1)
        self.label_64 = QtGui.QLabel(self.layoutWidget_5)
        self.label_64.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Participa el Jefe de Familia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.gridLayout_30.addWidget(self.label_64, 1, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem8, 1, 4, 1, 1)
        self.label_65 = QtGui.QLabel(self.layoutWidget_5)
        self.label_65.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Participa un miembro de la familia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.gridLayout_30.addWidget(self.label_65, 2, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(17, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_30.addItem(spacerItem9, 3, 3, 1, 1)
        self.cmbPaticipaJefe_2 = QtGui.QComboBox(self.layoutWidget_5)
        self.cmbPaticipaJefe_2.setObjectName(_fromUtf8("cmbPaticipaJefe_2"))
        self.cmbPaticipaJefe_2.addItem(_fromUtf8(""))
        self.cmbPaticipaJefe_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "No Participa", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPaticipaJefe_2.addItem(_fromUtf8(""))
        self.cmbPaticipaJefe_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "En Asociaciones de Vecinos", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPaticipaJefe_2.addItem(_fromUtf8(""))
        self.cmbPaticipaJefe_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "En Consejos Comunales", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_30.addWidget(self.cmbPaticipaJefe_2, 1, 2, 1, 1)
        self.cmbParticipaMiembro_2 = QtGui.QComboBox(self.layoutWidget_5)
        self.cmbParticipaMiembro_2.setObjectName(_fromUtf8("cmbParticipaMiembro_2"))
        self.cmbParticipaMiembro_2.addItem(_fromUtf8(""))
        self.cmbParticipaMiembro_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "No Participan", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbParticipaMiembro_2.addItem(_fromUtf8(""))
        self.cmbParticipaMiembro_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "En Asociaciones de Vecinos", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbParticipaMiembro_2.addItem(_fromUtf8(""))
        self.cmbParticipaMiembro_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "En Consejos Comunales", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_30.addWidget(self.cmbParticipaMiembro_2, 2, 2, 1, 1)
        self.cmbOrgComunitaria_2 = QtGui.QComboBox(self.layoutWidget_5)
        self.cmbOrgComunitaria_2.setObjectName(_fromUtf8("cmbOrgComunitaria_2"))
        self.cmbOrgComunitaria_2.addItem(_fromUtf8(""))
        self.cmbOrgComunitaria_2.setItemText(0, QtGui.QApplication.translate("Censo_socioeconomico", "No Existe", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOrgComunitaria_2.addItem(_fromUtf8(""))
        self.cmbOrgComunitaria_2.setItemText(1, QtGui.QApplication.translate("Censo_socioeconomico", "Asociacion de Vecinos", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOrgComunitaria_2.addItem(_fromUtf8(""))
        self.cmbOrgComunitaria_2.setItemText(2, QtGui.QApplication.translate("Censo_socioeconomico", "Consejo Comunal", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_30.addWidget(self.cmbOrgComunitaria_2, 0, 2, 1, 1)
        self.btnGuardarBienestar_2 = QtGui.QPushButton(self.bienestar)
        self.btnGuardarBienestar_2.setGeometry(QtCore.QRect(870, 20, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardarBienestar_2.setFont(font)
        self.btnGuardarBienestar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuardarBienestar_2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnGuardarBienestar_2.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGuardarBienestar_2.setObjectName(_fromUtf8("btnGuardarBienestar_2"))
        self.btnLimpiarBienestar_2 = QtGui.QPushButton(self.bienestar)
        self.btnLimpiarBienestar_2.setGeometry(QtCore.QRect(870, 80, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnLimpiarBienestar_2.setFont(font)
        self.btnLimpiarBienestar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLimpiarBienestar_2.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnLimpiarBienestar_2.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLimpiarBienestar_2.setObjectName(_fromUtf8("btnLimpiarBienestar_2"))
        self.btnModificarBienestar = QtGui.QPushButton(self.bienestar)
        self.btnModificarBienestar.setEnabled(True)
        self.btnModificarBienestar.setGeometry(QtCore.QRect(870, 130, 94, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModificarBienestar.setFont(font)
        self.btnModificarBienestar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarBienestar.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.btnModificarBienestar.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificarBienestar.setObjectName(_fromUtf8("btnModificarBienestar"))
        self.line_9 = QtGui.QFrame(self.bienestar)
        self.line_9.setGeometry(QtCore.QRect(850, 0, 16, 191))
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.line_8 = QtGui.QFrame(self.bienestar)
        self.line_8.setGeometry(QtCore.QRect(860, 120, 118, 3))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_10 = QtGui.QFrame(self.bienestar)
        self.line_10.setGeometry(QtCore.QRect(860, 70, 118, 3))
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.frame_6 = QtGui.QFrame(self.bienestar)
        self.frame_6.setGeometry(QtCore.QRect(30, 460, 771, 111))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.label_4 = QtGui.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 181, 17))
        self.label_4.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Observaciones</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txteObservaciones_2 = QtGui.QPlainTextEdit(self.frame_6)
        self.txteObservaciones_2.setGeometry(QtCore.QRect(10, 30, 731, 66))
        self.txteObservaciones_2.setObjectName(_fromUtf8("txteObservaciones_2"))
        self.label_5 = QtGui.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 601, 17))
        self.label_5.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(Introduzca un descripción de los servicios en la comunidad que sean necesarios o requieran mejoras)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lblNotificacionBienestar = QtGui.QLabel(self.bienestar)
        self.lblNotificacionBienestar.setGeometry(QtCore.QRect(30, 10, 811, 31))
        self.lblNotificacionBienestar.setStyleSheet(_fromUtf8("border: 1px solid Yellow;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #FFFF80, stop: 0.08 #FAFFD8,\n"
"stop: 0.39999 #FEFFE5, stop: 0.4 #FEFFE5,\n"
"stop: 0.9 #FAFFD8, stop: 1 #fff);\n"
"\n"
""))
        self.lblNotificacionBienestar.setText(QtGui.QApplication.translate("Censo_socioeconomico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotificacionBienestar.setObjectName(_fromUtf8("lblNotificacionBienestar"))
        self.tabWidget.addTab(self.bienestar, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        Censo_socioeconomico.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Censo_socioeconomico)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_administracion = QtGui.QMenu(self.menubar)
        self.menu_administracion.setTitle(QtGui.QApplication.translate("Censo_socioeconomico", "&Administración", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_administracion.setObjectName(_fromUtf8("menu_administracion"))
        self.menu_Herramientas = QtGui.QMenu(self.menubar)
        self.menu_Herramientas.setTitle(QtGui.QApplication.translate("Censo_socioeconomico", "&Herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Herramientas.setObjectName(_fromUtf8("menu_Herramientas"))
        self.menu_Ayuda = QtGui.QMenu(self.menubar)
        self.menu_Ayuda.setTitle(QtGui.QApplication.translate("Censo_socioeconomico", "&Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Ayuda.setObjectName(_fromUtf8("menu_Ayuda"))
        self.menu_Familias = QtGui.QMenu(self.menubar)
        self.menu_Familias.setTitle(QtGui.QApplication.translate("Censo_socioeconomico", "&Familias", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Familias.setObjectName(_fromUtf8("menu_Familias"))
        self.menu_Archivo = QtGui.QMenu(self.menubar)
        self.menu_Archivo.setTitle(QtGui.QApplication.translate("Censo_socioeconomico", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Archivo.setObjectName(_fromUtf8("menu_Archivo"))
        Censo_socioeconomico.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Censo_socioeconomico)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Censo_socioeconomico.setStatusBar(self.statusbar)
        self.action_Nuevo = QtGui.QAction(Censo_socioeconomico)
        self.action_Nuevo.setText(QtGui.QApplication.translate("Censo_socioeconomico", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Nuevo.setObjectName(_fromUtf8("action_Nuevo"))
        self.actionA_brir = QtGui.QAction(Censo_socioeconomico)
        self.actionA_brir.setText(QtGui.QApplication.translate("Censo_socioeconomico", "A&brir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_brir.setObjectName(_fromUtf8("actionA_brir"))
        self.action_Guardar = QtGui.QAction(Censo_socioeconomico)
        self.action_Guardar.setText(QtGui.QApplication.translate("Censo_socioeconomico", "&Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Guardar.setObjectName(_fromUtf8("action_Guardar"))
        self.action_Salir = QtGui.QAction(Censo_socioeconomico)
        self.action_Salir.setText(QtGui.QApplication.translate("Censo_socioeconomico", "&Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Salir.setToolTip(QtGui.QApplication.translate("Censo_socioeconomico", "Salir de Komunal", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Salir.setObjectName(_fromUtf8("action_Salir"))
        self.actionAcerca_de_Komunal = QtGui.QAction(Censo_socioeconomico)
        self.actionAcerca_de_Komunal.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Acerca de Komunal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de_Komunal.setObjectName(_fromUtf8("actionAcerca_de_Komunal"))
        self.actionListado = QtGui.QAction(Censo_socioeconomico)
        self.actionListado.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Gestión Familias", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado.setObjectName(_fromUtf8("actionListado"))
        self.actionIngresar_Nucleo_Familiar = QtGui.QAction(Censo_socioeconomico)
        self.actionIngresar_Nucleo_Familiar.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Ingresar Nucleo Familiar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIngresar_Nucleo_Familiar.setObjectName(_fromUtf8("actionIngresar_Nucleo_Familiar"))
        self.actionConcejoComunal = QtGui.QAction(Censo_socioeconomico)
        self.actionConcejoComunal.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Consejo Comunal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConcejoComunal.setObjectName(_fromUtf8("actionConcejoComunal"))
        self.actionGestionar_Consejos_Comunales = QtGui.QAction(Censo_socioeconomico)
        self.actionGestionar_Consejos_Comunales.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Gestionar Consejos Comunales", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGestionar_Consejos_Comunales.setObjectName(_fromUtf8("actionGestionar_Consejos_Comunales"))
        self.actionManual_Komunal = QtGui.QAction(Censo_socioeconomico)
        self.actionManual_Komunal.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Manual Komunal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManual_Komunal.setObjectName(_fromUtf8("actionManual_Komunal"))
        self.actionIndicadores = QtGui.QAction(Censo_socioeconomico)
        self.actionIndicadores.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Indicadores", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndicadores.setObjectName(_fromUtf8("actionIndicadores"))
        self.actionExportar_Base_de_Datos = QtGui.QAction(Censo_socioeconomico)
        self.actionExportar_Base_de_Datos.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Exportar Base de Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportar_Base_de_Datos.setObjectName(_fromUtf8("actionExportar_Base_de_Datos"))
        self.actionSalir = QtGui.QAction(Censo_socioeconomico)
        self.actionSalir.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionListado_Familias = QtGui.QAction(Censo_socioeconomico)
        self.actionListado_Familias.setText(QtGui.QApplication.translate("Censo_socioeconomico", "Listado Familias", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Familias.setObjectName(_fromUtf8("actionListado_Familias"))
        self.menu_administracion.addSeparator()
        self.menu_administracion.addAction(self.actionConcejoComunal)
        self.menu_administracion.addAction(self.actionGestionar_Consejos_Comunales)
        self.menu_administracion.addAction(self.actionIndicadores)
        self.menu_Ayuda.addAction(self.actionAcerca_de_Komunal)
        self.menu_Ayuda.addAction(self.actionManual_Komunal)
        self.menu_Familias.addAction(self.actionListado)
        self.menu_Familias.addAction(self.actionIngresar_Nucleo_Familiar)
        self.menu_Familias.addAction(self.actionListado_Familias)
        self.menu_Archivo.addAction(self.actionExportar_Base_de_Datos)
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menu_administracion.menuAction())
        self.menubar.addAction(self.menu_Familias.menuAction())
        self.menubar.addAction(self.menu_Herramientas.menuAction())
        self.menubar.addAction(self.menu_Ayuda.menuAction())

        self.retranslateUi(Censo_socioeconomico)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget1.setCurrentIndex(1)
        QtCore.QObject.connect(self.btnSalirKomunal, QtCore.SIGNAL(_fromUtf8("clicked()")), Censo_socioeconomico.close)
        QtCore.QObject.connect(self.rbtSiTienen, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.chbAll_ninos.setEnabled)
        QtCore.QObject.connect(self.rbtSiTienen, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.chbMenoresSeis.setEnabled)
        QtCore.QObject.connect(self.rbtNoTiene, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.chbAll_ninos.setDisabled)
        QtCore.QObject.connect(self.rbtNoTiene, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.chbMenoresSeis.setDisabled)
        QtCore.QObject.connect(self.rbtSiTienen, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.frame_8.setEnabled)
        QtCore.QObject.connect(self.rbtNoTiene, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.frame_8.setDisabled)
        QtCore.QObject.connect(self.rbtSiOperacion, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.txtCuantos.setEnabled)
        QtCore.QObject.connect(self.rbtSiOperacion, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.txtTipoOperacion.setEnabled)
        QtCore.QObject.connect(self.rbtNoOperacion, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.txtCuantos.setDisabled)
        QtCore.QObject.connect(self.rbtNoOperacion, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.txtTipoOperacion.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Censo_socioeconomico)
        Censo_socioeconomico.setTabOrder(self.txtNombrejefe, self.txtApellidojefe)
        Censo_socioeconomico.setTabOrder(self.txtApellidojefe, self.txtCedulaJefe)
        Censo_socioeconomico.setTabOrder(self.txtCedulaJefe, self.cmbSexoJefe)
        Censo_socioeconomico.setTabOrder(self.cmbSexoJefe, self.cmbNacionalidadJefe)
        Censo_socioeconomico.setTabOrder(self.cmbNacionalidadJefe, self.cmbEdoCivilJefe)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilJefe, self.cmbLugarNacimientoJefe)
        Censo_socioeconomico.setTabOrder(self.cmbLugarNacimientoJefe, self.txtFechaNacJefe)
        Censo_socioeconomico.setTabOrder(self.txtFechaNacJefe, self.txtOcupacionJefe)
        Censo_socioeconomico.setTabOrder(self.txtOcupacionJefe, self.txtIngresoJefe)
        Censo_socioeconomico.setTabOrder(self.txtIngresoJefe, self.cmbGradoInstruccion)
        Censo_socioeconomico.setTabOrder(self.cmbGradoInstruccion, self.btnModificarJefeFamilia)
        Censo_socioeconomico.setTabOrder(self.btnModificarJefeFamilia, self.btnGuardarJefeFamilia)
        Censo_socioeconomico.setTabOrder(self.btnGuardarJefeFamilia, self.Limpiar_datos_jefe)
        Censo_socioeconomico.setTabOrder(self.Limpiar_datos_jefe, self.lblParentescoF1)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF1, self.cmbEdoCivilF1)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF1, self.cmbInstruccionF1)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF1, self.lblOcupacionF1)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF1, self.lblIngresoF1)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF1, self.lblNombreF2)
        Censo_socioeconomico.setTabOrder(self.lblNombreF2, self.lblApellidoF2)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF2, self.lblCedulaF2)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF2, self.lblParentescoF2)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF2, self.cmbEdoCivilF2)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF2, self.cmbInstruccionF2)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF2, self.lblOcupacionF2)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF2, self.lblIngresoF2)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF2, self.lblNombreF3)
        Censo_socioeconomico.setTabOrder(self.lblNombreF3, self.lblApellidoF3)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF3, self.lblCedulaF3)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF3, self.lblParentescoF3)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF3, self.cmbEdoCivilF3)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF3, self.cmbInstruccionF3)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF3, self.lblOcupacionF3)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF3, self.lblIngresoF3)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF3, self.lblNombreF4)
        Censo_socioeconomico.setTabOrder(self.lblNombreF4, self.lblApellidoF4)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF4, self.lblCedulaF4)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF4, self.lblParentescoF4)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF4, self.cmbEdoCivilF4)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF4, self.cmbInstruccionF4)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF4, self.lblOcupacionF4)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF4, self.lblIngresoF4)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF4, self.lblNombreF5)
        Censo_socioeconomico.setTabOrder(self.lblNombreF5, self.lblApellidoF5)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF5, self.lblCedulaF5)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF5, self.lblParentescoF5)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF5, self.cmbEdoCivilF5)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF5, self.cmbInstruccionF5)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF5, self.lblOcupacionF5)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF5, self.lblIngresoF5)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF5, self.lblNombreF6)
        Censo_socioeconomico.setTabOrder(self.lblNombreF6, self.lblApellidoF6)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF6, self.lblCedulaF6)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF6, self.lblParentescoF6)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF6, self.cmbEdoCivilF6)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF6, self.cmbInstruccionF6)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF6, self.lblOcupacionF6)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF6, self.lblIngresoF6)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF6, self.lblNombreF7)
        Censo_socioeconomico.setTabOrder(self.lblNombreF7, self.lblApellidoF7)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF7, self.lblCedulaF7)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF7, self.lblParentescoF7)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF7, self.cmbEdoCivilF7)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF7, self.cmbInstruccionF7)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF7, self.lblOcupacionF7)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF7, self.lblIngresoF7)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF7, self.lblNombreF8)
        Censo_socioeconomico.setTabOrder(self.lblNombreF8, self.lblApellidoF8)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF8, self.lblCedulaF8)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF8, self.lblParentescoF8)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF8, self.cmbEdoCivilF8)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF8, self.cmbInstruccionF8)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF8, self.lblOcupacionF8)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF8, self.lblIngresoF8)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF8, self.lblNombreF9)
        Censo_socioeconomico.setTabOrder(self.lblNombreF9, self.lblApellidoF9)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF9, self.lblCedulaF9)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF9, self.lblParentescoF9)
        Censo_socioeconomico.setTabOrder(self.lblParentescoF9, self.cmbEdoCivilF9)
        Censo_socioeconomico.setTabOrder(self.cmbEdoCivilF9, self.cmbInstruccionF9)
        Censo_socioeconomico.setTabOrder(self.cmbInstruccionF9, self.lblOcupacionF9)
        Censo_socioeconomico.setTabOrder(self.lblOcupacionF9, self.lblIngresoF9)
        Censo_socioeconomico.setTabOrder(self.lblIngresoF9, self.cmbHabitaciones)
        Censo_socioeconomico.setTabOrder(self.cmbHabitaciones, self.cmbSalaComedor)
        Censo_socioeconomico.setTabOrder(self.cmbSalaComedor, self.cmbBanos)
        Censo_socioeconomico.setTabOrder(self.cmbBanos, self.cmbCocina)
        Censo_socioeconomico.setTabOrder(self.cmbCocina, self.lblNombreF1)
        Censo_socioeconomico.setTabOrder(self.lblNombreF1, self.lblCedulaF1)
        Censo_socioeconomico.setTabOrder(self.lblCedulaF1, self.lblApellidoF1)
        Censo_socioeconomico.setTabOrder(self.lblApellidoF1, self.cmbTipoVivienda)
        Censo_socioeconomico.setTabOrder(self.cmbTipoVivienda, self.chkTecho)
        Censo_socioeconomico.setTabOrder(self.chkTecho, self.chkPiso)
        Censo_socioeconomico.setTabOrder(self.chkPiso, self.chkFriso)
        Censo_socioeconomico.setTabOrder(self.chkFriso, self.chkPared)
        Censo_socioeconomico.setTabOrder(self.chkPared, self.chkPintura)
        Censo_socioeconomico.setTabOrder(self.chkPintura, self.chkAmpliar)
        Censo_socioeconomico.setTabOrder(self.chkAmpliar, self.chkCocina)
        Censo_socioeconomico.setTabOrder(self.chkCocina, self.chkJardineria)
        Censo_socioeconomico.setTabOrder(self.chkJardineria, self.cmbMaterialTecho)
        Censo_socioeconomico.setTabOrder(self.cmbMaterialTecho, self.cmbEstadoVivienda)
        Censo_socioeconomico.setTabOrder(self.cmbEstadoVivienda, self.cmbTenencia)
        Censo_socioeconomico.setTabOrder(self.cmbTenencia, self.cmbMaterialPared)
        Censo_socioeconomico.setTabOrder(self.cmbMaterialPared, self.cmbUsoVivienda)
        Censo_socioeconomico.setTabOrder(self.cmbUsoVivienda, self.cmbMaterialPiso)

    def retranslateUi(self, Censo_socioeconomico):
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)
        item = self.tableWidget.horizontalHeaderItem(2)
        item = self.tableWidget.horizontalHeaderItem(3)
        item = self.tableWidget.horizontalHeaderItem(4)
        item = self.tableWidget.horizontalHeaderItem(5)
        item = self.tableWidget.horizontalHeaderItem(6)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Listado_familia), QtGui.QApplication.translate("Censo_socioeconomico", "Listado", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.jefe_familia), QtGui.QApplication.translate("Censo_socioeconomico", "&Jefe de Familia", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.intgrantes), QtGui.QApplication.translate("Censo_socioeconomico", "&Integrantes Familiar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Datos_Familia), QtGui.QApplication.translate("Censo_socioeconomico", "&Grupo Familiar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vivienda), QtGui.QApplication.translate("Censo_socioeconomico", "Vivienda", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Censo_socioeconomico", "Salud Vacunas", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bienestar), QtGui.QApplication.translate("Censo_socioeconomico", "&Bienestar", None, QtGui.QApplication.UnicodeUTF8))

