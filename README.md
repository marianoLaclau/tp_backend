# Proyecto de Gestión Administrativa Para Institucion Educativa

Este es un sistema de gestión escolar desarrollado en Django como parte de un trabajo final para la materia **Desarrollo de Sistemas Web Backend**. 
El proyecto está diseñado para facilitar la administración de datos académicos y administrativos de un instituto, incluyendo roles diferenciados para **administración** y **docentes**.
Su principal proposito es almacenar y centralizar todos los datos relevantes para la institucion , tanto para facilitar las tareas diarias , como tambien para poder generar analisis de datos en el futuro 
y crear reportes o paneles que puedan ayudar a tomar mejores decisiones en la gestion general .

---

## Cómo Ejecutar el Proyecto

### Requisitos

- Python 3.9+
- pip
- **Librería requerida:** `django-widget-tweaks`

Para instalar la librería, ejecuta:

bash

```pip install django-widget-tweaks```



### Pasos para Iniciar el Proyecto

1. **Inicia el servidor de desarrollo:**

La base de datos ya está preconfigurada, por lo que no es necesario aplicar migraciones ni configurar datos iniciales. Solo ejecuta el servidor:

bash

```python manage.py runserver```

2. **Accede al sistema:**

Una vez que el servidor esté corriendo, abre tu navegador en la URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Serás redirigido automáticamente a la pantalla de inicio de sesión.

---

## Datos de Acceso

| Usuario    | Rol          | Contraseña |
|------------|--------------|------------|
| `@anadmin` | Administrador | `35665878` |
| `@ana`     | Docente       | `35665878` |


---

## Notas Adicionales

- Este proyecto incluye la base de datos preconfigurada, por lo que no es necesario realizar migraciones ni configuraciones adicionales.

---


