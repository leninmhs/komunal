-- Describe VIVIENDA
CREATE TABLE vivienda
(
id_vivienda integer PRIMARY KEY AUTOINCREMENT NOT NULL,
familia text,
tipo_vivienda text,
estado_vivienda text,
tenencia text,
material_piso text,
material_pared text,
material_techo text,
habitacion integer,
sala_comedor integer,
banos integer,
cocina integer,
uso_vivienda text, 
mejorar_vivienda text
)

CREATE TABLE familia 
(
id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre VARCHAR NOT NULL ,
apellido VARCHAR NOT NULL ,
cedula VARCHAR NOT NULL ,
fecha_nacimiento DATETIME,
sexo CHAR NOT NULL ,
parentezco VARCHAR NOT NULL ,
edad VARCHAR,"ocupacion" TEXT,
ingreso TEXT,"instruccion" TEXT,
edo_civil TEXT,
nacionalidad TEXT,
jefe_familia TEXT,
creado_en DATETIME DEFAULT (CURRENT_TIMESTAMP) 
)

