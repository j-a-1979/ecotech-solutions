from abc import ABC, abstractmethod

from decorator import DEF


# CLASE ABSTRACTA USUARIO
# SEGUN EL DIAGRAMA UML, 2 CLASES HEREDAN DE ESTA:
    # EMPLEADO
    # ADMIN

class Usuario(ABC):

    @abstractmethod
    def idUsuario(self):
        pass

    @abstractmethod
    def nombreUsuario(self):
        pass

    @abstractmethod
    def contrasenaHash(self):
        pass

    @abstractmethod
    def rol(self):
        pass


    # METODOS
    
    def autenticar(self, contrasenaIngresada):
        # Aquí se implementaría la lógica de autenticación
        # Por ejemplo, comparar el hash de la contraseña ingresada con el hash almacenado
        pass

    def tieneAcceso(self, modulo):
        # Aquí se implementaría la lógica para verificar si el usuario tiene acceso a un módulo específico
        # Por ejemplo, verificar el rol del usuario y los permisos asociados a ese rol
        pass

class Empleado(Usuario):

    def __init__(self, idUsuario, nombreUsuario, contrasenaHash):
        self._idUsuario = idUsuario
        self._nombreUsuario = nombreUsuario
        self._contrasenaHash = contrasenaHash
        self._rol = "Empleado"

    def idUsuario(self):
        return self._idUsuario

    def nombreUsuario(self):
        return self._nombreUsuario

    def contrasenaHash(self):
        return self._contrasenaHash

    def rol(self):
        return self._rol

    # METODOS ABSTRACTOS
    
    def autenticar(self, contrasenaIngresada):
        # Aquí se implementaría la lógica de autenticación
        # Por ejemplo, comparar el hash de la contraseña ingresada con el hash almacenado
        pass

    def tieneAcceso(self, modulo):
        # Aquí se implementaría la lógica para verificar si el usuario tiene acceso a un módulo específico
        # Por ejemplo, verificar el rol del usuario y los permisos asociados a ese rol
        pass

        

    def actualizarDatos(self, nuevosDatos):
        # Aquí se implementaría la lógica para actualizar los datos del empleado
        pass

    def registrarHoras(self, horas):
        # Aquí se implementaría la lógica para registrar las horas trabajadas por el empleado
        pass

    def calcularAntiguedad(self, fechaIngreso):
        # Aquí se implementaría la lógica para calcular la antigüedad del empleado
        pass
    
class Admin(Usuario):

    def __init__(self, idUsuario, nombreUsuario, contrasenaHash):
        self._idUsuario = idUsuario
        self._nombreUsuario = nombreUsuario
        self._contrasenaHash = contrasenaHash
        self._rol = "Admin"

    def idUsuario(self):
        return self._idUsuario

    def nombreUsuario(self):
        return self._nombreUsuario

    def contrasenaHash(self):
        return self._contrasenaHash

    def rol(self):
        return self._rol


     # METODOS ABSTRACTOS
    
    def autenticar(self, contrasenaIngresada):
        # Aquí se implementaría la lógica de autenticación
        # Por ejemplo, comparar el hash de la contraseña ingresada con el hash almacenado
        pass

    def tieneAcceso(self, modulo):
        # Aquí se implementaría la lógica para verificar si el usuario tiene acceso a un módulo específico
        # Por ejemplo, verificar el rol del usuario y los permisos asociados a ese rol
        pass

    # METODOS UNICOS DE CLASE   

    def registrarEmpleado(self, empleado):
        # Aquí se implementaría la lógica para registrar un nuevo empleado
        pass

    def generarInforme(self, tipo):
        # Aquí se implementaría la lógica para generar un informe
        pass

class Departamento:
    def __init__(self, nombre, gerente):
        self._nombre = nombre
        self._gerente = gerente


    # Metodo para asignar nombre a departamento?

    def nombre(self):
        return self._nombre

    def asignarEmpleado(self, empleado):
        # Aquí se implementaría la lógica para asignar un empleado al departamento
        pass

    def reasignarEmpleado(self, empleado, nuevoDepartamento):
        # Aquí se implementaría la lógica para reasignar un empleado a un nuevo departamento
        pass

    def buscar(self, criterio):
        # Aquí se implementaría la lógica para buscar empleados en el departamento según un criterio
        pass

class Informe:
    def __init__(self, tipo, fechaGeneracion):
        self._tipo = tipo
        self._fecha = fechaGeneracion

    def tipo(self):
        return self._tipo

    def fechaGeneracion(self):
        return self._fecha
    
    def generar(self):
        # Aquí se implementaría la lógica para generar el informe
        pass

class RegistroDeTiempo:
    def __init__(self, fecha, horasTrabajadas, descripcionTarea):
        self._fecha = fecha
        self._horasTrabajadas = horasTrabajadas
        self._descripcionTarea = descripcionTarea

    def fecha(self):
        return self._fecha

    def horasTrabajadas(self):
        return self._horasTrabajadas

    def descripcionTarea(self):
        return self._descripcionTarea

    def validar(self):
        # Aquí se implementaría la lógica para validar el registro de tiempo
        pass

class Proyecto:
    def __init__(self, nombre, descripcion, fechaInicio, fechaFin):
        self._nombre = nombre
        self._descripcion = descripcion
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin


    def nombre(self):
        return self._nombre

    def descripcion(self):
        return self._descripcion

    def fechaInicio(self):
        return self._fechaInicio

    def fechaFin(self):
        return self._fechaFin



    def asignarEmpleado(self, empleado):
        # Aquí se implementaría la lógica para asignar un empleado al proyecto
        pass

    def deasignarEmpleado(self, empleado):
        # Aquí se implementaría la lógica para desasignar un empleado del proyecto
        pass

    