PROYECTO_DESARROLLO: Backend CRUD con Django y MariaDB/MySQL
📝 Descripción del Proyecto
Este repositorio contiene la aplicación Backend principal, desarrollada con el framework Django. Su función primordial es gestionar la lógica de negocio, la persistencia de datos (CRUD) y la validación estricta para una entidad de Persona (Registro de Usuarios).

Aunque este código fue subido a un repositorio con nombre de Vue, su tecnología y arquitectura es Python/Django.

🛠️ Tecnologías y Requisitos
Framework: Django (Python)

Lenguaje: Python 3.10+

Base de Datos: MariaDB o MySQL

Adaptador DB: mysqlclient (instalado en el entorno virtual)

Gestión de Versiones: Git y GitHub

📂 Arquitectura del Backend
El proyecto está organizado en dos capas principales: el Proyecto Global (crud_nuevo) y la Aplicación de Negocio (crud_app).

1. Capa de Configuración Global (crud_nuevo/)
Archivo	Rol Principal	Concepto Clave
settings.py	Configuración Maestra. Aquí se define la conexión a la base de datos (MariaDB/MySQL), se registran las aplicaciones instaladas ('crud_app') y se gestionan las configuraciones de seguridad (DEBUG, ALLOWED_HOSTS).	
urls.py	Rutas Raíz. Funciona como el enrutador principal, dirigiendo el tráfico web entrante a las rutas específicas definidas por la aplicación (crud_app).	
manage.py	Herramienta de Consola. Utilizado para ejecutar tareas administrativas de Django (runserver, makemigrations, migrate).	

Exportar a Hojas de cálculo
2. Capa de Aplicación de Negocio (crud_app/)
Archivo	Rol Principal	Concepto Clave
models.py	ORM (Mapeo Relacional de Objetos). Contiene la clase Persona, que define la estructura de la tabla en la base de datos (columnas, tipos de datos, unique=True).	
forms.py	Validación Crítica. Implementa los métodos clean_campo (p. ej., clean_dni, clean_nombres) para asegurar que los datos sean válidos (solo números, solo letras, edad mínima, unicidad) antes de guardarse.	
views.py	Lógica CRUD. Contiene las funciones de Python que manejan las peticiones HTTP (GET/POST) y ejecutan la lógica de negocio (Listar, Crear, Editar, Eliminar).	
urls.py	Rutas Específicas. Define los endpoints de la aplicación, mapeando URLs como /nuevo/ o /editar/<id>/ a las funciones dentro de views.py.	

Exportar a Hojas de cálculo
⚙️ Guía de Instalación y Ejecución Local
Para ejecutar el proyecto, es fundamental recrear el entorno virtual y asegurar la conexión con MariaDB/MySQL.

1. Configuración del Entorno Virtual
Moverse al Directorio Raíz:

Bash

cd crud_nuevo
Crear y Activar el venv:

Bash

python -m venv venv
.\venv\Scripts\activate
Instalar Dependencias: Asumiendo que se generó un archivo requirements.txt con las dependencias necesarias:

Bash

pip install -r requirements.txt
(Si no existe requirements.txt, se usaría: pip install django mysqlclient)

2. Configuración de la Base de Datos
Asegúrese de que MariaDB/MySQL esté activo (p. ej., usando XAMPP o WAMP).

Verifique las credenciales en crud_nuevo/settings.py (usuario, contraseña y nombre de la base de datos).

Aplicar Migraciones: Sincronice el modelo Persona con la base de datos.

Bash

py manage.py makemigrations crud_app
py manage.py migrate
3. Ejecución del Servidor
Bash

py manage.py runserver
La aplicación será accesible a través de http://127.0.0.1:8000/.

🔗 Integración con el Frontend (React/Vue)
El Frontend (TALLERREACT) se comunica con este Backend utilizando peticiones HTTP (GET, POST, PUT, DELETE) dirigidas a los endpoints definidos en crud_app/urls.py.

Separación de Servidores: El Backend corre en http://127.0.0.1:8000/ y el Frontend (React/Vue) corre en http://localhost:3000.

CORS: Para que esta comunicación funcione, la configuración de CORS debe ser manejada en el servidor Django (generalmente agregando la librería django-cors-headers y configurando CORS_ALLOWED_ORIGINS en settings.py).
