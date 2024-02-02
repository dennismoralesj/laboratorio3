class Estudiante:
    def __init__(self, nombre, apellido, edad, calificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.calificacion = calificacion

    def aprovado(self):
        return self.calificacion >=60

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
apellido_estudiante = input("Ingrese el apellido del estudiante: ")
edad_estudiante = int(input("Ingrese la edad del estudiante: "))
calificacion_estudiante = float(input("Ingrese la calificación del estudiante: "))

estudiante = Estudiante(nombre_estudiante, apellido_estudiante,edad_estudiante, calificacion_estudiante)

if estudiante.aprovado():
    print("El estudiante ",nombre_estudiante, "ah sido aprobado")
else:
    print("El estudiante ",nombre_estudiante, "ah sido reprobado")