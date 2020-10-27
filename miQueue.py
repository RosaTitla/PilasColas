from Estudiante import Estudiante
from Queue import Queue
fila=Queue()

#creo el objeto Estudiante1 y lo apilo
miEstudiante1 = Estudiante("2299", "Pedro", "Nanotecnología")
fila.agregarAlaCola(miEstudiante1)

#creo el objeto Estudiante2 y lo apilo
miEstudiante2 = Estudiante("3209", "Ezequiel", "Ing. en IA")
fila.agregarAlaCola(miEstudiante2)
#miPila.desapilar()

#creo el objeto Estudiante3 y lo apilo
miEstudiante3 = Estudiante("3233", "Isaias", "Ing. en Ciencia de datos")
fila.agregarAlaCola(miEstudiante3)

#creo el objeto Estudiante4 y lo apilo
miEstudiante4 = Estudiante("3119", "Emmanuel", "Ing. en TI")
fila.agregarAlaCola(miEstudiante4)


print('longitud de la fila:',len(fila))
#mostrar la pila de estudiantes
for ele in fila:
    print(ele)

print('Pila después de despachar al primero de la fila')

fila.extraerDeLaCola()
for ele in fila:
    print(ele)