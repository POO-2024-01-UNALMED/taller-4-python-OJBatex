from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

asignatura1 = Asignatura("Vision por Computador")
asignatura2 = Asignatura("POO", "Salon 503B")

if __name__ == "main":
    print(asignatura1._nombre)