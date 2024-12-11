from apps.inscripciones.models import Curso, PadreTutor
from apps.alumno.models import Alumno
from apps.administracion.models import Genero, Turno, Nacionalidad, Docente
from datetime import date

alumnos = [
    ('Juan', 'Pérez', '10000048', None, 1, '2005-06-15', 1, 'juan.perez48@mail.com', '555-1234567', 'Calle Ficticia 123', 1, 1),
    ('María', 'Gómez', '10000049', None, 2, '2006-02-10', 2, 'maria.gomez49@mail.com', '555-2345678', 'Avenida Imaginaria 456', 2, 2),
    ('Pedro', 'Ruiz', '10000050', None, 1, '2004-11-22', 3, 'pedro.ruiz50@mail.com', '555-3456789', 'Calle Real 789', 3, 1),
    ('Lucía', 'Sánchez', '10000051', None, 2, '2005-03-18', 4, 'lucia.sanchez51@mail.com', '555-4567890', 'Calle del Sol 101', 4, 2),
    ('Carlos', 'Martínez', '10000052', None, 1, '2006-08-30', 5, 'carlos.martinez52@mail.com', '555-5678901', 'Calle del Mar 102', 5, 1),
    ('Ana', 'García', '10000053', None, 2, '2005-12-05', 6, 'ana.garcia53@mail.com', '555-6789012', 'Calle Mayor 103', 6, 2),
    ('Luis', 'Hernández', '10000054', None, 1, '2006-04-25', 1, 'luis.hernandez54@mail.com', '555-7890123', 'Calle del Árbol 104', 7, 1),
    ('Patricia', 'López', '10000055', None, 2, '2005-09-13', 2, 'patricia.lopez55@mail.com', '555-8901234', 'Calle del Río 105', 8, 2),
    ('Marta', 'Vázquez', '10000056', None, 1, '2004-12-01', 3, 'marta.vazquez56@mail.com', '555-9981723', 'Calle de la Luna 106', 9, 1),
    ('Ricardo', 'Ramírez', '10000057', None, 2, '2006-07-01', 4, 'ricardo.ramirez57@mail.com', '555-1012345', 'Calle de los Pinos 107', 10, 2),
    ('Jorge', 'Álvarez', '10000058', None, 1, '2005-11-17', 5, 'jorge.alvarez58@mail.com', '555-1123456', 'Calle Santa Fe 108', 11, 1),
    ('Silvia', 'Mendoza', '10000059', None, 2, '2006-01-10', 6, 'silvia.mendoza59@mail.com', '555-1234568', 'Calle Argentina 109', 12, 2),
    ('Daniel', 'Torres', '10000060', None, 1, '2005-02-15', 1, 'daniel.torres60@mail.com', '555-1345679', 'Calle Libertad 110', 13, 1),
    ('Laura', 'Jiménez', '10000061', None, 2, '2006-03-20', 2, 'laura.jimenez61@mail.com', '555-1456789', 'Calle Rosas 111', 14, 2),
    ('Roberto', 'González', '10000062', None, 1, '2004-05-25', 3, 'roberto.gonzalez62@mail.com', '555-1567890', 'Calle Nueva 112', 15, 1),
    ('Verónica', 'Díaz', '10000063', None, 2, '2006-06-30', 4, 'veronica.diaz63@mail.com', '555-1678901', 'Calle del Parque 113', 16, 2),
    ('Héctor', 'Martín', '10000064', None, 1, '2005-10-03', 5, 'hector.martin64@mail.com', '555-1789012', 'Calle San Martín 114', 17, 1),
    ('Beatriz', 'Paredes', '10000065', None, 2, '2006-09-15', 6, 'beatriz.paredes65@mail.com', '555-1890123', 'Calle San Juan 115', 1, 2),
    ('Emilio', 'Gutiérrez', '10000066', None, 1, '2004-07-18', 1, 'emilio.gutierrez66@mail.com', '555-1901234', 'Calle Zapiola 116', 2, 1),
    ('Susana', 'Romero', '10000067', None, 2, '2005-08-23', 2, 'susana.romero67@mail.com', '555-2012345', 'Calle Lomas 117', 3, 2),
    ('Luis', 'Ríos', '10000068', None, 1, '2006-05-17', 3, 'luis.rios68@mail.com', '555-2123456', 'Calle Central 118', 4, 1),
    ('Sandra', 'Vera', '10000069', None, 2, '2005-01-21', 4, 'sandra.vera69@mail.com', '555-2234567', 'Calle del Norte 119', 5, 2),
    ('Juan', 'Vega', '10000070', None, 1, '2004-10-10', 5, 'juan.vega70@mail.com', '555-2345678', 'Calle Sol 120', 6, 1),
    ('Carmen', 'Hernández', '10000071', None, 2, '2006-12-25', 6, 'carmen.hernandez71@mail.com', '555-2456789', 'Calle Los Andes 121', 7, 2),
    ('Antonio', 'Ferrer', '10000072', None, 1, '2005-11-11', 1, 'antonio.ferrer72@mail.com', '555-2567890', 'Calle Las Piedras 122', 8, 1),
    ('Estela', 'Pinto', '10000073', None, 2, '2006-04-17', 2, 'estela.pinto73@mail.com', '555-2678901', 'Calle del Lago 123', 9, 2),
    ('Manuel', 'Torres', '10000074', None, 1, '2004-08-30', 3, 'manuel.torres74@mail.com', '555-2789012', 'Calle Las Palmas 124', 10, 1),
    ('Julia', 'Serrano', '10000075', None, 2, '2005-06-12', 4, 'julia.serrano75@mail.com', '555-2890123', 'Calle de la Luna 125', 11, 2),
    ('Carlos', 'Vázquez', '10000076', None, 1, '2006-11-02', 5, 'carlos.vazquez76@mail.com', '555-2901234', 'Calle de los Pinos 126', 12, 1),
    ('Mercedes', 'López', '10000077', None, 2, '2005-07-20', 6, 'mercedes.lopez77@mail.com', '555-3012345', 'Calle del Mar 127', 13, 2),
    ('Luis', 'Cortés', '10000078', None, 1, '2006-10-08', 1, 'luis.cortes78@mail.com', '555-3123456', 'Calle del Árbol 128', 14, 1),
    ('Patricia', 'Torres', '10000079', None, 2, '2004-11-14', 2, 'patricia.torres79@mail.com', '555-3234567', 'Calle del Sol 129', 15, 2),
    ('Gabriel', 'Vera', '10000080', None, 1, '2005-09-01', 3, 'gabriel.vera80@mail.com', '555-3345678', 'Calle Las Flores 130', 16, 1),
    ('Fernanda', 'Ramírez', '10000081', None, 2, '2006-09-28', 4, 'fernanda.ramirez81@mail.com', '555-3456789', 'Calle del Río 131', 17, 2),
    ('Alejandro', 'Méndez', '10000082', None, 1, '2004-06-01', 5, 'alejandro.mendez82@mail.com', '555-3567890', 'Calle del Sol 132', 1, 1),
    ('Elena', 'Luna', '10000083', None, 2, '2005-09-14', 6, 'elena.luna83@mail.com', '555-3678901', 'Calle Libertad 133', 2, 2),
    ('José', 'Sánchez', '10000084', None, 1, '2006-02-02', 1, 'jose.sanchez84@mail.com', '555-3789012', 'Calle Santa Clara 134', 3, 1),
    ('Rosana', 'Pérez', '10000085', None, 2, '2005-04-15', 2, 'rosana.perez85@mail.com', '555-3890123', 'Calle Los Laureles 135', 4, 2),
    ('Rafael', 'Torres', '10000086', None, 1, '2006-08-19', 3, 'rafael.torres86@mail.com', '555-3901234', 'Calle de la Paz 136', 5, 1),
    ('Laura', 'Martínez', '10000087', None, 2, '2004-12-22', 4, 'laura.martinez87@mail.com', '555-4012345', 'Calle Verde 137', 6, 2),
    ('Carlos', 'González', '10000088', None, 1, '2005-02-02', 5, 'carlos.gonzalez88@mail.com', '555-4123456', 'Calle Sol 138', 7, 1),
    ('María', 'Paredes', '10000089', None, 2, '2006-10-27', 6, 'maria.paredes89@mail.com', '555-4234567', 'Calle San Pedro 139', 8, 2),
    ('Antonio', 'Romero', '10000090', None, 1, '2004-09-10', 1, 'antonio.romero90@mail.com', '555-4345678', 'Calle Flores 140', 9, 1),
    ('Silvia', 'Vega', '10000091', None, 2, '2005-05-30', 2, 'silvia.vega91@mail.com', '555-4456789', 'Calle Luján 141', 10, 2),
    ('José', 'Ramírez', '10000092', None, 1, '2006-01-16', 3, 'jose.ramirez92@mail.com', '555-4567890', 'Calle Nueva 142', 11, 1),
    ('Alicia', 'López', '10000093', None, 2, '2005-12-07', 4, 'alicia.lopez93@mail.com', '555-4678901', 'Calle Buenos Aires 143', 12, 2),
    ('Marcos', 'Gutiérrez', '10000094', None, 1, '2006-07-08', 5, 'marcos.gutierrez94@mail.com', '555-4789012', 'Calle La Plata 144', 13, 1)
]


# Cargar los alumnos en la base de datos
for alumno in alumnos:
    Alumno.objects.create(
        nombre=alumno[0],
        apellido=alumno[1],
        dni=alumno[2],
        padretutor_fk_id=alumno[3],
        genero_id=alumno[4],
        fecha_nac=alumno[5],
        nacionalidad_id=alumno[6],
        email=alumno[7],
        telefono=alumno[8],
        direccion=alumno[9],
        curso_id=alumno[10],
        turno_id=alumno[11],
    )
    print('Se cargó el registro de OK')

    
    
    
    
    
    
