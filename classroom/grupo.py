from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes = None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

        if self._asignaturas == None:
            self._asignaturas = []
        if self.listadoAlumnos == None:
            self.listadoAlumnos = []

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas == None:
            self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if self.listadoAlumnos == None:
             self.listadoAlumnos = []
        if lista != None:
            for i in lista:
                self.listadoAlumnos.append(i)
        self.listadoAlumnos.append(alumno)
            
    def __str__(self):
        cadena = f"Grupo de estudiantes: {self._grupo}"
        return cadena

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
