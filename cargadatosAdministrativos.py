from apps.administracion.models import Turno, Genero, Nacionalidad, PersonalAdmin

personal_admin = [
    ('Ana', 'Pérez', '20345001', 'Calle Ficticia 201', '555-1000001', 'ana.perez@admin.com', 1, 1, 2),
    ('Luis', 'González', '20345002', 'Avenida Sol 202', '555-1000002', 'luis.gonzalez@admin.com', 2, 2, 3),
    ('María', 'Rodríguez', '20345003', 'Calle Real 203', '555-1000003', 'maria.rodriguez@admin.com', 1, 1, 4),
    ('Carlos', 'Martínez', '20345004', 'Calle Luna 204', '555-1000004', 'carlos.martinez@admin.com', 2, 2, 5),
    ('Patricia', 'Sánchez', '20345005', 'Calle Agua 205', '555-1000005', 'patricia.sanchez@admin.com', 1, 1, 6),
    ('Juan', 'Torres', '20345006', 'Calle Norte 206', '555-1000006', 'juan.torres@admin.com', 2, 2, 1),
    ('Laura', 'Fernández', '20345007', 'Calle Oeste 207', '555-1000007', 'laura.fernandez@admin.com', 1, 1, 2),
    ('Ricardo', 'López', '20345008', 'Calle Este 208', '555-1000008', 'ricardo.lopez@admin.com', 2, 2, 3),
    ('Estela', 'Gómez', '20345009', 'Avenida Argentina 209', '555-1000009', 'estela.gomez@admin.com', 1, 1, 4),
    ('Marta', 'Ramírez', '20345010', 'Calle Sur 210', '555-1000010', 'marta.ramirez@admin.com', 2, 2, 5),
    ('César', 'Mendoza', '20345011', 'Calle Central 211', '555-1000011', 'cesar.mendoza@admin.com', 1, 1, 6),
    ('Verónica', 'Álvarez', '20345012', 'Calle San Martín 212', '555-1000012', 'veronica.alvarez@admin.com', 2, 2, 1),
    ('Jorge', 'Jiménez', '20345013', 'Calle Lomas 213', '555-1000013', 'jorge.jimenez@admin.com', 1, 1, 2),
    ('Silvia', 'Morales', '20345014', 'Calle Chica 214', '555-1000014', 'silvia.morales@admin.com', 2, 2, 3),
    ('Daniel', 'Vázquez', '20345015', 'Calle Mayor 215', '555-1000015', 'daniel.vazquez@admin.com', 1, 1, 4),
    ('Alfredo', 'González', '20345016', 'Calle Río 216', '555-1000016', 'alfredo.gonzalez@admin.com', 2, 2, 5),
    ('Julia', 'Torres', '20345017', 'Calle Primavera 217', '555-1000017', 'julia.torres@admin.com', 1, 1, 6),
    ('Ricardo', 'Pinto', '20345018', 'Calle Valle 218', '555-1000018', 'ricardo.pinto@admin.com', 2, 2, 1),
    ('Gabriela', 'Ramírez', '20345019', 'Calle Pacifico 219', '555-1000019', 'gabriela.ramirez@admin.com', 1, 1, 2),
    ('Miguel', 'Serrano', '20345020', 'Calle Libertad 220', '555-1000020', 'miguel.serrano@admin.com', 2, 2, 3),
]

for admin in personal_admin:
    PersonalAdmin.objects.create(
        nombre=admin[0],           
        apellido=admin[1],         
        dni=admin[2],              
        direccion=admin[3],        
        telefono=admin[4],         
        email=admin[5],            
        turno_id=admin[6],         
        genero_id=admin[7],        
        nacionalidad_id=admin[8],  
    )
    print('Se cargó el registro de Personal Administrativo OK')
