# -*- coding: utf-8 -*-
import sys
import datetime, hashlib, re;
#from sqlalchemy import *
from PyQt4 import QtCore, QtGui
from frmconsejo import *
from funciones import *

#from frmfamiliaslist import *
#pyuic4 ui/frmconsejo.ui -o frmconsejo.py

class concejoComunal(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Sqlite
		try:
			try: import sqlite3 as dbapi
			except ImportError: from pysqlite2 import dbapi2 as dbapi
	
	
		except:
			QMessageBox.critical(self,"komunal.db - Error",self.str("No se pudo cargar la extensión SQLlite."))
			self.setCursor(QCursor(0))
			return
		print "SQLite cargado"		
		try:				
			self.db = dbapi.connect("komunal.db")
		except:
			print "error al conectar"
			QMessageBox.critical(self,"sMovieDB - Error",self.__tr("No se pudo conectar con la base de datos"))
			self.setCursor(QCursor(0))
			return
		self.dbconn = self.db.cursor()
	
		self.connect(self.ui.btnGuardarConsejo, QtCore.SIGNAL('clicked()'),self.guardarConcejoComunal)
		self.connect(self.ui.btnModificarConsejo, QtCore.SIGNAL('clicked()'),self.ModificarConcejoComunal)
		self.funciones = Funciones(  )
		self.ui.lblNotificacionConsejo.setHidden(True)
		self.ui.btnModificarConsejo.setVisible(False)
		self.funciones.centroPantalla(self)
	'''
	def limpiarMensajesError():
		self.ui.lblErrorNombreUsuario.setText("")		
		self.ui.lblErrorClavesIguales.setText("")
		self.ui.txtNombreConsejo.setText("AQUII")
		return
	'''	
	def llenarCamposmodificarConsejo(self, gidconsejo, gidusuario):
		print "A modificar!!"

		consejo = self.dbconn.execute(str("select * from consejo_comunal where id_consejo='"+ str(gidconsejo) +"'")).fetchone()
		usuario = self.dbconn.execute(str("select * from usuario where co_consejo='"+ str(gidconsejo) +"' and id_usuario='"+ str(gidusuario) +"'")).fetchone()
		
		
		print str(consejo[1]) + str(consejo[2]) + str(consejo[3]) + usuario[1]
		self.ui.cmbTipoConsejo.setItemText(0, consejo[1])
		self.ui.txtNombreConsejo.setText(consejo[2])
		self.ui.cmbTipoConsejo.setItemText(0, consejo[2])
		self.ui.txtMunicipio.setText(consejo[4])
		self.ui.txtParroquia.setText(consejo[5])
		self.ui.txtSector.setText(consejo[6])
		self.ui.textDireccionConsejo.setPlainText(consejo[7])
		self.ui.txtNombre.setText(consejo[8])
		self.ui.txtApellido.setText(consejo[9])
		self.ui.txtCedula.setText(consejo[10])
		self.ui.txtTelefono.setText(consejo[11])
		self.ui.txtTelefono2.setText(consejo[12])
		self.ui.txtCorreo.setText(consejo[13])
		self.ui.textDireccionPersona.setPlainText(consejo[14])		
	
		self.ui.txtNombreCompleto.setText(usuario[3])
		self.ui.txtCedulaUsuario.setText(usuario[4])
		self.ui.txtCorreoUsuario.setText(usuario[5])
		self.ui.txtUsuario.setText(usuario[1])
		self.ui.txtClave.setText(usuario[2])
		self.ui.txtClave2.setText(usuario[2])
		
		self.ui.btnGuardarConsejo.setVisible(False)
		self.ui.btnModificarConsejo.setVisible(True)

		
	def ModificarConcejoComunal(self):
		print "aqui sql modificar"

		if (self.ui.txtNombreConsejo.text() == ''):
			self.ui.lblErrorNombreConsejo.setText("Campo Requerido")
			self.ui.txtNombreConsejo.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtNombreConsejo.setFocus()
		else:
			'''sexoJefe = "M" if self.ui.cmbSexoJefe.currentText() == "Masculino" else "F"
			nacionalidadJefe = "V" if self.ui.cmbNacionalidadJefe.currentText() == "Venezolano" else "E"'''
			#id_grupo = self.dbconn.execute(str("select id from familia where cedula='"+self.ui.txtCedulaJefe.text()+"'")).fetchone()[0]
			sql = "UPDATE consejo_comunal set "
			sql = sql+"tipo_consejo='"+str(self.ui.cmbTipoConsejo.currentText())+"', "
			sql = sql+"nombre_consejo='"+str(self.ui.txtNombreConsejo.text())+"', "
			sql = sql+"estado='"+str(self.ui.cmbEstado.currentText())+"', "
			sql = sql+"municipio='"+str(self.ui.txtMunicipio.text())+"', "
			sql = sql+"parroquia='"+str(self.ui.txtParroquia.text())+"', "
			sql = sql+"sector='"+str(self.ui.txtSector.text())+"', "
			sql = sql+"direccion_consejo='"+str(self.ui.textDireccionConsejo.toPlainText())+"', "
			sql = sql+"vocero_nombre='"+str(self.ui.txtNombre.text())+"', "
			sql = sql+"vocero_apellido='"+str(self.ui.txtApellido.text())+"', "
			sql = sql+"vocero_cedula='"+str(self.ui.txtCedula.text())+"', "
			sql = sql+"vocero_tlf='"+str(self.ui.txtTelefono.text())+"', "
			sql = sql+"vocero_tlf2='"+str(self.ui.txtTelefono2.text())+"', "
			sql = sql+"vocero_correo='"+str(self.ui.txtCorreo.text())+"', "
			sql = sql+"vocero_direccion='"+str(self.ui.textDireccionPersona.toPlainText())+"', "
			sql = sql+"activo='S' "			
			sql = sql+" WHERE id_consejo='" + str(1) +"'"
			try:
				self.dbconn.execute(str(sql))
				self.db.commit()
				self.funciones.generar_log(self, "El consejo comunal " + self.ui.txtNombreConsejo.text() + " fue modificado. " + str(sql))				
				self.ui.lblNotificacionConsejo.setHidden(False)
				self.ui.lblNotificacionConsejo.setText("<b>Los datos del consejo comunal "+str(self.ui.txtNombreConsejo.text())+" fueron modificados exitosamente!</b>")
			except:
				self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
				self.funciones.generar_log(self, "Error modificando el consejo comunal = "+str(sql))
				QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error Modificando", "Ocurrio un error Modificando el consejo comunal ").exec_()
				print sql
				return
	
		print sql
	
		
		
	def guardarConcejoComunal(self):
		
		
		
		self.ui.lblErrorNombreConsejo.setText("")
		self.ui.txtNombreConsejo.setStyleSheet("background-color: #FFF")		
		self.ui.lblErrorMunicipio.setText("")
		self.ui.txtMunicipio.setStyleSheet("background-color: #FFF")
		self.ui.lblErrorParroquia.setText("")
		self.ui.txtParroquia.setStyleSheet("background-color: #FFF")
		self.ui.lblErrorSector.setText("")
		self.ui.txtSector.setStyleSheet("background-color: #FFF")
		self.ui.lblErrorDireccionConsejo.setText("")
		self.ui.textDireccionConsejo.setStyleSheet("background-color: #FFF")
		self.ui.lblErrorVNombre.setText("")
		self.ui.txtNombre.setStyleSheet("background-color: #FFF")
		self.ui.lblErrorVApellido.setText("")
		self.ui.txtApellido.setStyleSheet("background-color: #FFF")		
		self.ui.lblErrorVTlf.setText("")
		self.ui.txtTelefono.setStyleSheet("background-color: #FFF")
		self.ui.lblErrorVCorreo.setText("")
		self.ui.txtCorreo.setStyleSheet("background-color: #FFF")
		self.ui.lblErrorVCorreo.setText("")
		self.ui.txtCorreoUsuario.setStyleSheet("background-color: #FFF")
		
		
		
		digito= self.ui.txtCedula.text()
		if str(digito).isdigit():
			print str(digito)
		else:
			self.ui.lblErrorVCedula.setText("Solo digitos")
			self.ui.txtCedula.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtCedula.setFocus()
			print "No es digito la cedula"
			
		
		if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',str(self.ui.txtCorreo.text()).lower()):
			print "Correo correcto"
		else:
			print "Correo incorrecto"
			
		
		if (self.ui.txtCorreo.text() != ''):	
			if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", str(self.ui.txtCorreo.text())) == None:
				print "No Valido"
				self.ui.lblErrorVCorreo.setText("Correo Invalido")
				self.ui.txtCorreo.setStyleSheet("background-color: #FFD8D8")
				self.ui.txtCorreo.setFocus()			
		
		if (self.ui.txtCorreoUsuario.text() != ''):	
			if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", str(self.ui.txtCorreoUsuario.text())) == None:
				print "No Valido"
				self.ui.lblErrorCorreoUsuario.setText("Correo Invalido")
				self.ui.txtCorreoUsuario.setStyleSheet("background-color: #FFD8D8")
				self.ui.txtCorreoUsuario.setFocus()
		



		#self.limpiarMensajesError()

		
		
		
		if (self.ui.txtNombreConsejo.text() == ''):
			self.ui.lblErrorNombreConsejo.setText("Campo Requerido")
			self.ui.txtNombreConsejo.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtNombreConsejo.setFocus()

		elif (self.ui.txtMunicipio.text() == ''):
			self.ui.lblErrorMunicipio.setText("Campo Requerido")
			self.ui.txtMunicipio.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtMunicipio.setFocus()

		elif (self.ui.txtParroquia.text() == ''):
			self.ui.lblErrorParroquia.setText("Campo Requerido")
			self.ui.txtParroquia.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtParroquia.setFocus()

		elif (self.ui.txtSector.text() == ''):
			self.ui.lblErrorSector.setText("Campo Requerido")
			self.ui.txtSector.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtSector.setFocus()

		elif (self.ui.textDireccionConsejo.toPlainText() == ''):
			self.ui.lblErrorDireccionConsejo.setText("Campo Requerido")
			self.ui.textDireccionConsejo.setStyleSheet("background-color: #FFD8D8")
			self.ui.textDireccionConsejo.setFocus()

		elif (self.ui.txtNombre.text() == ''):
			self.ui.lblErrorVNombre.setText("Campo Requerido")
			self.ui.txtNombre.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtNombre.setFocus()

		elif (self.ui.txtApellido.text() == ''):
			self.ui.lblErrorVApellido.setText("Campo Requerido")
			self.ui.txtApellido.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtApellido.setFocus()
			
		elif (self.ui.txtCedula.text() == '' ):
			self.ui.lblErrorVCedula.setText("Campo Requerido")
			self.ui.txtCedula.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtCedula.setFocus()
			
		elif (self.ui.txtTelefono.text()== ''):
			self.ui.lblErrorVTlf.setText("Campo Requerido")
			self.ui.txtTelefono.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtTelefono.setFocus()
			
		elif (self.ui.textDireccionPersona.toPlainText() == ''):
			self.ui.lblErrorVDireccion.setText("Campo Requerido")
			self.ui.textDireccionPersona.setStyleSheet("background-color: #FFD8D8")
			self.ui.textDireccionPersona.setFocus()

		elif (self.ui.txtNombreCompleto.text() == '') :
			self.ui.lblErrorNombreUsuario.setText("Campo Requerido")
			self.ui.txtNombreCompleto.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtNombreCompleto.setFocus()
			
		elif (self.ui.txtCedulaUsuario.text() == ''):
			#self.ui.lblErrorCedulaUsuario.setText("Campo Requerido")
			self.ui.txtCedulaUsuario.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtCedulaUsuario.setFocus()

		elif (self.ui.txtUsuario.text() == ''):
			#self.ui.lblErrorUsuario.setText("Campo Requerido")
			self.ui.txtUsuario.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtUsuario.setFocus()
			
		elif (self.ui.txtClave.text() == ''):
			self.ui.lblErrorClave.setText("Campo Requerido")
			self.ui.txtClave.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtClave.setFocus()

		elif (self.ui.txtClave2.text() == ''):
			self.ui.lblErrorClave2.setText("Campo Requerido")
			self.ui.txtClave2.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtClave2.setFocus()

		elif (self.ui.txtClave2.text() != self.ui.txtClave.text()):
			self.ui.lblErrorClavesIguales.setText("Contraseñas no coinciden. Verifique nuevamente.")
			self.ui.txtClave.setText("")
			self.ui.txtClave.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtClave2.setText("")
			self.ui.txtClave2.setStyleSheet("background-color: #FFD8D8")
			self.ui.txtClave.setFocus()
		
		else:
			#sql = "INSERT INTO consejo_comunal ('nombre_consejo', 'estado', 'municipio', 'parroquia', 'sector',  'direccion_consejo', 'vocero_nombre', 'vocero_apellido', 'vocero_cedula','vocero_tlf','tlf2', 'correo','id_usuario') VALUES( "

			sql= "INSERT INTO consejo_comunal ('tipo_consejo', 'nombre_consejo'  , 'estado', 'municipio' , 'parroquia'  ,'sector'  ,'direccion_consejo', 'vocero_nombre' ,'vocero_apellido' ,'vocero_cedula' ,'vocero_tlf' ,'vocero_tlf2' ,'vocero_correo' , 'vocero_direccion' ,'activo' ,'id_usuario' ) VALUES ("
			sql = sql + "'" + self.ui.cmbTipoConsejo.currentText() + "'"
			sql = sql + ",'" + self.ui.txtNombreConsejo.text() + "'"
			sql = sql + ",'" + self.ui.cmbEstado.currentText() + "'"
			sql = sql + ",'" + self.ui.txtMunicipio.text() + "'"
			sql = sql + ",'" + self.ui.txtParroquia.text() + "'"
			sql = sql + ",'" + self.ui.txtSector.text() + "'"
			sql = sql + ",'" + self.ui.textDireccionConsejo.toPlainText() + "'"
			#sql = sql + ",'" + self.ui.textEdit.selectAll() + "'"
			sql = sql + ",'" + self.ui.txtNombre.text() + "'"
			sql = sql + ",'" + self.ui.txtApellido.text() + "'"
			sql = sql + ",'" + self.ui.txtCedula.text() + "'"
			sql = sql + ",'" + self.ui.txtTelefono.text() + "'"
			sql = sql + ",'" + self.ui.txtTelefono2.text() + "'"
			#sql = sql + ",'" + self.ui.textDireccionPersona.selectAll() + "')"
			sql = sql + ",'" + self.ui.txtCorreo.text() + "'"
			sql = sql + ",'" + self.ui.textDireccionPersona.toPlainText() + "'"
                        sql = sql + ",'" + 'S' + "'"
			sql = sql + ",'1')"
			#sql = sql + ",'" + self.ui.txtUsuario.text() + "'"
			#sql = sql + ",'" + hashlib.md5(self.ui.txtClave.text()).hexdigest() + "')"
                        sql_1 =  "INSERT INTO usuario ('usuario', 'passwd', 'nombre_completo', 'cedula', 'correo',  'id_perfil','co_consejo', 'activo') VALUES( "
			sql_1 = sql_1 + "'" + self.ui.txtUsuario.text() + "'"
			sql_1 = sql_1 + ",'" + hashlib.md5(self.ui.txtClave.text()).hexdigest() + "'"
			sql_1 = sql_1 + ",'" + self.ui.txtNombreCompleto.text() + "'"
			sql_1 = sql_1 + ",'" + self.ui.txtCedulaUsuario.text() + "'"
			sql_1 = sql_1 + ",'" + self.ui.txtCorreoUsuario.text() + "'"
			sql_1 = sql_1 + ",'2'"
	    		sql_1 = sql_1 + ",'" + str(self.dbconn.execute("SELECT seq FROM sqlite_sequence where name = 'consejo_comunal'").fetchone()[0]+1)+"'"
			sql_1 = sql_1 + ",'s')"
			try:
				self.dbconn.execute(str(sql))
				self.dbconn.execute(str(sql_1))
				self.db.commit()
				self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
				self.ui.lblNotificacionConsejo.setHidden(False)
				QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Los datos fueron guardados exitosamente", "El Consejo Comunal fue registrado satifactoriamente. Ingrese con el usuario y contraseña suministrado").exec_()
				self.funciones.generar_log(self, "El consejo comunal " + self.ui.txtNombreConsejo.text() + " fue registrado exitosamente. " + str(sql))				

			except:
				self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
				self.funciones.generar_log(self, "Ocurrio un error guardando el consejo comunal: " + self.ui.txtNombreConsejo.text() + str(sql))				
				QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Ocurrio un error", "Guardando los datos.Contacte al administrador").exec_()
				print sql
				
			#iva aqui
				
				return
			print sql	
