# -*- coding: utf-8 -*-

from dlgindicadores import *

class DlgIndicadores(QtGui.QDialog):

	def __init__(self, parent=None):
			
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_DlgIndicadores()
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
		
		
		self.connect(self.ui.btnGenerarPDF, QtCore.SIGNAL('clicked()'),self.generarReporteIndicadores)

  
	
	#para el reporte en pdf de la pantalla de indicadores
	
	def generarReporteIndicadores(self):
	    print "Aqui en pdf"
	    from reportlab.lib.pagesizes import A4
	    from reportlab.lib.pagesizes import letter
	    from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
	    from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
	    from reportlab.platypus import Paragraph, Image
	    from reportlab.lib import colors
	    
	    pdf_x_indicador = QtGui.QFileDialog.getSaveFileName(self, "Guardar Planilla Komunal (*.pdf)", QtCore.QDir.homePath() + "/indicadores-komunal.pdf", "Documento PDF (*.pdf)")
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
    
	    style_fecha= ParagraphStyle('',
			 fontSize = 11,
			 textColor = '#000',
			 leftIndent = 500,
			 rightIndent = 10)
    
	    h = Paragraph( texto_principal, estilo_texto)
	    banner = [ [ img , h ] ]

	    ban = Table( banner )
	    ban.setStyle([ ('ALIGN',(0,0),(0,0),'LEFT'),('ALIGN',(0,0),(1,0),'LEFT'), ('VALIGN',(0,0),(1,0),'TOP'),
			    ('TEXTCOLOR',(0,1),(0,-1), colors.blue) ])
	    story.append(ban)
	    story.append(Spacer(0,10))
    
	    #dia = time.localtime()
	    #mes = dia.tm_mon
	    #mes_sp = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre']
     
	    #hoy='%s %d' % (mes_sp[mes-1], dia.tm_year)
	    #P= Paragraph(hoy,style_fecha)
	    #story.append(P)
	    #story.append(Spacer(0,25))
    
	    P= Paragraph("<b>Reporte de Indicadores</b> ",otro_estilo)
	    story.append(P)
	    story.append(Spacer(0,25))
	    
	    mayor_60 = self.dbconn.execute("SELECT count(a.fecha_nacimiento) from familia a where fecha_nacimiento < Date('now', '-60 year') AND a.co_consejo=1").fetchone()
    
	    ninos = self.dbconn.execute("SELECT count(a.fecha_nacimiento) from familia a where fecha_nacimiento between Date('now', '-12 year') and Date('now', '-3 year') AND a.co_consejo=1").fetchone()
    
	    personas = self.dbconn.execute("select count(id) as cant_perso,  (select count(sexo) from familia where sexo='F' and co_consejo=1) as cant_mujer,(select count(sexo) from familia where sexo='M' and co_consejo=1) as cant_hombre from familia where co_consejo=1").fetchone()
    
	    familias = self.dbconn.execute("SELECT count(id) FROM familia WHERE jefe_familia='S' AND co_consejo=1").fetchone()
    
	    adolecentes = self.dbconn.execute("SELECT count(a.fecha_nacimiento) from familia a where fecha_nacimiento between Date('now', '-17 year') and Date('now', '-13 year') AND a.co_consejo=1").fetchone()
    
	    alfabetizados = self.dbconn.execute("select count(a.id) from familia a where a.instruccion='N/P' and fecha_nacimiento < Date('now', '-7 year')").fetchone()
	    
	    data_indicador = [['Personas Mayores de 60 Años: ', mayor_60[0] ],
			     ['Niños entre 3 y 12 años: ', ninos[0] ],
			     ['Personas del Sexo Masculino: ', personas[2] ],
			     ['Personas del Sexo Femenino: ', personas[1] ],
			     ['Cantidad de Familias: ', familias[0] ],
			     ['Adolecentes (entre 13 y 17 años): ', adolecentes[0] ],
			     ['Personas Alfabetizadas: ', alfabetizados[0] ],
			     ['Total de Personas en el Consejo: ', personas[0] ]]
	
	    anchocolumna = (350, 80)
	    c=Table(data_indicador, anchocolumna )
	    c.setStyle([  ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
			  ('BOX', (0,0), (-1,-1), 0.25, colors.black)		       ])	
	    story.append(c)
	    story.append(Spacer(0,15))
	    
    
	    style=styleSheet['BodyText']
    
	    doc=SimpleDocTemplate(pdf_x_indicador,pagesize=letter,leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10, title="Komunal - Reporte de Indicadores", author= "Komunal Beta" )
	    doc.build( story )

		#Icono del boton salir
		#icon = QtGui.QIcon()
		#icon.addPixmap(QtGui.QPixmap("./themes/default/16x16/dialog-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		#self.ui.btnSalir.setIcon(icon)

		#self.ui.textLabel1.setOpenExternalLinks(1)
		#self.ui.textLabel1.setText(str("Komunal\n\nCopyright: (C) 2012 \n\n Sistema para la Gestión del Censo Socioeconómico de los Consejos Comunales \n\n Python + QT4 + SQLite"))

		#self.ui.tabWidget4.setCurrentIndex(0)
		#self.ui.lblMayor60.setText("<b>Komunal </b>")
		#self.ui.lblMenor3.setText("<b> 6 niños de dios</b>")

	def version(self,version):
		self.ui.lblName.setText("<b>Komunal "+str(version)+"</b>")
