# Pre-entrega-3

# Curso
- Curso de Python
- Comisión Nº 60095 
- Prof. Esteban Acevedo

# Alumno
- Nombre: Daniel Helman


# Sistema de Gestión de Obras Sociales

Este proyecto es una aplicación Django que permite gestionar obras sociales, planes de salud y afiliados. Incluye formularios para agregar información en cada una de estas entidades.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener:

- Python 3.12 o superior
- Django 5.1.4
- Un entorno virtual configurado

## Instalación

1. Clona este repositorio.
   ```bash
   git clone <URL-del-repositorio>
   cd <directorio-del-repositorio>
   ```

2. Activa el entorno virtual.
   ```bash
   # En Windows
   .\.venv\Scripts\activate

   # En macOS/Linux
   source .venv/bin/activate
   ```

3. Instala las dependencias.
   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones para configurar la base de datos.
   ```bash
   python manage.py migrate
   ```

5. Inicia el servidor de desarrollo.
   ```bash
   python manage.py runserver
   ```

## Orden para probar las funcionalidades

### 1. Inicio del sistema

1. Accede a la URL principal: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Verifica que se muestre el menú principal con las siguientes opciones:
   - **Agregar Obra Social**
   - **Agregar Plan de Salud**
   - **Agregar Afiliado**

### 2. Agregar una obra social

1. Haz clic en **Agregar Obra Social**.
2. Completa el formulario con los datos requeridos y haz clic en **Guardar**.
3. Verifica que seas redirigido a la página principal y que la obra social haya sido guardada correctamente en la base de datos (puedes verificarlo desde el panel de admin si está habilitado).

### 3. Agregar un plan de salud

1. Haz clic en **Agregar Plan de Salud**.
2. Completa el formulario con los datos requeridos y haz clic en **Guardar**.
3. Verifica que seas redirigido a la página principal y que el plan de salud haya sido guardado correctamente en la base de datos.

### 4. Agregar un afiliado

1. Haz clic en **Agregar Afiliado**.
2. Completa el formulario con los datos requeridos, incluyendo:
   - DNI
   - Nombre y apellido
   - ID de afiliado
   - Obra social asociada (si aplica)
3. Haz clic en **Guardar**.
4. Verifica que seas redirigido a la página principal y que el afiliado haya sido guardado correctamente en la base de datos.


## Notas adicionales

- Si se requiere editar una obra social, plan de salud o afiliado, puedes habilitar estas opciones en el panel de administración de Django.
- Si encuentras algún error, verifica los mensajes en la consola del servidor o revisa la configuración de los formularios en `forms.py` y las vistas en `views.py`.

## Futuras mejoras

- Implementar un listado para visualizar y editar las entidades directamente desde la interfaz.
- Agregar validaciones adicionales en los formularios.
- Mejorar el diseño de la interfaz utilizando un framework CSS como Bootstrap.

---
gi
Si tienes preguntas o comentarios, no dudes en comunicarte con el equipo de desarrollo.

