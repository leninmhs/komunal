#!/usr/bin/python
# -*- coding: utf-8 -*-
# aptitude install python-psycopg2
# pyqt4-dev-tools python-sqlite python-reportlab
# pyuic4 ui/familias.ui -o familias.py
#
import sys, time
import datetime;
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from frmfamilias import *
from concejocomunal import *
from about import *
from bienvenida import *
from indicadores import *
from funciones import *
from generarPdfs import *

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
	    QtGui.QWidget.__init__(self, parent)
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
		    QMessageBox.critical(self,"Komunal - Error",self.__tr("No se pudo conectar con la base de datos"))
		    self.setCursor(QCursor(0))
		    return
	    self.dbconn = self.db.cursor()

	    self.ui = Ui_Censo_socioeconomico()
	    self.ui.setupUi(self)
	    self.login = DlgBienvenida()
	    self.login.show()
	    
	    self.login.ui.txtUsuario.setFocus()
	    self.connect(self.login.ui.btnLoginAceptar, QtCore.SIGNAL('clicked()'),self.validarLogin)
	    self.connect(self.login.ui.btnRegistroLogin, QtCore.SIGNAL('clicked()'),self.frmConcejoComunal)

	    globals()["gidusuario"] = 0
	    globals()["gidconsejo"] = 0
	    self.funciones = Funciones(  )
	    self.generarPdf = GenerarPdf(  )

    def iniciar(self):
	    #splash_pix = QPixmap('img/komunal-logo-beta.png')
	    #splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
	    #splash.setMask(splash_pix.mask())
	    #splash.show()
	    #time.sleep(2) #Simular que toma tiempo abrir la aplicacion
	    #myapp.show()
	    #splash.finish(myapp)
	    #splash.finish(self)
	    self.funciones.centroPantalla(self)
	    self.actualizarGrid()
	    self.show()



	    
	    self.ui.lblNombreConsejo.setText( "Consejo Comunal: " + self.dbconn.execute("select nombre_consejo from consejo_comunal where id_consejo= " + str(gidconsejo) ).fetchone()[0])
	    self.ui.lblUsuarioAutenticado.setText( "Usuario: " + self.dbconn.execute("select nombre_completo from usuario where id_usuario= " + str(gidusuario) ).fetchone()[0])
	    self.ui.lblUsuarioAutenticado.setAlignment(QtCore.Qt.AlignRight)
	    self.connect(self.ui.btnGuardarJefeFamilia, QtCore.SIGNAL('clicked()'),self.guardarJefeFamilia)
	    self.connect(self.ui.btnGuardarMiembros, QtCore.SIGNAL('clicked()'),self.guardarMiembrosFamilia)
	    self.connect(self.ui.btnGuardarVivienda, QtCore.SIGNAL('clicked()'),self.guardarViviendaFamilia)
	    self.connect(self.ui.actionAcerca_de_Komunal, QtCore.SIGNAL('activated()'),self.acercaKomunal)
	    self.connect(self.ui.actionListado_Familias, QtCore.SIGNAL('activated()'),self.listadoFamilias)
	    self.connect(self.ui.actionIndicadores, QtCore.SIGNAL('activated()'),self.indicadoresKomunal)
	    self.connect(self.ui.btnBorrarFamilia, QtCore.SIGNAL('clicked()'),self.borrarFamilia)
	    self.connect(self.ui.btnModificarFamilia, QtCore.SIGNAL('clicked()'),self.llenarCamposModificarFamilia)
	    self.connect(self.ui.btnPlanillaFamilia, QtCore.SIGNAL('clicked()'),self.generarPlanillaFamilia)

	    self.connect(self.ui.btnModificarJefeFamilia, QtCore.SIGNAL('clicked()'),self.modificarJefeFamilia)
    	    self.connect(self.ui.actionConcejoComunal, QtCore.SIGNAL('activated()'),self.modificarConcejoComunal)
	    self.connect(self.ui.btnGuardarBienestar_2, QtCore.SIGNAL('clicked()'),self.guardarBienestar)
	    self.connect(self.ui.btnModificarBienestar, QtCore.SIGNAL('clicked()'),self.modificarBienestar)
	    self.connect(self.ui.btnGuardarSalud_2, QtCore.SIGNAL('clicked()'),self.guardarSalud)
	    self.ui.btnModificarJefeFamilia.setVisible(False)
	    self.ui.btnModificarBienestar.setVisible(False)
	    self.ui.lblNotificacionJefeFamilia.setVisible(False)

	    self.ui.btnModificarSalud_2.setVisible(False)
	    self.ui.lblNotificacionSalud.setVisible(False)
	    self.ui.tabWidget.setCurrentIndex(0)





    def actualizarGrid(self):
	    rows = 0
	    self.ui.tableWidget.clearContents()
		
	    global gidconsejo
	    global gidusuario
	    sql = "select id,cedula,nombre,apellido,fecha_nacimiento, case when sexo='F' then 'Femenino'  else 'Masculino'   end  as sexo, (Date('now') -fecha_nacimiento) as edad  from familia where jefe_familia = 'S' and co_consejo = '"+ str(gidconsejo) +"' order by id desc"
            #(Date('now') -fecha_nacimiento) as edad
	    self.dbconn.execute(str(sql))
	    rs = self.dbconn.fetchall()
	    self.familiares = {}
	    for familiar in rs:
	        self.ui.tableWidget.setRowCount(rows+1)
		    #print rows
	        self.ui.tableWidget.setItem(rows, 0, QtGui.QTableWidgetItem(str(familiar[0])))
	        self.ui.tableWidget.setItem(rows, 1, QtGui.QTableWidgetItem(familiar[1]))
	        self.ui.tableWidget.setItem(rows, 2, QtGui.QTableWidgetItem(familiar[2]))
	        self.ui.tableWidget.setItem(rows, 3, QtGui.QTableWidgetItem(familiar[3]))
	        self.ui.tableWidget.setItem(rows, 4, QtGui.QTableWidgetItem(familiar[5]))
	        self.ui.tableWidget.setItem(rows, 5, QtGui.QTableWidgetItem(str(familiar[6])))
   	        self.ui.tableWidget.setItem(rows, 6, QtGui.QTableWidgetItem(str(self.dbconn.execute("SELECT COUNT(*) FROM familia where id_grupo = '"+ str(familiar[0])+"'").fetchone()[0])))
	        rows=rows+1

	    self.ui.lblTotalFamilias.setText( "Total Familias: " + str(rows))

    def validarLogin(self):
	sql = "SELECT id_usuario,co_consejo FROM usuario where usuario= '"+ str(self.login.ui.txtUsuario.text()) + "' AND passwd = '"+ str(hashlib.md5(self.login.ui.txtClave.text()).hexdigest()) + "'"
	if ( self.dbconn.execute(str(sql)).fetchone() ):
	    global gidusuario
	    global gidconsejo
	    gidusuario = self.dbconn.execute(str(sql)).fetchone()[0]
	    gidconsejo = self.dbconn.execute(str(sql)).fetchone()[1]

	    self.login.close()
	    self.iniciar()
	    self.funciones.generar_log(self, "Inicio session usuario " + str(self.login.ui.txtUsuario.text()) )

	else:
	    self.funciones.limpiar_formularios(self,"txtUsuario")
	    self.login.ui.lblError.setVisible(True)
	    self.login.ui.lblError.setText("<b>Datos incorrectos :(</b>")
	    self.funciones.generar_log(self, "Login Datos incorrectos = "+str(sql))




    def generarPlanillaFamilia(self):
	from reportlab.lib.pagesizes import A4
	from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
	from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
	from reportlab.platypus import Paragraph, Image
	from reportlab.lib import colors
	
	pdf_x_familia = QtGui.QFileDialog.getSaveFileName(self, "Guardar Planilla Komunal (*.pdf)", QtCore.QDir.homePath() + "/familia-" + str(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()) + ".pdf", "Documento PDF (*.pdf)")
	styleSheet=getSampleStyleSheet()
	story=[]
	h1=styleSheet['Heading1']
	h1.pageBreakBefore=0
	h1.keepWithNext=1
	h1.backColor=colors.red
	h2=styleSheet['Heading2']
	h2.pageBreakBefore=0
	h2.keepWithNext=1
	
	img=Image("img/logo_pdf_barra.png",580,70)
	img.hAlign = "LEFT"
	
	texto_principal = ""
	estilo_texto = ParagraphStyle('',
		        fontSize = 22,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
			#backColor = '#fff',
			textColor = '#999',
			leftIndent = 10 )

	otro_estilo= ParagraphStyle('',
	             fontSize = 20,
		     textColor = '#000',
		     leftIndent = 200,
		     rightIndent = 50) 

	style_barra= ParagraphStyle('',
		     fontSize = 13,
		     textColor = '#000',
		     backColor='#f5f5f5',
		     borderColor ='#a3a3a3',
		     borderWidth = 1,
		     borderPadding = (1, 2, 5))

	style_fecha= ParagraphStyle('',
		     fontSize = 11,
		     textColor = '#000',
		     leftIndent = 500,
		     rightIndent = 10)

	h = Paragraph( texto_principal, estilo_texto)
	banner = [ [ img , h ] ]
	
	ban = Table( banner, colWidths=300 )
	ban.setStyle([ ('ALIGN',(0,0),(0,0),'LEFT'),('ALIGN',(0,0),(1,0),'LEFT'), ('VALIGN',(0,0),(1,0),'TOP'),
			('TEXTCOLOR',(0,1),(0,-1), colors.blue) ])
	story.append(ban)
	story.append(Spacer(0,10))

	dia = time.localtime()
	mes = dia.tm_mon
	mes_sp = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre']
 
	hoy='%s %d' % (mes_sp[mes-1], dia.tm_year)
	P= Paragraph(hoy,style_fecha)
	story.append(P)
	story.append(Spacer(0,25))

	P= Paragraph("<b>Censo Socio-Economico</b> ",otro_estilo)
	story.append(P)
	story.append(Spacer(0,25))

	P=Paragraph("<b>Información General</b> ",style_barra)
	story.append(P)
	story.append(Spacer(0,25))


	style=styleSheet['BodyText']
	
	consejo = self.dbconn.execute("select * from consejo_comunal where id_consejo=1").fetchone()
	
	data_consejo = [['Consejo Comnual: ', consejo[2] ],
			['Estado' ,'Municipio:' , 'Parroquia:', 'Sector: ' ],
			[ consejo[3], consejo[4] , consejo[5] , consejo[6]] ,
			['Dirección: ', consejo[7] ] ]
	c=Table(data_consejo, colWidths=148)
	c.setStyle([  ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		      ('BOX', (0,0), (-1,-1), 0.25, colors.black), ('SPAN',(1,3),(3,3)), ('SPAN',(1,0),(-1,0))
		   ])	
	story.append(c)
	story.append(Spacer(0,15))	
	
	
	
	jefe = self.dbconn.execute("SELECT *, (Date('now') -fecha_nacimiento) as edad FROM familia where id_grupo= 1 AND jefe_familia= 'S'").fetchone()

	PO = Paragraph('''<font size=12> <b> Jefe de Familia</b></font>''',styleSheet["BodyText"])
	print jefe
	sexoJefe = "Masculino" if jefe[6] == "M" else "Femenino"
	if (jefe[9]== '' or jefe[9]== 0):
	    ingreso = "N/P"
	else:
	    ingreso = jefe[9] + " Bs. "
	datos_jefe = [[ Paragraph('''<font size=12> <b> Jefe de Familia</b></font>''',styleSheet["BodyText"]) ],
		    ['Cedula: ', jefe[12]+jefe[4], 'Apellidos y Nombres: ' , str(jefe[2])+ ' ' + str(jefe[3]) , 'Sexo: ', sexoJefe ],
		    [ 'Lugar de Nacimiento: ',jefe[12] , 'Fecha Nacimiento: ', jefe[5], 'Edad: ', jefe[19] ],
		    ['Edo Civil: ',jefe[11], 'Ingreso Mensual: ', ingreso , 'Grado de Instrucción', jefe[10] ], 
		    ['Ocupación: ', jefe[8]] ]
	
	colwidths = (100, 90, 100, 90, 110, 100)
	j = Table( datos_jefe, colwidths )
	j.setStyle([ ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	('BOX', (0,0), (-1,-1), 0.25, colors.black),('SPAN',(0,0),(5,0)) ])
	story.append(j)
	story.append(Spacer(0,15))

	self.dbconn.execute("SELECT *, (Date('now') -fecha_nacimiento) as edad FROM familia where id_grupo= 1 AND jefe_familia= 'N'")
	rs = self.dbconn.fetchall()
	
	integrantes = [[Paragraph('''<font size=12> <b> Integrantes del grupo familiar</b></font>''',styleSheet["BodyText"])],
			['Cedula', 'Nombre/Apellido', 'Parentesco', 'Sexo', 'Edad', 'Edo Civil' , 'Instrucción', 'Ocupación','Ingreso']]
	for familia in rs:
	    	if (familia[9]== "" or familia[9]== "0"):
		    ingreso = "N/P"
		else:
		    ingreso = familia[9] + " Bs. "
		    
		integrantes.append([str(familia[4]), str(familia[2])+ " " + str(familia[3]), str(familia[7]), str(familia[6]), str(familia[19]),str(familia[11]), str(familia[10]), str(familia[8]), ingreso ])
	
	t=Table(integrantes, (55,150, 60, 35, 35, 50, 80, 80, 45))
		
	t.setStyle([ ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	('BOX', (0,0), (-1,-1), 0.25, colors.black), ('SPAN',(0,0),(8,0))
	 ])
	
	story.append(t)
	story.append(Spacer(0,15))

	
	
	vivienda = self.dbconn.execute("SELECT * FROM vivienda where id_grupo= 1").fetchone()

	datos_vivienda = [[ Paragraph('''<font size=12><b>Características de la vivienda</b></font>''',styleSheet["BodyText"]) ],
		    ['Tipo de Vivienda: ', vivienda[2], 'Estado de la Vivienda: ' , vivienda[3] , 'Tenencia: ', vivienda[4] ],
		    ['Material del Piso: ',vivienda[5] , 'Material de Paredes: ', vivienda[6] ],
		    ['Material Techo: ', vivienda[7],'Habitaciones: ',vivienda[8], 'Sala Comedor: ', vivienda[9] ], 
		    ['Baños', vivienda[10] , 'Cocina: ', vivienda[11], 'Uso de Vivienda: ', vivienda[12]],
		    ['Le gustaria Mejorar: ', vivienda[13]] ]
	
	v=Table(datos_vivienda, (100,100, 110, 100, 90, 90))
	v.setStyle([ ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	('BOX', (0,0), (-1,-1), 0.25, colors.black),('SPAN',(0,0),(5,0)),('SPAN',(3,2),(5,2)),('SPAN',(1,5),(5,5))
	 ])
	story.append(v)
	story.append(Spacer(0,15))	
	

	salud = self.dbconn.execute("SELECT * FROM salud_bienestar where id_familia = 1").fetchone()
	vacuna = "Si" if salud[2] == "S" else "No"
	datos_salud = [[ Paragraph('''<font size=12><b>Salud y Bienestar</b></font>''',styleSheet["BodyText"]) ],
		    ['Los Niños estan vacunados: '+ str(salud[2]), '', 'Solo menores de seis(6) años : ' + str(salud[3]),  '', 'Todos: ' + salud[4], '' ] ]
	
	datos_salud.append( ['De las siguientes vacunas cuales tiene la seguridad de haberles suministrado:' ])

	self.dbconn.execute("SELECT desc_vacuna, id_salud FROM tipos_vacuna LEFT OUTER JOIN vacuna  ON tipos_vacuna.id_tipo_vacuna = vacuna.id_tipo_vacuna")
	rs = self.dbconn.fetchall()
	a = 1
	i = 3
	fila = ""
	
	for vacuna in rs:
	    si_no = "X" if vacuna[1] else ""
	    fila = fila + vacuna[0] + ","+ si_no + ","
	    if (a == i ):
		i = i + 3
		fila = fila[0:-1].split(',')
		datos_salud.append(  fila )
		fila = ""
	    a = a + 1
	
	
	datos_salud.append( ['Algunos de los miembros de la familia a presentado problemas de:' ])

	self.dbconn.execute("SELECT desc_enfermedad, id_salud FROM tipo_enfermedad LEFT OUTER JOIN enfermedad  ON tipo_enfermedad.id_tipo_enfermedad = enfermedad.id_tipo_enfermedad where activa='s'")
	rs = self.dbconn.fetchall()
	a = 1
	i = 3
	fila = ""
	
	for enfermedad in rs:
	    si_no = "X" if enfermedad[1] else ""
	    fila = fila + enfermedad[0] + ","+ si_no + ","
	    if (a == i ):
		i = i + 3
		fila = fila[0:-1].split(',')
		datos_salud.append(  fila )
		fila = ""
	    a = a + 1
	
	v=Table(datos_salud, (120,90, 110, 90, 90, 90))
	v.setStyle([ ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),	('BOX', (0,0), (-1,-1), 0.25, colors.black),
	    ('SPAN',(0,0),(5,0)), ('SPAN',(0,1),(1,1)), ('SPAN',(2,1),(3,1)),('SPAN',(4,1),(5,1)), ('SPAN',(0,2),(5,2)),('SPAN',(0,6),(5,6)) ])


	story.append(v)
	story.append(Spacer(0,25))		


	
	servicios = self.dbconn.execute("SELECT * FROM servicios_publicos where familia = 1").fetchone()

	serv_publicos = [[ Paragraph('''<font size=12><b>Servicios Publicos Existentes</b></font>''',styleSheet["BodyText"]) ],
		    ['Aguas Blancas: ', servicios[1], 'Aguas Servidas: ' , servicios[2] , 'Gas: ', servicios[3] ],
		    ['Sistema Electrico: ',servicios[4] , 'Recolección de Basura: ', servicios[5] ],
		    ['Otros Servicios: '],
		    ['Telefonía: ', servicios[6],'Transporte: ',servicios[7] ], 
		    ['Mecanismos de Información: ', '', servicios[8] ] ]
	
	s=Table(serv_publicos, (90,100, 115, 100, 90, 90))
	s.setStyle([ ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	('BOX', (0,0), (-1,-1), 0.25, colors.black),('SPAN',(0,0),(5,0)),('SPAN',(0,3),(5,3)),('SPAN',(0,5),(1,5)) ,('SPAN',(2,5),(5,5)) ])
	story.append(s)
	story.append(Spacer(0,15))
	
	par_comunitaria = [[ Paragraph('''<font size=12><b>Participacion Comunitaria</b></font>''',styleSheet["BodyText"]) ],
		    ['Existe organización Comunitaria: ', servicios[9] ],
		    ['Participación del jefe de familia: ', servicios[13] ],
		    ['Participación de los miembros de familia: ', servicios[10] ] ]
	s=Table(par_comunitaria, (200, 385))
	s.setStyle([ ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	('BOX', (0,0), (-1,-1), 0.25, colors.black),('SPAN',(0,0),(1,0)) ])
	story.append(s)
	story.append(Spacer(0,15))
	
	doc=SimpleDocTemplate(pdf_x_familia, pagesize=letter,leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10,
			      title="Komunal - Planilla Familiar", author= "Komunal Beta" )
	doc.build( story )
	self.funciones.generar_log(self, "Se genero planilla pdf de familia = "+ str(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()) + " el usuario lo guardo en: " + pdf_x_familia )

    
  
    

    def	generarPlanillaFamilia2(self):
	self.dbconn.execute("SELECT * FROM familia where id_grupo= " + str( self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text() ) +" AND jefe_familia= 'N'")
	rs = self.dbconn.fetchall()
	pdf_x_familia = QtGui.QFileDialog.getSaveFileName(self, "Guardar Planilla Komunal (*.pdf)", QtCore.QDir.homePath() + "/familia-" + str(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()) + ".pdf", "Documento PDF (*.pdf)")
	pdf = canvas.Canvas(pdf_x_familia, pagesize=letter)
	pdf.setLineWidth(.3)
	pdf.setFont('Helvetica', 12)

	pdf.drawImage("img/komunal-logo-beta.png",50,700,200,75)

	pdf.drawString(80,750,'JEFE FAMILIA')
	pdf.drawString(80,735,'INTEGRANTES DE FAMILIA')
	pdf.drawString(500,750,"29/05/2012")
	pdf.line(480,747,580,747)

	pdf.drawString(275,725,'NOMBRE:')
	pdf.drawString(500,725,"FECHA NACIMIENTO")
	pdf.line(378,723,580,723)

	pdf.drawString(80,703,'NOMBRES:')
	pdf.line(120,700,580,700)
	pdf.drawString(120,703,"LENIN HERNANDEZ")
	
	pdf.drawString(20, 530, 'Nombre / Apellido')
	pdf.drawString(120, 530, 'C.I')
	pdf.drawString(190, 530, 'Edad')

	y = 500
	
	for familia in rs:
	    print str(y) + str(familia[2]) + str(familia[3])
	    pdf.line(120,700,395,148)
	    
	    pdf.drawString(20, y, str(familia[2]) + " " + str(familia[3]) )
	    pdf.drawString(120, y, str(familia[4]))
	    pdf.drawString(190, y, str(familia[5]))
	    
	    y = y - 15


	pdf.save()


    def indicadoresKomunal(self):
	self.dlg_indicadores = DlgIndicadores()
	self.dlg_indicadores.show()
	self.dlg_indicadores.ui.lblMayor60.setText( str(self.dbconn.execute("SELECT count(a.fecha_nacimiento) from familia a where fecha_nacimiento < Date('now', '-60 year') AND a.co_consejo=1").fetchone()[0]) )
	self.dlg_indicadores.ui.lblNino.setText( str(self.dbconn.execute("SELECT count(a.fecha_nacimiento) from familia a where fecha_nacimiento between Date('now', '-12 year') and Date('now', '-3 year') AND a.co_consejo=1").fetchone()[0]) )
	self.dlg_indicadores.ui.lblAlfabetizada.setText(str(self.dbconn.execute("select count(a.id) from familia a where a.instruccion='N/P' and fecha_nacimiento < Date('now', '-7 year')").fetchone()[0]) )
	self.dlg_indicadores.ui.lblCantAdolecentes.setText( str(self.dbconn.execute("SELECT count(a.fecha_nacimiento) from familia a where fecha_nacimiento between Date('now', '-17 year') and Date('now', '-13 year') AND a.co_consejo=1").fetchone()[0]) )
	self.dlg_indicadores.ui.lblTotalPersonas.setText( str(self.dbconn.execute("SELECT count(*) from familia where co_consejo=1").fetchone()[0]) )
	personas = self.dbconn.execute("select count(id) as cant_perso,  (select count(sexo) from familia where sexo='F' and co_consejo=1) as cant_mujer,(select count(sexo) from familia where sexo='M' and co_consejo=1) as cant_hombre from familia where co_consejo=1").fetchone()
	self.dlg_indicadores.ui.lblPersonasComunidad.setText( str(personas[0]) )
	self.dlg_indicadores.ui.lblSexoMasculino.setText( str(personas[2]) )
	self.dlg_indicadores.ui.lblSexoFemenino.setText( str(personas[1]) )

	return


    def acercaKomunal(self):
	self.frm_about4 = about2()
	self.frm_about4.show()
	return

    def frmConcejoComunal(self):
	self.login.close()
	self.frm_concejo = concejoComunal()
	self.frm_concejo.show()
	print str(self.frm_concejo.ui.textDireccionConsejo.selectAll() ) + "aqui"
	return

    def modificarConcejoComunal(self  ):
	self.frm_concejo = concejoComunal()
	self.frm_concejo.show()
	self.frm_concejo.llenarCamposmodificarConsejo( gidconsejo, gidusuario)
	return	


    def listadoFamilias(self):

	return


    def guardarJefeFamilia(self):

	self.funciones.limpiar_formularios(self,"txtCedulaJefe")

	digito= self.ui.txtCedulaJefe.text()
	if str(digito).isdigit():
		print str(digito)
	else:
		self.ui.lblErrorCedulaJefe.setText("Solo digitos")
		self.ui.txtCedulaJefe.setStyleSheet("background-color: #FFD8D8")
		self.ui.txtCedulaJefe.setFocus()
		print "No es digito la cedula"

	if (self.ui.txtNombrejefe.text() == ''):
	    self.ui.lblErrorNombreJefe.setText("Campo Requerido")
	    self.ui.txtNombrejefe.setStyleSheet("background-color: #FFD8D8")
	    self.ui.txtNombrejefe.setFocus()

	elif (self.ui.txtApellidojefe.text() == ''):
	    self.ui.lblErrorApellidoJefe.setText("Campo Requerido")
	    self.ui.txtApellidojefe.setStyleSheet("background-color: #FFD8D8")
	    self.ui.txtApellidojefe.setFocus()

	elif (self.ui.txtCedulaJefe.text() == ''):
	    self.ui.lblErrorCedulaJefe.setText("Campo Requerido")
	    self.ui.txtCedulaJefe.setStyleSheet("background-color: #FFD8D8")
	    self.ui.txtCedulaJefe.setFocus()

	elif (self.ui.txtFechaNacJefe.text() == '01-01-2000'):
	    self.ui.lblErrorFechaJefe.setText("Campo Requerido")
	    self.ui.txtFechaNacJefe.setStyleSheet("background-color: #FFD8D8")
	    self.ui.txtFechaNacJefe.setFocus()

	elif (self.ui.txtOcupacionJefe.text() == ''):
	    self.ui.lblErrorOcupacionJefe.setText("Campo Requerido")
	    self.ui.txtOcupacionJefe.setStyleSheet("background-color: #FFD8D8")
	    self.ui.txtOcupacionJefe.setFocus()

	elif (self.ui.txtIngresoJefe.text() == ''):
	    self.ui.lblErrorIngresosJefe.setText("Campo Requerido")
	    self.ui.txtIngresoJefe.setStyleSheet("background-color: #FFD8D8")
	    self.ui.txtIngresoJefe.setFocus()




	else:
	    global gidusuario
	    global gidconsejo
	    sexoJefe = "M" if self.ui.cmbSexoJefe.currentText() == "Masculino" else "F"
	    nacionalidadJefe = "V" if self.ui.cmbNacionalidadJefe.currentText() == "Venezolano" else "E"

	    sql = "INSERT INTO familia ('co_consejo','nombre', 'apellido', 'cedula', 'fecha_nacimiento', 'sexo',  'parentezco', 'ocupacion', 'edo_civil','nacionalidad','ingreso', 'instruccion','jefe_familia','id_grupo','id_usuario') VALUES( "
	    sql = sql + "'" + str( gidconsejo) + "',"
	    sql = sql + "'" + self.ui.txtNombrejefe.text() + "'"
	    sql = sql + ",'" + self.ui.txtApellidojefe.text() + "'"
	    sql = sql + ",'" + self.ui.txtCedulaJefe.text() + "'"
	    sql = sql + ",'" + self.ui.txtFechaNacJefe.dateTime().toString("yyyy-MM-dd") + "'"
	    sql = sql + ",'" + sexoJefe + "'"
	    sql = sql + ",'jefe_familia'"
	    sql = sql + ",'" + self.ui.txtOcupacionJefe.text() + "'"
	    sql = sql + ",'" + self.ui.cmbEdoCivilJefe.currentText() + "'"
	    sql = sql + ",'" + nacionalidadJefe + "'"
	    sql = sql + ",'" + self.ui.txtIngresoJefe.text() + "'"
	    sql = sql + ",'" + self.ui.cmbGradoInstruccion.currentText() + "'"
	    sql = sql + ",'S'"
	    sql = sql + ",'" + str(self.dbconn.execute("SELECT seq FROM sqlite_sequence where name = 'familia'").fetchone()[0]+1) + "'"
	    sql = sql + "," + str( gidusuario) + ")"
	    try:
		self.dbconn.execute(str(sql))
		self.db.commit()
		self.ui.lblNotificacionJefeFamilia.setVisible(True)
		self.ui.lblNotificacionJefeFamilia.setText("<b>Los datos del jefe de familia "+str(self.ui.txtNombrejefe.text())+ " " +str(self.ui.txtApellidojefe.text()) +" fueron guardados exitosamente!</b>")
		self.actualizarGrid()
		self.funciones.generar_log(self, "Fue registrado "+ self.ui.txtCedulaJefe.text() + " como jefe de familia. " + str(sql) )

	    except:
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Ocurrio un error", "Ocurrio un error Guardando los datos del jefe de familia").exec_()
		self.funciones.generar_log(self, "Ocurrio un error registrando un jefe de familia. " + str(sql) )
		print sql
		return

	print sql


    def modificarJefeFamilia(self):
	if (self.ui.txtCedulaJefe.text() == ''):
	    QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "La cedula de identidad no puede estar vacia").exec_()
	else:
	    sexoJefe = "M" if self.ui.cmbSexoJefe.currentText() == "Masculino" else "F"
	    nacionalidadJefe = "V" if self.ui.cmbNacionalidadJefe.currentText() == "Venezolano" else "E"
	    sql = "UPDATE familia set "
	    sql = sql+"nombre='"+str(self.ui.txtNombrejefe.text())+"', "
	    sql = sql+"apellido='"+str(self.ui.txtApellidojefe.text())+"', "
	    sql = sql+"sexo='"+ sexoJefe +"', "
	    sql = sql+"fecha_nacimiento='"+str(self.ui.txtFechaNacJefe.dateTime().toString("yyyy-MM-dd"))+"', "
	    sql = sql+"ocupacion='"+str(self.ui.txtOcupacionJefe.text())+"', "
	    sql = sql+"edo_civil='"+str(self.ui.cmbEdoCivilJefe.currentText())+"', "
	    sql = sql+"nacionalidad='"+ nacionalidadJefe +"', "
	    sql = sql+"ingreso='"+str(self.ui.txtIngresoJefe.text())+"', "
	    sql = sql+"instruccion='"+str(self.ui.cmbGradoInstruccion.currentText())+"' "
	    sql = sql+" WHERE cedula=" + str(self.ui.txtCedulaJefe.text())
	    try:
		self.dbconn.execute(str(sql))
		self.db.commit()
		self.ui.lblNotificacionJefeFamilia.setVisible(True)
		self.ui.lblNotificacionJefeFamilia.setText("<b>Los datos del jefe de familia "+str(self.ui.txtNombrejefe.text())+" "+ str(self.ui.txtApellidojefe.text()) +" fueron modificados exitosamente!</b>")
		self.actualizarGrid()
		self.funciones.generar_log(self, "Fue modificando el jefe de familia =" +str(self.ui.txtCedulaJefe.text()))
	    except:
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error Modificando", "Ocurrio un error Modificando los datos del jefe de familia").exec_()
		self.funciones.generar_log(self, "Ocurrio un error modificando el jefe de familia =" +str(self.ui.txtCedulaJefe.text())+str(sql))
		print sql
		return

	print sql



    def borrarFamilia(self):
	lineaSeleccionada=self.ui.tableWidget.currentRow()
	if lineaSeleccionada == "":
	    QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Ocurrio un error", "Borrar familia").exec_()

	elementos=[]
	for i in range(3):
	    itemText = self.ui.tableWidget.item(lineaSeleccionada, i).text()
	    print 'itemText: ' + itemText
	    elementos.append(str(itemText))

	reply = QtGui.QMessageBox.question(self, "Confirmación - Eliminar Jefe de Familia",
            "¿Esta realmente seguro de eliminar al jefe de familia de C.I " + elementos[1] +" ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.dbconn.execute('DELETE FROM familia WHERE cedula=? AND co_consejo=? AND id=? ',(elementos[1],1,elementos[0]))
	    self.db.commit()
	    self.actualizarGrid()
	    self.funciones.generar_log(self, "Se elimino la familia cuyo jefe es =" +str(elementos[1])+ " junto a toda su informacion de vivienda, salud, bienestar, y servicios")
        else:
	    print self.ui.tableWidget.currentRow()


    def llenarCamposModificarFamilia(self):
	self.ui.tabWidget.setCurrentIndex(1)
	self.ui.btnModificarJefeFamilia.setVisible(True)
	self.ui.btnGuardarJefeFamilia.setVisible(False)

	self.ui.btnModificarBienestar.setVisible(True)
	self.ui.btnGuardarBienestar_2.setVisible(False)
	lineaSeleccionada=self.ui.tableWidget.currentRow()
	elementos=[]
	for i in range(3):
	    itemText = self.ui.tableWidget.item(lineaSeleccionada, i).text()
	    print 'CAMPO: ' + itemText
	    elementos.append(str(itemText))


	##Llenar campos para modificar de jefe familia
	self.dbconn.execute("SELECT * FROM familia WHERE id=? and cedula=?",(elementos[0],elementos[1]))
	rs = self.dbconn.fetchall()
	self.familiares = {}
	for familiar in rs:
	        print str(familiar[0]) + familiar[2] + familiar[6]
		self.ui.txtCedulaJefe.setText(familiar[4])
		self.ui.txtNombrejefe.setText(familiar[2])
		self.ui.txtApellidojefe.setText(familiar[3])
		self.ui.cmbSexoJefe.setCurrentIndex(0 if familiar[6] == "M" else 1)
		self.ui.txtOcupacionJefe.setText(familiar[8])
		self.ui.cmbEdoCivilJefe.setCurrentIndex(2)
		self.ui.cmbNacionalidadJefe.setCurrentIndex(0 if familiar[12] == "V" else 1)
		self.ui.txtIngresoJefe.setText(familiar[9])

	##Llenar campos para modificar de integrantes familia
	self.dbconn.execute("SELECT * FROM familia WHERE id_grupo=" + elementos[0] + " and jefe_familia='N'")
	rs = self.dbconn.fetchall()
	self.integrante = {}
	i = 0
	for integrante in rs:
	        print str(integrante[2]) + integrante[3] + integrante[4]
		eval("self.ui.lblNombreF"+ str(i+1) + ".setText(integrante[2])")
		eval("self.ui.lblApellidoF"+ str(i+1) + ".setText(integrante[3])")
		eval("self.ui.lblCedulaF"+ str(i+1) + ".setText(integrante[4])")
		#eval("self.ui.lblFechaF"+ str(i+1) + ".setText(familiar[4])")
		eval("self.ui.cmbSexoF"+ str(i+1) + ".setCurrentIndex(0 if integrante[6] == 'M' else 1)")
		eval("self.ui.lblParentescoF"+ str(i+1) + ".setText(integrante[7])")
		eval("self.ui.lblOcupacionF"+ str(i+1) + ".setText(integrante[8])")
		eval("self.ui.lblIngresoF"+ str(i+1) + ".setText(integrante[9])")
		i = i +1

	##Llenar campos de vivienda de la familia
	self.dbconn.execute( "SELECT * FROM vivienda WHERE id_grupo=" + elementos[0] )
	rs = self.dbconn.fetchall()
	for vivienda in rs:
	    print str(vivienda[0]) + vivienda[2] + vivienda[6]
	    self.ui.cmbTipoVivienda.setCurrentIndex(2)
	    self.ui.cmbEstadoVivienda.setCurrentIndex(2)
	    self.ui.cmbMaterialPiso.setCurrentIndex(2)
	    self.ui.cmbMaterialPared.setCurrentIndex(2)
	    self.ui.cmbMaterialTecho.setCurrentIndex(2)
	    self.ui.cmbBanos.setCurrentIndex(2)
	    self.ui.cmbCocina.setCurrentIndex(2)
	    self.ui.cmbUsoVivienda.setCurrentIndex(2)


	##Llenar campos de servicios_basicos
	self.dbconn.execute("SELECT * FROM servicios_publicos WHERE familia=" + elementos[0])
	rs = self.dbconn.fetchall()
	print "SELECT * FROM servicios_publicos WHERE familia=" + str(elementos[0])
	self.servicios = {}
	for servicios in rs:
	        print str(servicios[2]) + servicios[3] + servicios[4]
		self.ui.cmbAguasBlancas_2.setItemText(0,servicios[1])
		self.ui.cmbAguasServidas_2.setItemText(0,servicios[2])
		self.ui.cmbGas_2.setItemText(0,servicios[3])
		self.ui.cmbSistemaElectrico_2.setItemText(0,servicios[4])
		self.ui.cmbRecoleccionBasura_2.setItemText(0,servicios[5])
		self.ui.cmbTelefonia_2.setItemText(0,servicios[6])
		self.ui.cmbTransporte_2.setItemText(0,servicios[7])
		self.ui.cmbMecanismosInformacion_2.setItemText(0,servicios[8])
		self.ui.cmbOrgComunitaria_2.setItemText(0,servicios[9])
		self.ui.cmbPaticipaJefe_2.setItemText(0,servicios[13])
		self.ui.cmbParticipaMiembro_2.setItemText(0,servicios[10])
		self.ui.txteObservaciones_2.setPlainText(servicios[14])





    def guardarMiembrosFamilia(self):
	if (self.ui.txtCedulaJefe.text() == ''):
	    QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "Debe agregar primero un Jefe de Familia").exec_()
	else:
	    global gidusuario
	    global gidconsejo
	    id_grupo = self.dbconn.execute(str("select id from familia where cedula='"+self.ui.txtCedulaJefe.text()+"'")).fetchone()[0]
	    for i in range(8):
		if (eval("self.ui.lblNombreF"+ str(i+1) + ".text()") and eval("self.ui.lblApellidoF"+ str(i+1) + ".text()") and  eval("self.ui.lblCedulaF"+ str(i+1) + ".text()")) :
		    sql = "INSERT INTO familia ('co_consejo','nombre', 'apellido', 'cedula', 'fecha_nacimiento', 'sexo', 'parentezco', 'ocupacion', 'ingreso', 'edo_civil', 'instruccion','nacionalidad', 'jefe_familia', 'id_grupo', 'id_usuario') VALUES( "
		    sql = sql + "'" + str( gidconsejo ) +"'"
		    sql = sql + ",'" + eval("self.ui.lblNombreF"+ str(i+1) + ".text()") + "'"
		    sql = sql + ",'" + eval("self.ui.lblApellidoF"+ str(i+1) + ".text()") + "'"
		    sql = sql + ",'" + eval("self.ui.lblCedulaF"+ str(i+1) + ".text()") + "'"
		    sql = sql + ",'" + eval("self.ui.lblFechaF"+ str(i+1) + ".dateTime().toString('yyyy-MM-dd')") + "'"
		    sql = sql + ",'" + eval("self.ui.cmbSexoF"+ str(i+1) + ".currentText()") + "'"
		    sql = sql + ",'" + eval("self.ui.lblParentescoF"+ str(i+1) + ".text()") + "'"
		    sql = sql + ",'" + eval("self.ui.lblOcupacionF"+ str(i+1) + ".text()") + "'"
		    sql = sql + ",'" + eval("self.ui.lblIngresoF"+ str(i+1) + ".text()") + "'"
		    sql = sql + ",'" + eval("self.ui.cmbEdoCivilF"+ str(i+1) + ".currentText()") + "'"
		    sql = sql + ",'" + eval("self.ui.cmbInstruccionF"+ str(i+1) + ".currentText()") + "'"
		    sql = sql + ",'V'"
		    sql = sql + ",'N'"
		    sql = sql + ",'"+ str( id_grupo ) +"'"
		    sql = sql + ",'" + str( gidusuario ) +"')"
		    try:
			self.dbconn.execute(str(sql))
			self.db.commit()
			self.ui.lblNotificacionGrupoFamiliar.setVisible(True)
			self.ui.lblNotificacionGrupoFamiliar.setText("<b>Los miembros de la familia "+str(self.ui.txtNombrejefe.text())+" "+ str(self.ui.txtApellidojefe.text()) +" fueron agregados exitosamente! :D</b>")
			self.actualizarGrid()
			self.funciones.generar_log(self, "Se registraro el miembro de familia =" +eval("self.ui.lblNombreF"+ str(i+1) + ".text()")+ " " + eval("self.ui.lblApellidoF"+ str(i+1) + ".text()") )

		    except:
			self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
			QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Ocurrio un error", "Guardando los datos de los miembros de familia").exec_()
			self.funciones.generar_log(self, "Ocurrio un error registrando un miembro de familia =" + sql )
			return
		else:
		   continue
		    #i = i +1

    def guardarViviendaFamilia(self):

	if (self.ui.txtCedulaJefe.text() == ''):
	    QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "Debe agregar primero un Jefe de Familia").exec_()
	else:
	    global gidusuario
	    #global gidconsejo
	    id_grupo = self.dbconn.execute(str("select id from familia where cedula='"+self.ui.txtCedulaJefe.text()+"'")).fetchone()[0]

	    sql = "INSERT INTO vivienda ('id_grupo', 'tipo_vivienda', 'estado_vivienda', 'tenencia', 'material_piso',  'material_pared', 'material_techo', 'habitacion', 'sala_comedor','banos','cocina', 'uso_vivienda','mejorar_vivienda', 'id_usuario') VALUES( "
	    sql = sql + "'" +  str( id_grupo ) + "'"
	    sql = sql + ",'" + self.ui.cmbTipoVivienda.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbEstadoVivienda.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbTenencia.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbMaterialPiso.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbMaterialPared.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbMaterialTecho.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbHabitaciones.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbSalaComedor.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbBanos.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbCocina.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbUsoVivienda.currentText() + "'"
    	    sql = sql + ",' '"
	    sql = sql + ",'" + str( gidusuario ) + "')"

	    try:
		self.dbconn.execute(str(sql))
		self.db.commit()
		self.ui.lblNotificacionVivienda.setVisible(True)
		self.ui.lblNotificacionVivienda.setText("<b>La vivienda de la familia de "+str(self.ui.txtNombrejefe.text())+" "+ str(self.ui.txtApellidojefe.text()) +" fueron agregados exitosamente! :D</b>")
		self.actualizarGrid()
		self.funciones.generar_log(self, "Se registro la vivienda de la familia =" + self.ui.txtCedulaJefe.text() )

	    except:
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error guardando vivienda", "Error Guardando los datos de la vivienda familiar").exec_()
		self.funciones.generar_log(self, "Ocurrio un error registrando la vivienda de familia =" + self.ui.txtCedulaJefe.text() + sql )
		return
	    print sql


    def guardarServiciosPublicos(self):

	if (self.ui.txtCedulaJefe.text() == ''):
	    QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "Debe agregar primero un Jefe de Familia").exec_()
	else:
	    sql = "INSERT INTO servicios_publicos ('familia', 'agua_blanca', 'agua_servida', 'gas', 'sistema_electrico',  'recoleccion_basura', 'telefonia', 'transporte', 'mec_informacion','org_comunitaria','participa_jefe', 'participa_miembro') VALUES( "
	    sql = sql + "'" +  self.ui.txtCedulaJefe.text() + "'"
	    sql = sql + ",'" + self.ui.cmbAguasBlancas.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbAguasServidas.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbGas.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbSistemaElectrico.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbRecoleccionBasura.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbTelefonia.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbTransporte.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbMecanismosInformacion.currentText() + "'"
	    sql = sql + ",''"
	    sql = sql + ",''"
	    sql = sql + ",'')"
	    try:
			    self.dbconn.execute(str(sql))
			    self.db.commit()
			    self.funciones.generar_log(self, "Se registraron los servicios publicos para la familia =" + self.ui.txtCedulaJefe.text() )
	    except:
			    print sql
			    self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
			    QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Ocurrio un error", "Guardando los datos de los miembros de familia").exec_()
			    self.funciones.generar_log(self, "Ocurrio un error registrando los servicios publicos de la familia =" + self.ui.txtCedulaJefe.text() + sql )
			    return
	    print sql



    def guardar(self):
	sqlite_db = create_engine('sqlite:////home/lenin/komunal/komunal.db')
	metadata  = MetaData(sqlite_db)
	persona = Table('persona', metadata, autoload=True)
	i = persona.insert()
	nombre = self.ui.lineEdit.text()
	i.execute({'nombre':  str(self.ui.lineEdit_2.text()) , 'apellido':str(self.ui.lineEdit_3.text()), 'cedula':str(self.ui.lineEdit.text()), 'fecha_nacimiento': datetime.date(1985, 10, 15), 'sexo' : 'M', 'created_by' : 'lenin'} )
	self.ui.lineEdit.setText(self.ui.lineEdit.text())
	self.ui.lineEdit_2.setText(self.ui.lineEdit_2.text())
	self.ui.lineEdit_3.setText(self.ui.lineEdit_3.text())
	self.ui.lineEdit_4.setText(self.ui.lineEdit_4.text())


    def guardarBienestar(self):

	if (self.ui.txtCedulaJefe.text() == ''):
	    QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "Debe agregar primero un Jefe de Familia").exec_()
	else:

	    #global gidconsejo
	    id_grupo = self.dbconn.execute(str("select id from familia where cedula='"+self.ui.txtCedulaJefe.text()+"'")).fetchone()[0]

	    sql = "INSERT INTO servicios_publicos ('agua_blanca' ,'agua_servida','gas','sistema_electrico','recoleccion_basura','telefonia','transporte','mec_informacion' ,'org_comunitaria','participa_jefe' ,'participa_miembro','observaciones','familia' ) VALUES( "
	    sql = sql + "'" +  self.ui.cmbAguasBlancas_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbAguasServidas_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbGas_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbSistemaElectrico_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbRecoleccionBasura_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbTelefonia_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbTransporte_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbMecanismosInformacion_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbOrgComunitaria_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbPaticipaJefe_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.cmbParticipaMiembro_2.currentText() + "'"
	    sql = sql + ",'" + self.ui.txteObservaciones_2.toPlainText() + "'"
	    sql = sql + ",'" + str( id_grupo ) + "')"

	    try:
		self.dbconn.execute(str(sql))
		self.db.commit()
		self.ui.lblNotificacionBienestar.setVisible(True)
		self.ui.lblNotificacionBienestar.setText("<b>Los datos fueron agregados exitosamente! :D</b>")
		self.actualizarGrid()
		self.funciones.generar_log(self, "Se registraron los servicios publicos de la familia =" + self.ui.txtCedulaJefe.text() )
		
	    except:
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error guardando servicios basicos", "Error Guardando los datos de los servicios basicos").exec_()
		self.funciones.generar_log(self, "Ocurrio un error registrando los servicios publicos de la familia =" + self.ui.txtCedulaJefe.text() + sql )
		return

    def modificarBienestar(self):
	if (self.ui.txtCedulaJefe.text() == ''):
	    QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "La cedula de identidad no puede estar vacia").exec_()
	else:
	    '''sexoJefe = "M" if self.ui.cmbSexoJefe.currentText() == "Masculino" else "F"
	    nacionalidadJefe = "V" if self.ui.cmbNacionalidadJefe.currentText() == "Venezolano" else "E"'''
	    id_grupo = self.dbconn.execute(str("select id from familia where cedula='"+self.ui.txtCedulaJefe.text()+"'")).fetchone()[0]
	    sql = "UPDATE servicios_publicos set "
	    sql = sql+"agua_blanca='"+str(self.ui.cmbAguasBlancas_2.currentText())+"', "
	    sql = sql+"agua_servida='"+str(self.ui.cmbAguasServidas_2.currentText())+"', "
	    sql = sql+"gas='"+str(self.ui.cmbGas_2.currentText())+"', "
	    sql = sql+"sistema_electrico='"+str(self.ui.cmbSistemaElectrico_2.currentText())+"', "
	    sql = sql+"recoleccion_basura='"+str(self.ui.cmbRecoleccionBasura_2.currentText())+"', "
	    sql = sql+"telefonia='"+str(self.ui.cmbTelefonia_2.currentText())+"', "
	    sql = sql+"transporte='"+str(self.ui.cmbTransporte_2.currentText())+"', "
	    sql = sql+"mec_informacion='"+str(self.ui.cmbMecanismosInformacion_2.currentText())+"', "
	    sql = sql+"org_comunitaria='"+str(self.ui.cmbOrgComunitaria_2.currentText())+"', "
	    sql = sql+"participa_miembro='"+str(self.ui.cmbParticipaMiembro_2.currentText())+"', "
	    sql = sql+"participa_jefe='"+str(self.ui.cmbPaticipaJefe_2.currentText())+"', "
	    sql = sql+"Observaciones='"+str(self.ui.txteObservaciones_2.toPlainText())+"' "
	    sql = sql+" WHERE familia=" + str( id_grupo )
	    try:
		self.dbconn.execute(str(sql))
		self.db.commit()
		self.ui.lblNotificacionBienestar.setVisible(True)
		self.ui.lblNotificacionBienestar.setText("<b>Los datos de servicios basicos del jefe de familia "+str(self.ui.txtNombrejefe.text())+" "+ str(self.ui.txtApellidojefe.text()) +" fueron modificados exitosamente!</b>")
		self.actualizarGrid()
		self.funciones.generar_log(self, "Fueron registrados los servicios publicos de la familia =" + self.ui.txtCedulaJefe.text() )		
	    except:
		self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error Modificando", "Ocurrio un error Modificando los datos de servicios basicos ").exec_()
		self.funciones.generar_log(self, "Ocurrio un error modificando los servicios publicos de la familia =" + self.ui.txtCedulaJefe.text() + sql )
		return

	print sql

    def guardarSalud(self):

	if (self.ui.txtCedulaJefe.text() == ''):
	    QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "Debe agregar primero un Jefe de Familia").exec_()
	else:

	    #global gidconsejo
            id_grupo = self.dbconn.execute(str("select id from familia where cedula='"+self.ui.txtCedulaJefe.text()+"'")).fetchone()[0]
            if (self.ui.rbtSiTienen.isChecked()):
                #QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Komunal - Advertencia", "accepto exitosamente").exec_()
                vacuna = 'S'
                if (self.ui.chbAll_ninos.isChecked()):
                    all_nino='true'
                    print all_nino
                else:
                    all_nino='false'
                    print all_nino
                if (self.ui.chbMenoresSeis.isChecked()):
                    menor_seis='true'
                    print menor_seis
                else:
                    menor_seis='false'
                    print menor_seis



                print vacuna
            else:
                vacuna = 'N'
                print vacuna

            if(self.ui.rbtSiOperacion.isChecked()):
                atencion='S'
                cuanto=self.ui.txtCuantos.text()
                print cuanto
                tipo_opera=self.ui.txtTipoOperacion.text()
                print tipo_opera
            else:
                atencion='N'
                cuanto='N/P'
                print cuanto
                tipo_opera='N/P'
                print tipo_opera

            if(self.ui.rbtSiDiscapacidad.isChecked()):
                discapacitado='S'
                print tipo_opera
            else:
                discapacitado='N'
                print discapacitado

        problema_enfer='N'

        sql = "INSERT INTO salud_bienestar ('vacuna','all_vacuna_nino','menores_seis_ano','problemas_enfermedad','atencion_quirurgica', 'cant_quirurgico', 'tipo_operacion','discapacitado','id_familia' ) VALUES( "
        sql = sql + "'" +  str( vacuna ) + "'"
        sql = sql + ",'" + str( all_nino ) + "'"
        sql = sql + ",'" + str( menor_seis ) + "'"
        sql = sql + ",'" + str( problema_enfer ) + "'"
        sql = sql + ",'" + str( atencion ) + "'"
        sql = sql + ",'" + str( cuanto ) + "'"
        sql = sql + ",'" + str( tipo_opera ) + "'"
        sql = sql + ",'" + str( discapacitado ) + "'"
        sql = sql + ",'" + str( id_grupo ) + "')"

        try:
            self.dbconn.execute(str(sql))
            self.db.commit()
            self.ui.lblNotificacionSalud.setVisible(True)
            self.ui.lblNotificacionSalud.setText("<b>Los datos de salud del grupo familiar, fueron agregados exitosamente! :D</b>")
            self.actualizarGrid()
	    self.funciones.generar_log(self, "Fue registrada la información de salud de la familia =" + self.ui.txtCedulaJefe.text() )
	except:
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error guardando servicios basicos", "Error Guardando los datos de salud del grupo familiar").exec_()
	    self.funciones.generar_log(self, "Ocurrio un error registrando la informacion de salud de la familia =" + self.ui.txtCedulaJefe.text() + sql )	    
            return




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    #splash_pix = QPixmap('img/komunal-logo-beta.png')
    #splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    #splash.setMask(splash_pix.mask())
    #splash.show()
    #time.sleep(2) #Simular que toma tiempo abrir la aplicacion
    #myapp.show()
    #splash.finish(myapp)
    sys.exit(app.exec_())
