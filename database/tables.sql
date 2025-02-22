CREATE TABLE PROFESORES
(
	id_profesor SMALLINT AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
	apellidos VARCHAR(20) NOT NULL,
	email VARCHAR(20) NOT NULL,
	ADD CONSTRAINT pk_key PRIMARY KEY (id_profesor)

)

CREATE TABLE ALUMNOS
(
	id_alumno SMALLINT AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
	apellidos VARCHAR(20) NOT NULL,
	email VARCHAR(20) NOT NULL,
	ADD CONSTRAINT pk_key PRIMARY KEY (id_alumno)
)

CREATE TABLE CLASESPROFESOR
(
	id_profesor SMALLINT,
	id_clase SMALLINT,
	ADD CONSTRAINT pk_key PRIMARY KEY (id_profesor, id_clase),
	ADD CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_profesor) REFERENCES PROFESORES(id_profesor)
)


CREATE TABLE CLASESALUMNO
(
	id_alumno SMALLINT,
	id_clase SMALLINT,
	ADD CONSTRAINT pk_key PRIMARY KEY (id_alumno, id_clase),
	ADD CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_alumno) REFERENCES ALUMNOS(id_alumno)
)
CREATE TABLE PROFESORALUMNO
(

	id_profesor SMALLINT,
	id_alumno SMALLINT,
	ADD CONSTRAINT pk_key PRIMARY KEY (if_profesor, id_alumno),
	ADD CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_profesor) REFERENCES PROFESORES(id_profesor),
	ADD CONSTRAINT fg_key_to_profesores FOREIGN KEY (id_alumno) REFERENCES ALUMNOS(id_alumno)
)