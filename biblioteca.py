# ============================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# ============================================

# ------------------------------
# Clase Libro
# ------------------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla para guardar titulo y autor
        # porque no deben cambiar después de crear el libro
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        return f"Título: {self.obtener_titulo()} | Autor: {self.obtener_autor()} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# ------------------------------
# Clase Usuario
# ------------------------------
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

        # Lista para almacenar los libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("El usuario no tiene libros prestados")
        else:
            print("Libros prestados:")
            for libro in self.libros_prestados:
                print("-", libro.obtener_titulo())

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"


# ------------------------------
# Clase Biblioteca
# ------------------------------
class Biblioteca:
    def __init__(self):

        # Diccionario para guardar libros usando ISBN como clave
        self.libros = {}

        # Diccionario para guardar usuarios
        self.usuarios = {}

        # Conjunto para asegurar IDs únicos
        self.ids_usuarios = set()

    # --------------------------
    # Añadir libro
    # --------------------------
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente")
        else:
            print("El libro ya existe")

    # --------------------------
    # Quitar libro
    # --------------------------
    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # --------------------------
    # Registrar usuario
    # --------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente")
        else:
            print("El ID de usuario ya existe")

    # --------------------------
    # Eliminar usuario
    # --------------------------
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # --------------------------
    # Prestar libro
    # --------------------------
    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no encontrado")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        libro = self.libros[isbn]

        if libro.prestado:
            print("El libro ya está prestado")
        else:
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            libro.prestado = True
            print("Libro prestado correctamente")

    # --------------------------
    # Devolver libro
    # --------------------------
    def devolver_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no encontrado")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        usuario.devolver_libro(libro)
        libro.prestado = False
        print("Libro devuelto correctamente")

    # --------------------------
    # Buscar por título
    # --------------------------
    def buscar_por_titulo(self, titulo):
        print("Resultados de búsqueda:")
        for libro in self.libros.values():
            if titulo.lower() in libro.obtener_titulo().lower():
                print(libro)

    # --------------------------
    # Buscar por autor
    # --------------------------
    def buscar_por_autor(self, autor):
        print("Resultados de búsqueda:")
        for libro in self.libros.values():
            if autor.lower() in libro.obtener_autor().lower():
                print(libro)

    # --------------------------
    # Buscar por categoría
    # --------------------------
    def buscar_por_categoria(self, categoria):
        print("Resultados de búsqueda:")
        for libro in self.libros.values():
            if categoria.lower() in libro.categoria.lower():
                print(libro)

    # --------------------------
    # Listar libros de usuario
    # --------------------------
    def listar_libros_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.listar_libros()
        else:
            print("Usuario no encontrado")


# ============================================
# PRUEBA DEL SISTEMA
# ============================================

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "111")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "222")
libro3 = Libro("Python para principiantes", "Juan Pérez", "Tecnología", "333")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Lui Rojas", "U001")
usuario2 = Usuario("Chris Morales", "U002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("111", "U001")

# Listar libros prestados
biblioteca.listar_libros_usuario("U001")

# Buscar libro
biblioteca.buscar_por_autor("Cervantes")

# Devolver libro
biblioteca.devolver_libro("111", "U001")

# Listar nuevamente
biblioteca.listar_libros_usuario("U001")
