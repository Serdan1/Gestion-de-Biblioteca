# Gestion-de-Biblioteca

https://github.com/Serdan1/Gestion-de-Biblioteca.git


# Sistema de Gestión de Biblioteca

Este proyecto es un sistema básico de gestión de biblioteca desarrollado en Python como parte de un ejercicio práctico. Permite catalogar libros, gestionar usuarios, realizar préstamos y devoluciones, y consultar la disponibilidad de libros. El sistema ofrece dos interfaces: una gráfica (usando Tkinter) y una basada en consola.

## Características

- **Catalogación de libros**: Añade libros con título, autor, género, y estado de disponibilidad.
- **Gestión de usuarios**: Registra usuarios y permite que tomen prestados y devuelvan libros.
- **Gestión de empleados**: Los empleados pueden añadir y eliminar libros, y gestionar usuarios.
- **Interfaz gráfica**: Una interfaz con Tkinter para interactuar con el sistema de forma visual.
- **Interfaz de consola**: Una alternativa para usar el sistema en entornos sin soporte gráfico (como Codespaces).
- **Persistencia de datos**: Los datos se guardan en archivos JSON (`books.json`, `users.json`, `employees.json`).

## Requisitos

### Para la Interfaz Gráfica
- Python 3.6 o superior.
- Tkinter (normalmente incluido con Python en Windows y macOS; en Linux, instalar con `sudo apt install python3-tk`).
- Un entorno con soporte gráfico (no funciona en entornos como Codespaces sin configuración adicional).

### Para la Interfaz de Consola
- Python 3.6 o superior.
- Funciona en cualquier entorno, incluyendo Codespaces.

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Serdan1/Gestion-de-Biblioteca.git
   cd Gestion-de-Biblioteca
  
  - Asegúrate de tener Python instalado
  - Verifica Tkinter (para la interfaz gráfica)


## Uso
Interfaz Gráfica (Recomendada para Máquina Local)

Ejecuta el programa:
En Windows:
cmd
cd C:\ruta\a\Gestion-de-Biblioteca
python main.py

En Linux/macOS:
bash
cd /ruta/a/Gestion-de-Biblioteca
python3 main.py

Interfaz:
Añade libros usando los campos "Título", "Autor", y "Género".

Añade usuarios con "ID de Usuario" y "Nombre de Usuario".

Presta o devuelve libros seleccionándolos de la lista e ingresando el ID del usuario.

Haz clic en "Salir" para guardar los datos.

## Archivos Generados

books.json: Almacena los libros.
users.json: Almacena los usuarios y sus libros prestados.
employees.json: Almacena los empleados.

Estos archivos se generan automáticamente al usar el programa y están ignorados en el .gitignore.

```mermaid
flowchart TD
    A[Inicio: Usuario quiere prestar un libro] --> B[Seleccionar un libro de la lista]
    B --> C{¿El libro está disponible?}
    C -- Sí --> D[Ingresar ID del usuario]
    D --> E{¿El usuario existe?}
    E -- Sí --> F[Prestar el libro al usuario]
    F --> G[Marcar libro como no disponible]
    G --> H[Actualizar lista de libros prestados del usuario]
    H --> I[Guardar cambios en JSON]
    I --> J[Éxito: Libro prestado]
    C -- No --> K[Error: Libro no disponible]
    E -- No --> L[Error: Usuario no encontrado]
    K --> M[Fin]
    L --> M[Fin]
    J --> M[Fin]
