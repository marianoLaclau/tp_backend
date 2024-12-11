from apps.inscripciones.models import Materia, Curso
from apps.administracion.models import Genero, Turno, Nacionalidad, Docente

docentes = [
    (16, 'Carlos', 'Martínez', 'carlos.martinez5@mail.com', 'Calle del Mar 102', 1, '31000001', 5, '555-5678901', 1,5),
    (2, 'Ana', 'García', 'ana.garcia6@mail.com', 'Calle Mayor 103', 2, '31000002', 6, '555-6789012', 2,6),
    (3, 'Luis', 'Hernández', 'luis.hernandez7@mail.com', 'Calle del Árbol 104', 1, '31000003', 1, '555-7890123', 1,7),
    (4, 'Patricia', 'López', 'patricia.lopez8@mail.com', 'Calle del Río 105', 2, '31000004', 2, '555-8901234', 2,8),
    (5, 'Marta', 'Vázquez', 'marta.vazquez9@mail.com', 'Calle de la Luna 106', 1, '31000005', 3, '555-9981723', 1,9),
    (6, 'Ricardo', 'Ramírez', 'ricardo.ramirez10@mail.com', 'Calle Pinos 107', 2, '31000006', 4, '555-1012345', 2,10),
    (7, 'Jorge', 'Álvarez', 'jorge.alvarez11@mail.com', 'Calle Santa Fe 108', 1, '31000007', 5, '555-1123456', 1,11),
    (8, 'Silvia', 'Mendoza', 'silvia.mendoza12@mail.com', 'Calle Argentina 109', 2, '31000008', 6, '555-1234568', 2,12),
    (9, 'Daniel', 'Torres', 'daniel.torres13@mail.com', 'Calle Libertad 110', 1, '31000009', 1, '555-1345679', 1,13),
    (10, 'Laura', 'Jiménez', 'laura.jimenez14@mail.com', 'Calle Rosas 111', 2, '31000010', 2, '555-1456789', 2,14),
    (11, 'Roberto', 'González', 'roberto.gonzalez15@mail.com', 'Calle Nueva 112', 1, '31000011', 3, '555-1567890', 1, 4),
    (12, 'Verónica', 'Díaz', 'veronica.diaz16@mail.com', 'Calle Parque 113', 2, '31000012', 4, '555-1678901', 2, 6),
    (13, 'Héctor', 'Martín', 'hector.martin17@mail.com', 'Calle San Martín 114', 1, '31000013', 5, '555-1789012', 1, 4),
    (14, 'Estela', 'Pinto', 'estela.pinto18@mail.com', 'Calle Lago 123', 2, '31000014', 6, '555-1890123', 1, 2),
    (2, 'Manuel', 'Torres', 'manuel.torres19@mail.com', 'Calle Palmas 124', 1, '31000015', 1, '555-1901234', 1, 6),
    (3, 'Julia', 'Serrano', 'julia.serrano20@mail.com', 'Calle Luna 125', 2, '31000016', 2, '555-2012345', 1, 7),
    (2, 'Ricardo', 'Sánchez', 'ricardo.sanchez21@mail.com', 'Calle Sol 126', 1, '31000017', 3, '555-2123456', 1, 5),
    (3, 'Alfredo', 'Morales', 'alfredo.morales22@mail.com', 'Calle Las Palmas 127', 2, '31000018', 4, '555-2234567', 1, 4),
    (2, 'Elena', 'Hernández', 'elena.hernandez23@mail.com', 'Calle Las Lomas 128', 1, '31000019', 5, '555-2345678', 1, 4),
    (2, 'César', 'González', 'cesar.gonzalez24@mail.com', 'Calle Santa Rosa 129', 2, '31000020', 6, '555-2456789', 1, 6),
    (8, 'Sara', 'Pérez', 'sara.perez25@mail.com', 'Calle Centro 130', 1, '31000021', 1, '555-2567890', 2, 4),
    (2, 'Miguel', 'Rodríguez', 'miguel.rodriguez26@mail.com', 'Calle Real 131', 2, '31000022', 2, '555-2678901', 2, 4),
    (10, 'Ana', 'Jiménez', 'ana.jimenez27@mail.com', 'Calle De Las Flores 132', 1, '31000023', 3, '555-2789012', 2, 6),
    (2, 'Gabriela', 'Moreno', 'gabriela.moreno28@mail.com', 'Calle Azul 133', 2, '31000024', 4, '555-2890123', 1, 7),
    (7, 'Juan', 'Pérez', 'juan.perez29@mail.com', 'Calle Margarita 134', 1, '31000025', 5, '555-2901234', 1, 8),
    (2, 'Isabel', 'Fernández', 'isabel.fernandez30@mail.com', 'Calle Los Álamos 135', 2, '31000026', 6, '555-3012345', 2, 4),
    (5, 'Eduardo', 'Soto', 'eduardo.soto31@mail.com', 'Calle Los Olivos 136', 1, '31000027', 1, '555-3123456',1, 2),
]




for docente in docentes:
    Docente.objects.create(
        materia_id=docente[0],   
        nombre=docente[1],             
        apellido=docente[2],           
        email=docente[3],              
        direccion=docente[4],          
        genero_id=docente[5],          
        dni=docente[6],               
        nacionalidad_id=docente[7],    
        telefono=docente[8],           
        turno_id=docente[9],           
        curso_id=docente[10],
    )
    print('Se cargó el registro de OK')
