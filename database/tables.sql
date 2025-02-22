CREATE TABLE PROFESORES
(
	id_profesor SMALLINT AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
	apellidos VARCHAR(20) NOT NULL,
	email VARCHAR(20) NOT NULL,
	CONSTRAINT pk_key_profesores PRIMARY KEY (id_profesor)

)

CREATE TABLE ALUMNOS
(
	id_alumno SMALLINT AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
	apellidos VARCHAR(20) NOT NULL,
	email VARCHAR(20) NOT NULL,
	CONSTRAINT pk_key_alumnos PRIMARY KEY (id_alumno)
)

CREATE TABLE CLASESPROFESOR
(
	id_profesor SMALLINT,
	id_clase SMALLINT,
	CONSTRAINT pk_key_clasesprofesor PRIMARY KEY (id_profesor, id_clase),
	CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_profesor) REFERENCES PROFESORES(id_profesor)
)


CREATE TABLE CLASESALUMNO
(
	id_alumno SMALLINT,
	id_clase SMALLINT,
	CONSTRAINT pk_key_clasesalumno PRIMARY KEY (id_alumno, id_clase),
	CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_alumno) REFERENCES ALUMNOS(id_alumno)
)
CREATE TABLE PROFESORALUMNO
(

	id_profesor SMALLINT,
	id_alumno SMALLINT,
	CONSTRAINT pk_key_profesoralumno PRIMARY KEY (id_profesor, id_alumno),
	CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_profesor) REFERENCES PROFESORES(id_profesor),
	CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_alumno) REFERENCES ALUMNOS(id_alumno)
)