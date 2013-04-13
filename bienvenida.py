# -*- coding: utf-8 -*-

from frmlogin import *
#from frmfamiliaslist import * 

class DlgBienvenida(QtGui.QDialog):

	def __init__(self, parent=None):
			
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_frmLogin()
		#self.ui = Ui_Familias_listado()
		self.ui.setupUi(self)
		
		#Icono del boton salir
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("./themes/default/16x16/dialog-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		#self.ui.btnSalir.setIcon(icon)
                #self.ui.btnContinuar2.setVisible(False)
		#self.ui.textLabel1.setOpenExternalLinks(1)
		#self.ui.textLabel1.setText(str("Komunal\n\nCopyright: (C) 2012 \n\n Sistema para la Gestión del Censo Socioeconómico de los Consejos Comunales \n\n Python + QT4 + SQLite"))
                #self.connect(self.ui.btnContinuar2, QtCore.SIGNAL('activated()'),self.frmAutenticar)
                #self.connect(self.ui.btnContinuar, QtCore.SIGNAL('activated()'),self.frmAutenticar)


		#self.ui.tabWidget4.setCurrentIndex(0)

	def version(self,version):
		self.ui.lblName.setText("<b>Komunal "+str(version)+"</b>")

        def frmAutenticar(self):
            print "ajaaa"
            self.frm_about3 = about2()
            self.frm_about3.show()
            return 

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    about = DlgBienvenida()
    about.ui.show()
    app.exec_()