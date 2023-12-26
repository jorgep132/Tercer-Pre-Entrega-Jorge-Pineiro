# Tercer Pre-Entrega / Coderhouse Python - 50190
***
Diseño básico de web, donde se implementan modelos y formularios, utilizando Django.
***

### Información general
En este proyecto lo escencial es el manejo de los models y formularios dentro de la web.
Contamos con tres modelos y un inicio, el cual servira de buscador: 

1.**Inicio**:
  - Descripción: Este modelo representa el inicio/index de la web, el cual contiene un formulario de busqueda de cursos, utilizando el numero de camada:
  - Atributos:
    - camada
2.  **Cursos**:
  - Descripción: Este modelo contiene un formulario de carga de datos de cursos:
  - Atributos:
    - nombre_curso
    - camada
3. **Estudiantes**:
  - Descripción: Este modelo contiene un formulario de carga de datos de estudiantes:
  - Atributos:
    - nombre_estudiante
    - apellido_estudiante
    - email_estudiante
4. **Entregables**:
  - Descripción: Este modelo contiene un formulario de carga de datos de las entregas de los estudiantes:
  - Atributos:
    - nombre_estudiantes
    - fecha_entrga
    - entregado
    - 
Estos modelos son fundamentales para el funcionamiento del proyecto, ya que abarcan aspectos clave como la información de los estudiantes, los detalles de los cursos y el seguimiento de las entregas.

***
## Utilización
***
Seguí estos pasos para probar la funcionalidad del programa:
1. **Inicio/Index:**
   - Ubica el modelo "Inicio" en el directorio `Entrega3/models`.
   - Ejecuta el formulario de búsqueda de cursos utilizando el número de camada del curso.

2. **Carga de Datos de Cursos:**
   - Ubica el modelo "Cursos" en `Entrega3/models`.
   - Utiliza el formulario de carga de datos de cursos en la interfaz de administrador o la ruta específica.

3. **Carga de Datos de Estudiantes:**
   - Ubica el modelo "Estudiantes" en `Entrega3/models`.
   - Utiliza el formulario de carga de datos de cursos en la interfaz de administrador o la ruta específica.

4. **Carga de Datos de Entregables:**
   - Ubica al modelo "Entregables" en `Entrega3/models`.
   - Utiliza el formulario de carga de datos de cursos en la interfaz de administrador o la ruta específica.

***
## Herramientas y tecnologías utilizadas
***
Disstintas tecnologías utilizadas:
* Visual Studio Code (https://code.visualstudio.com/): Version 1.85.1
* Python: Version 3.11.7
* Django: Version 23.3.1

***
## Instalación
Sigue el paso a paso para poder instalar el proyecto:
1. Clona el repositorio:
   $ git clone https://example.com
2. Navega al directorio del proyecto:
  $ cd path/to/the/project
3. Instala las dependencias:
  $ npm install
4. Inicia el proyecto:
  $ npm start
 

