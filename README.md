# Sistema de Administración de Biblioteca Digital

Descripción

El presente proyecto implica la creación de un sistema elemental para la gestión de una biblioteca digital utilizando Python. Este sistema facilita la organización de los libros disponibles, la inscripción de usuarios y el seguimiento del préstamo y regreso de libros.

La meta es implementar nociones de programación orientada a objetos y emplear diversas estructuras de datos tales como listas, tuplas, diccionarios y conjuntos.

---

Funcionalidades del sistema

El sistema permite llevar a cabo las siguientes acciones:

- Incorporar libros a la biblioteca
- Quitar libros del catálogo
- Incribir nuevos usuarios
- Eliminar usuarios registrados
- Prestar libros a los usuarios
- Retornar libros prestados
- Buscar libros por título
- Buscar libros por autor
- Buscar libros por género
- Enumerar los libros prestados a un usuario

---

Estructuras de datos utilizadas

En la creación del sistema se emplearon varias estructuras de datos:

- Tuplas: Para almacenar el título y el autor del libro, dado que estos detalles son inalterables.
- Listas: Para mantener un registro de los libros prestados a cada usuario.
- Diccionarios: Para guardar los libros utilizando el ISBN como clave.
- Conjuntos (set): Para garantizar que los identificadores de los usuarios sean únicos.

---

Clases implementadas

# Clase Libro
Representa un libro en el sistema con los siguientes atributos:
- título
- autor
- categoría
- ISBN
- estado del préstamo

# Clase Usuario
Representa un usuario que está registrado en la biblioteca:
- nombre
- ID de usuario
- lista de libros prestados

# Clase Biblioteca
Administra todo el sistema de la biblioteca:
- registro de libros
- registro de usuarios
- gestión de préstamos
- gestión de devoluciones
- búsquedas en el catálogo

---

Pruebas del sistema

Para verificar el funcionamiento del sistema, se crearon varios libros y usuarios. Luego, se realizaron acciones como añadir libros, registrar usuarios, prestar libros, devolverlos y ejecutar búsquedas.

---

Lenguaje utilizado

Python 3
