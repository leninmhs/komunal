#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, datetime
import traceback, logging
#import logging
import inicial
from inicial import *
from bienvenida import *
from PyQt4 import QtCore, QtGui


class Funciones(object):

    #def __init__( self):
    #	self.lenin = "Lenincito"
	#object.__init__(self)
	#inicial = MyForm(object)
	#self.form = MyForm( )
	#print self.form.login.ui.txtUsuario.text()
    #	return
    
    
    def limpiar_formularios (self, parent, foco):

	print foco
	#self.login = DlgBienvenida()
	
	#self.login.ui.txtUsuario.setText("")
	#self.login.ui.txtClave.setText("")
	#self.login.ui.txtClave.setText("")
	#parent.login.ui.txtUsuario.setText("")
	#parent.login.ui.txtClave.setText("")

	parent.ui.lblErrorCedulaJefe.setText("upaa")
	parent.ui.txtCedulaJefe.setStyleSheet("background-color: #FFF")		
	parent.ui.lblErrorNombreJefe.setText("")
	parent.ui.txtNombrejefe.setStyleSheet("background-color: #FFF")
	parent.ui.lblErrorApellidoJefe.setText("")
	parent.ui.txtApellidojefe.setStyleSheet("background-color: #FFF")
	parent.ui.lblErrorFechaJefe.setText("")
	parent.ui.txtFechaNacJefe.setStyleSheet("background-color: #FFF")
	parent.ui.lblErrorOcupacionJefe.setText("")
	parent.ui.txtOcupacionJefe.setStyleSheet("background-color: #FFF")
	parent.ui.lblErrorIngresosJefe.setText("")
	parent.ui.txtIngresoJefe.setStyleSheet("background-color: #FFF")
	#eval("parent.login.ui." + foco + ".setFocus()")
	
	

    def generar_log(self, parent,  mensaje):
	#archivo_log = QtCore.QDir.currentPath() + "/komunal.log"

	error = " - Error Clase ->" + str(sys.exc_info()[0])
	error = error + " - Error Descripcion ->" + str(sys.exc_info()[1])
	error = error + " - Error Traza ->" + str(traceback.extract_tb(sys.exc_info()[2]))
	#fname = open(archivo_log, 'a')
	fecha = datetime.datetime.now().strftime("\n[%Y-%m-%d %H:%M:%S]")
	#fname.write( fecha + mensaje  )
	#fname.close()
	#logging.basicConfig(filename = archivo_log, filemode = 'a', format='Nivel: %(levelname)s\nFecha-hora: %(asctime)s\n%(mensaje)s\n', level=logging.ERROR)
	#+ str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + str(traceback.extract_tb(sys.exc_info()[2]))
	#logging.basicConfig( filename = archivo_log, filemode = 'a', format= mensaje , level=logging.ERROR )
	if (str(sys.exc_info()[0]) != "None" ):
	    mensaje = mensaje + error
	    
	logging.basicConfig( filename = 'komunal.log', filemode='a', level=logging.DEBUG )
	logging.error( fecha + mensaje )
	

    def centroPantalla(self, parent):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  parent.geometry()
        parent.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
