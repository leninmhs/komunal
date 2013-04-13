#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, datetime
import traceback
import logging
import inicial
from inicial import *
from bienvenida import *
from PyQt4 import QtCore, QtGui

class GenerarPdf(object):

    def generarPlanillaFamiliaX(self, parent, ruta_pdf):
	from reportlab.lib.pagesizes import A4
	from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
	from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
	from reportlab.platypus import Paragraph, Image
	from reportlab.lib import colors
	
	
	print parent.ui.tableWidget.item(parent.ui.tableWidget.currentRow(), 1)
	print parent.ui.tableWidget.currentRow() 
	#print str(parent.ui.tableWidget.item(parent.ui.tableWidget.currentRow(), 1).text())
	#pdf_x_familia = QtGui.QFileDialog.getSaveFileName(self, "Guardar Planilla Komunal (*.pdf)", QtCore.QDir.homePath() + "/familia-" + str(parent.ui.tableWidget.item(parent.ui.tableWidget.currentRow(), 1).text()) + ".pdf", "Documento PDF (*.pdf)")
	pdf_x_familia = "Mejorando.pdf"
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
	
	consejo = parent.dbconn.execute("select * from consejo_comunal where id_consejo=1").fetchone()
	
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
	
	
	
	jefe = parent.dbconn.execute("SELECT *, (Date('now') -fecha_nacimiento) as edad FROM familia where id_grupo= 1 AND jefe_familia= 'S'").fetchone()

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



	#self.dbconn.execute("SELECT * FROM familia where id_grupo= " + str( self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text() ) +" AND jefe_familia= 'N'")
	parent.dbconn.execute("SELECT *, (Date('now') -fecha_nacimiento) as edad FROM familia where id_grupo= 1 AND jefe_familia= 'N'")
	rs = parent.dbconn.fetchall()
	
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

	
	
	vivienda = parent.dbconn.execute("SELECT * FROM vivienda where id_grupo= 1").fetchone()

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
	

	salud = parent.dbconn.execute("SELECT * FROM salud_bienestar where id_familia = 1").fetchone()
	vacuna = "Si" if salud[2] == "S" else "No"
	datos_salud = [[ Paragraph('''<font size=12><b>Salud y Bienestar</b></font>''',styleSheet["BodyText"]) ],
		    ['Los Niños estan vacunados: '+ str(salud[2]), '', 'Solo menores de seis(6) años : ' + str(salud[3]),  '', 'Todos: ' + salud[4], '' ] ]
	
	datos_salud.append( ['De las siguientes vacunas cuales tiene la seguridad de haberles suministrado:' ])

	parent.dbconn.execute("SELECT desc_vacuna, id_salud FROM tipos_vacuna LEFT OUTER JOIN vacuna  ON tipos_vacuna.id_tipo_vacuna = vacuna.id_tipo_vacuna")
	rs = parent.dbconn.fetchall()
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

	parent.dbconn.execute("SELECT desc_enfermedad, id_salud FROM tipo_enfermedad LEFT OUTER JOIN enfermedad  ON tipo_enfermedad.id_tipo_enfermedad = enfermedad.id_tipo_enfermedad where activa='s'")
	rs = parent.dbconn.fetchall()
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


	
	servicios = parent.dbconn.execute("SELECT * FROM servicios_publicos where familia = 1").fetchone()

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
	
	doc=SimpleDocTemplate(pdf_x_familia,pagesize=letter,leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10,
			      title="Komunal - Planilla Familiar", author= "Komunal Beta" )
	#doc.build(Document, onLaterPages=HeaderFooter) 
	doc.build( story )
	#exit()
    
    
	#def HeaderFooter( canvas, doc):
	#canvas.saveState()
	
	#canvas.setFont('Times-Roman', 9)
	#canvas.drawString(280, 43, "Page %d" % doc.page)
	#canvas.drawImage("rezilabs.bmp", 43,820, width=1.3*inch,height=0.2*inch)
	#canvas.drawImage("RezayatLogo.bmp", 470,820, width=1.5*inch,height=0.3*inch)
	#img=Image("img/komunal-logo-beta.png",width=80,height=100)
	#img.hAlign = "LEFT"
	#story.append(img)
	#canvas.restoreState() 
    
