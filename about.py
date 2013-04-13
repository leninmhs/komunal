# -*- coding: utf-8 -*-

from frmacerca import *
#from frmfamiliaslist import * 

class about2(QtGui.QDialog):

	def __init__(self, parent=None):
			
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_frmacercade()
		#self.ui = Ui_Familias_listado()
		self.ui.setupUi(self)
		
		#Icono del boton salir
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("./themes/default/16x16/dialog-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btnSalir.setIcon(icon)

		#self.ui.textLabel1.setOpenExternalLinks(1)
		self.ui.textLabel1.setText(str("Komunal\n\nCopyright: (C) 2012 \n\n Sistema para la Gestión del Censo Socioeconómico de los Consejos Comunales \n\n Python + QT4 + SQLite"))

		self.ui.tabWidget4.setCurrentIndex(0)

	def version(self,version):
		self.ui.lblName.setText("<b>Komunal "+str(version)+"</b>")
